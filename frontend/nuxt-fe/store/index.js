export const state = () => ({
  list: [],
  userChoice: [],
  downloads: 0,
  isFetchingPptx: false,
  isDownloads: false,
  currentRoute: null,
  taskAlerts: [],
  taskList: [],
  routeNow: null,
  isDropdownVisible: false



})


export const mutations = {
  toggleDropdownOn(state) {
    state.isDropdownVisible = true
    const body = document.getElementsByTagName('body')[0];
    body.classList.add("overflow-hidden")
  },
  toggleDropdownOff(state) {
    state.isDropdownVisible = false
    const body = document.getElementsByTagName('body')[0];
    body.classList.remove("overflow-hidden");
  },
  changeDropdownVis(state) {
    state.isDropdownVisible = !state.isDropdownVisible
    const body = document.getElementsByTagName('body')[0];

    if (state.isDropdownVisible) {
      const body = document.getElementsByTagName('body')[0];
      body.classList.add("overflow-hidden")
    }
    else {
      const body = document.getElementsByTagName('body')[0];
      body.classList.remove("overflow-hidden");
    }
  },

  testUpdate(state, route) {
    state.routeNow = route

  },
  turnDownloadOn(state, taskID) {
    var taskList = state.taskList
    var foundIndex = taskList.findIndex(x => x.taskID == taskID)
    taskList[foundIndex]["downloading"] = true
  },
  turnDownloadOff(state, taskID) {
    var taskList = state.taskList
    var foundIndex = taskList.findIndex(x => x.taskID == taskID)
    taskList[foundIndex]["downloading"] = false
  },
  updateList(state, payload) {
    state.list = payload
  },
  appendList(state, payload) {
    state.list.push(payload)
  },
  updateUserChoiceList(state, payload) {
    state.userChoice = payload
  },
  appendUserChoice(state, payload) {
    state.userChoice.push(payload)
  },
  deleteUserChoice(state, payload) {
    state.userChoice.splice(payload, 1)
  },
  deleteListItem(state, payload) {
    state.list.splice(payload, 1)
  },
  changeDownloadCount(state) {
    state.downloads++;
  },
  changeDownloadStatus(state) {
    state.isFetchingPptx = !state.isFetchingPptx
  },
  activateDownloads(state) {
    state.isDownloads = !state.isDownloads
  },
  changeCurrentRoute(state, payload) {
    state.currentRoute = payload
  },
  addTaskAlert(state, payload) {
    state.taskAlerts.push(payload)
  },
  updateTaskList(state, payload) {
    state.taskList.push(payload)
  },
  clearTaskList(state) {
    state.taskList = []
  },
  deleteTaskAlert(state, payload) {
    state.taskAlerts.splice(payload, 1);
  },
  clearAlertList(state) {
    this.state.taskAlerts = []
  },
  updateLocalStorage(state) {
    let taskList = state.taskList
    localStorage.setItem('taskList', JSON.stringify(taskList))
  },
  initialiseStore(state) {

    if (localStorage.getItem('taskList')) {
      state.taskList = JSON.parse(localStorage.getItem('taskList'))
    }

  }




}

export const actions = {
  updateList: ({ commit }, payload) => {
    commit('updateList', payload);
  },
  appendList: ({ commit }, payload) => {
    commit('appendList', payload);
  },
  appendUserChoice: ({ commit }, payload) => {
    commit('appendUserChoice', payload);
  },
  updateUserChoiceList({ commit }, payload) {
    commit('updateUserChoiceList', payload);
  },
  deleteUserChoice({ commit }, payload) {
    commit('deleteUserChoice', payload);
  },

  deleteListItem({ commit }, payload) {
    commit('deleteListItem', payload);
  },

  clearAlertList({ commit }) {
    commit('clearAlertList');

  },

  // API Calls //
  async sendTask({ commit, rootState }) {
    
    let onBoardingDeck = JSON.stringify({
      "sections": this.state.userChoice,
      "user": rootState.auth.user,
      "user_id": rootState.auth.userID
    })
    var config = {
      headers: {
        'Content-Type': 'application/json',
      },

    };

    const send = await this.$axios.$post('/v1/pptx/pptxjob', onBoardingDeck, config)
      .then((res) => {


        if (res.status == "success") {
          let alert = {
            'alertType': 'Info',
            'alertID': 'Job triggered successfully',
            'alertColor': 'green'
          }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);

        }
        else if (res.status == "no_sections") {
          let alert = {
            'alertType': 'Sections',
            'alertID': "Please select sections",
            'alertColor': 'red'
          }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }
        else if (res.status == "pptx_exists") {
          let alert = {
            'alertType': 'Powerpoint',
            'alertID': "Looks the requested deck already exists under Downloads",
            'alertColor': 'red'
          }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }



      })
      .catch((err) => {
        let stringErr = String(err)
        let alert = {
          'alertType': 'API Error',
          'alertID': stringErr.replace('Error: ', ''),
          'alertColor': 'red'
        }
        commit('addTaskAlert', alert);
        commit('changeDownloadStatus');

      });


  },

  async downloadPresentation({ commit, dispatch }, task) {
    let taskID = JSON.stringify({ "taskID": task })
    commit('changeDownloadCount');
    commit('turnDownloadOn', task);
    var config = {
      responseType: 'blob',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
      },
    };

    const send = await this.$axios.$post('/v1/pptx/download', taskID, config)
      .then((res) => {

        const url = window.URL.createObjectURL(new Blob([res]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'Onboarding.pptx');
        document.body.appendChild(link);
        link.click();
        link.remove()

        dispatch("registerDownload", task)
        console.log("registered task", task)
        commit('turnDownloadOff', task)


      })
      .catch((err) => {
        let stringErr = String(err)
        let alert = {
          'alertType': 'API Error',
          'alertID': stringErr.replace('Error: ', ''),
          'alertColor': 'red'
        }
        commit('addTaskAlert', alert);
        commit('turnDownloadOff', task)

      })


  },

  async registerDownload({ commit }, taskID) {
    let task = JSON.stringify({ "taskID": taskID })
    var config = {
      headers: {
        'Content-Type': 'application/json'
      },
    };
    const send = await this.$axios.$post('/v1/pptx/registerDownload', task, config)
  },

  async getSections({ commit }) {
    const res = await this.$axios.$get("/v1/pptx/sections")
      .then((res) => {
        commit("updateList", res.data);
      });
  },

  async getDownloads({ commit, rootState }) {
    console.log(rootState.auth.userID)
    let payload = JSON.stringify({ "user_id": rootState.auth.userID })
    var config = {
      headers: {
        'Content-Type': 'application/json'
      },
    };
    const res = await this.$axios.$post('/v1/pptx/getDownloads', payload, config)
      .then((res) => {

        commit('clearTaskList')
        res.forEach(elem => {
          let options = {
            hour: 'numeric',
            minute: 'numeric',
            year: 'numeric',
            month: 'numeric',
            day: 'numeric'
          }
          let payload = {
            'taskID': elem.taskID,
            'status': elem.status,
            'sections': elem.sections,
            'created': new Date(elem.date_started).toLocaleDateString("en-GB", options),
            'downloading': false
          }
          commit('updateTaskList', payload)
          commit('updateLocalStorage')


        })

      })

  },


}
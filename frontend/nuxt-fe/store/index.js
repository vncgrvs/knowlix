export const state = () => ({
  list: [],
  userChoice: [],
  downloads: 0,
  isFetchingPptx: false,
  isDownloads: false,
  currentRoute: null,
  tasksAlerts: [],
  taskList: [],


})

export const mutations = {
  initialiseStore(state) {

    if (localStorage.getItem('taskList')) {
      state.taskList = JSON.parse(localStorage.getItem('taskList'))
    }

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

    state.tasksAlerts.push(payload)
    // this._vm.$set(state.tasksAlerts, state.tasksAlerts.length, payload)
  },
  updateTask(state, payload) {
    let status = payload.status
    let index = payload.index

    if (status == "SUCCESS") {
      state.taskList[index].status = "done"
    }
    else if (status == "FAILURE") {
      state.taskList[index].status = "failed"
    }
    else if (status == "RETRY") {
      state.taskList[index].status = "retry"
    }
  },
  deleteTaskAlert(state, payload) {
    state.tasksAlerts.splice(payload, 1);
  },
  clearAlertList(state) {
    this.state.tasksAlerts = []
  },
  updateLocalStorage(state) {
    let taskList = state.taskList
    localStorage.setItem('taskList', JSON.stringify(taskList))
  },
  addTask(state, payload) {
    var date = new Date()

    var container = {
      'taskID': payload.taskID,
      'sections': payload.sections,
      'status': 'started',
      'created': date.toLocaleDateString('en-GB', {
        timeZone: 'Europe/Brussels',
        hour: 'numeric',
        minute: 'numeric',
        hour12: false
      })
    };


    state.taskList.push(container);

  },


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
  updateTask({ commit }, payload) {
    commit('updateTask', payload)
    commit('updateLocalStorage');
  },
  deleteListItem({ commit }, payload) {
    commit('deleteListItem', payload);
  },

  clearAlertList({ commit }) {
    commit('clearAlertList');

  },
  async sendTask({ commit }) {

    let onBoardingDeck = JSON.stringify({ "sections": this.state.userChoice })
    var config = {
      headers: {
        'Content-Type': 'application/json',
      },

    };

    const send = await this.$axios.$post('/v1/pptxjob', onBoardingDeck, config)
      .then((res) => {
        

        if (res.status == "success") {
          let alert = { 'alertType': 'jobTriggered', 'alertID': res.taskID }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);

          commit('addTask', res)
          commit('updateLocalStorage');
        }
        else if (res.status == "no_sections") {
          let alert = { 'alertType': 'noSections', 'alertID': "Please select sections" }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }
        else if(res.status == "pptx_exists"){
          let alert = { 'alertType': 'pptxExists', 'alertID': "Looks the requested deck already exists under Downloads" }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }



      });


  },

  async downloadPresentation({ commit }, task) {
    let taskID = JSON.stringify({ "taskID": task })
    commit('changeDownloadCount');
    var config = {
      responseType: 'blob',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
      },
    };

    const send = await this.$axios.$post('/v1/download', taskID, config)
      .then((res) => {

        const url = window.URL.createObjectURL(new Blob([res]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'Onboarding.pptx'); //or any other extension
        document.body.appendChild(link);
        link.click();


      })

  }
}
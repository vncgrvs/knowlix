export const state = () => ({
  list: [],
  userChoice: [],
  downloads: 0,
  isFetchingPptx: false,
  isDownloads: false,
  currentRoute: null,
  taskAlerts: [],
  taskList: [],


})

export const mutations = {
  
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
  deleteTaskAlert(state, payload) {
    state.taskAlerts.splice(payload, 1);
  },
  clearAlertList(state) {
    this.state.taskAlerts = []
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

  deleteListItem({ commit }, payload) {
    commit('deleteListItem', payload);
  },

  clearAlertList({ commit }) {
    commit('clearAlertList');

  },

  // API Calls //
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

        }
        else if (res.status == "no_sections") {
          let alert = { 'alertType': 'noSections', 'alertID': "Please select sections" }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }
        else if (res.status == "pptx_exists") {
          let alert = { 'alertType': 'pptxExists', 'alertID': "Looks the requested deck already exists under Downloads" }
          commit('changeDownloadStatus');
          commit('addTaskAlert', alert);
        }



      });


  },

  async downloadPresentation({ commit, dispatch }, task) {
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
        link.setAttribute('download', 'Onboarding.pptx');
        document.body.appendChild(link);
        link.click();
        link.remove()

        dispatch("registerDownload", task)

      })

  },

  async registerDownload({ commit }, taskID) {
    let task = JSON.stringify({ "taskID": taskID })
    var config = {
      headers: {
        'Content-Type': 'application/json'
      },
    };
    const send = await this.$axios.$post('/v1/registerDownload', task, config)
  },

  async getSections({ commit }) {
    const res = await this.$axios.$get("/v1/sections")
      .then((res) => {
        commit("updateList", res.data);
      });
  },

  async getDownloads({ commit }) {
    const res = await this.$axios.$get('/v1/getDownloads')
      .then((res) => {
        console.log('API Response Downloads: ', res)
        res.forEach(elem => {

          payload = {
            'taskID': elem.taskID,
            'status': elem.status,
            'created': new Date(elem.date_started).toLocaleDateString("en-GB")
          }
          commit('updateTaskList', payload)


        })

      })

  }
}
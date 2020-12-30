
import qs from 'qs';

export const AUTH_MUTATIONS = {
    SET_USER: 'SET_USER',
    SET_PAYLOAD: 'SET_PAYLOAD',
    LOGOUT: 'LOGOUT',
}


export const state = () => ({
    access_token: null, // JWT access token
    id: null, // user id
    user: null,
    loggedIn: null
})

export const mutations = {

    [AUTH_MUTATIONS.SET_USER](state, { id, username }) {
        state.id = id
        state.user = username
    },

    // store new or updated token fields in the state
    [AUTH_MUTATIONS.SET_PAYLOAD](state, { access_token }) {
        state.access_token = access_token
    },

    // clear our the state, essentially logging out the user
    [AUTH_MUTATIONS.LOGOUT](state) {
        state.id = null
        state.user = null
        state.loggedIn = null
        state.access_token = null

    },
}

export const actions = {

    async login({ commit, dispatch }, { username, password }) {
        // make an API call to login the user with an email address and password
        let data = qs.stringify({
            username: username,
            password: password,
        });


        const req = await this.$axios
            .post(
                '/v1/token',
                data
            )

            .then(({ data, config }) => {

                const accessToken = data.access_token
                this.$axios.setToken(accessToken, 'Bearer')

                commit(AUTH_MUTATIONS.SET_PAYLOAD, data)

            })

            .catch((err) => {

                let stringErr = String(err)
                let alert = {
                    'alertType': 'API Error',
                    'alertID': stringErr.replace('Error: ', ''),
                    'alertColor': 'red'
                }
                commit('addTaskAlert', alert);

            })





        // commit the user and tokens to the state
        // commit(AUTH_MUTATIONS.SET_USER, user)

    },

    async getUserInfo({ commit, dispatch }, { }) {



    }
}
import qs from 'qs';

export const AUTH_MUTATIONS = {
    SET_USER: 'SET_USER',
    SET_PAYLOAD: 'SET_PAYLOAD',
    LOGOUT: 'LOGOUT',
}


export const state = () => ({
    access_token: null, // JWT access token
    refresh_token: null, // JWT refresh token
    id: null, // user id
    email_address: null,
})

export const mutations = {

    [AUTH_MUTATIONS.SET_USER] (state, { id, email_address }) {
        state.id = id
        state.email_address = email_address
      },
    
      // store new or updated token fields in the state
      [AUTH_MUTATIONS.SET_PAYLOAD] (state, { access_token, refresh_token = null }) {
        state.access_token = access_token
    
        // refresh token is optional, only set it if present
        if (refresh_token) {
          state.refresh_token = refresh_token
        }
      },
    
      // clear our the state, essentially logging out the user
      [AUTH_MUTATIONS.LOGOUT] (state) {
        state.id = null
        state.email_address = null
        state.access_token = null
        state.refresh_token = null
      },
}

export const actions = {

    async login ({ commit, dispatch }, { username, password }) {
        // make an API call to login the user with an email address and password
        let data = qs.stringify({
            username: username,
            password: password,
          });
        const req = await this.$axios.post(
          '/v1/token', 
          data
        )
        let payload = req.data
        console.log(token)
        // commit the user and tokens to the state
        // commit(AUTH_MUTATIONS.SET_USER, user)
        commit(AUTH_MUTATIONS.SET_PAYLOAD, payload)
      },
}
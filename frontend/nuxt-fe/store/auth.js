import qs from "qs";
import jwt from 'jsonwebtoken';


export const AUTH_MUTATIONS = {
    SET_USER: 'SET_USER',
    SET_PAYLOAD: 'SET_PAYLOAD',
    LOGOUT: 'LOGOUT',
}


export const state = () => ({
    access_token: null, // JWT access token
    userID: null, // user id
    user: null,
    loggedIn: false,
    tokenExpires: null
})


  
export const mutations = {

    [AUTH_MUTATIONS.SET_USER](state, { id, username }) {
        state.id = id
        state.user = username
    },

    // store new or updated token fields in the state
    [AUTH_MUTATIONS.SET_PAYLOAD](state, { access_token, username, userid, exp }) {
        state.access_token = access_token
        state.userID = userid
        state.user = username
        state.loggedIn = true
        state.tokenExpires = exp
    },

    // clear our the state, essentially logging out the user
    [AUTH_MUTATIONS.LOGOUT](state) {
        state.id = ''
        state.user = ''
        state.loggedIn = false
        state.access_token = ''
        state.tokenExpires = ''
        state.userID = ''

        
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
                // this.$axios.setToken(accessToken, 'Bearer')

                let decodedToken = jwt.decode(accessToken)

                let payload = {
                    "access_token": accessToken,
                    "username": decodedToken.first_name,
                    "userid": decodedToken.user_id,
                    "exp": decodedToken.exp
                }

                commit(AUTH_MUTATIONS.SET_PAYLOAD, payload)
                this.$router.push('/')

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

    

     logUserOut({ commit, state }) {
        console.log("logout triggered...")
        commit(AUTH_MUTATIONS.LOGOUT)
        
    },

    async refreshToken({commit, state}){
        
        const {refresh_token} = jwt.decode(state.access_token)

        const req = await this.$axios
            .post(
                '/v1/refreshToken'
            )

            .then(({ data })=>{

                const accessToken = data.access_token
                // this.$axios.setToken(accessToken, 'Bearer')

                let decodedToken = jwt.decode(accessToken)

                let payload = {
                    "access_token": accessToken,
                    "username": decodedToken.first_name,
                    "userid": decodedToken.user_id,
                    "exp": decodedToken.exp
                }

                commit(AUTH_MUTATIONS.SET_PAYLOAD, payload)

            })

    }


}
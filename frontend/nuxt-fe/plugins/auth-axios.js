import jwt from 'jsonwebtoken';

export default function ({ store, app: { $axios }, redirect }) {

  $axios.onError((error) => {
    return new Promise(async (resolve, reject) => {
      const statusCode = error.response ? error.response.status : -1

      const timeNow = Date.now() / 1000 // in seconds - js default : mseconds
      let count = 0
      let loggedIn = store.state.auth.loggedIn

      

      if ((statusCode === 401 || statusCode === 422) && loggedIn) {
        const tokenExpiryDate = store.state.auth.tokenExpires
        let decodedAccessToken = jwt.decode(store.state.auth.access_token)
        let refreshToken = decodedAccessToken.refresh_token

        // sanity check if token expiry is cause
        if ((timeNow > tokenExpiryDate) && refreshToken) {

          if (error.config.hasOwnProperty('retryAttempts') || count > 1) {
            // immediately logout if already attempted refresh
            await store.dispatch('auth/logout')

            // redirect the user home

          }
          else {
            const config = { retryAttempts: 1, ...error.config }
            count++

            try {

              await store.dispatch('auth/refreshToken')
              return resolve($axios(config))

            } catch (error) {

              await store.dispatch('auth/logout')
              console.log(error)

            }

          }


        }




      }
      

      // ignore all other errors, let component or other error handlers handle them
      return reject(error)
    })
  })


}
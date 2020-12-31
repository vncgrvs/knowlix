export default function ({ store, app: { $axios }, redirect }) {

  $axios.onError((error) => {
    return new Promise(async (resolve, reject) => {
      const statusCode = error.response ? error.response.status : -1
      const tokenExpiryDate = store.auth.tokenExpires
      const timeNow = Date.now() / 1000 // in seconds - js default : mseconds

      if ((statusCode === 401 || statusCode === 422) ) {

        // sanity check if token expiry is cause
        if (timeNow > tokenExpiryDate) {
          
        }

        if (error.config.hasOwnProperty('retryAttempts')) {
          // immediately logout if already attempted refresh
          await store.dispatch('auth/logout')
          
          // redirect the user home
          return redirect('/login')
        }


      }

      // ignore all other errors, let component or other error handlers handle them
      return reject(error)
    })
  })


}
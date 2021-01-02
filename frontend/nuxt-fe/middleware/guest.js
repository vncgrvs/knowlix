export default function ({ store, redirect }) {
    if (store.state.auth.loggedIn) {
      console.log("guest middleware")
      return redirect('/')
    }
  }
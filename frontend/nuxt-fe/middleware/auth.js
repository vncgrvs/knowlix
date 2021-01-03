export default function ({ store, redirect }) {
    
    if (!store.state.auth.loggedIn) {
      console.log("hit auth")
      return redirect('/login')
    }
  }
export default function ({ store, redirect }) {
  ssr: false
    
    if (!store.state.auth.loggedIn) {
      console.log("AUTH middleware",store.state.auth.loggedIn )
      return redirect('/login')
    }
  }
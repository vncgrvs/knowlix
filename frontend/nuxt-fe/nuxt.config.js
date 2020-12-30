

export default {
  target: 'server',
  
  // Global page headers (https://go.nuxtjs.dev/config-head)
  head: {
    title: 'knowlix',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: 'https://www.leanix.net/hubfs/LeanIX_favi.png' },
      {
        rel: 'stylesheet',
        href: 'http://fonts.cdnfonts.com/css/axiforma'
      },
      {
        rel: 'stylesheet',
        href: 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'
      },
      // {
      //   rel: 'stylesheet',
      //   href: 'https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css'
      // }
      
    ], 
    script:[
      {
        src: "https://code.jquery.com/jquery-3.4.1.min.js",
        type: "text/javascript"
      },
      {
        
        src:"https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js",
        type:'text/javascript'
      },
      
    ]

  },
  

  

  // Global CSS (https://go.nuxtjs.dev/config-css)
  css: [
  ],

  // Plugins to run before rendering page (https://go.nuxtjs.dev/config-plugins)
  plugins: [
    { src: "~/plugins/vuelidate.js", mode: "client" },
    
    
  ],

  // Auto import components (https://go.nuxtjs.dev/config-components)
  components: true,

  // Modules for dev and build (recommended) (https://go.nuxtjs.dev/config-modules)
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
    '@nuxtjs/axios',
    '@nuxtjs/tailwindcss',
    '@nuxtjs/auth-next'
    
    
  ],

  // Modules (https://go.nuxtjs.dev/config-modules)
  modules: [
    // '@nuxtjs/axios',
    // '@nuxtjs/auth-next'
  ],

  auth: {
    strategies: {
      localRefresh: {
        scheme: 'refresh',
        token: {
          property: 'access_token',
          maxAge: 60 * 30 ,
          // type: 'Bearer'
        },
        refreshToken: {
          property: 'refresh_token',
          data: true,
          tokenRequired: true ,
          maxAge: 60 * 30 
        },
        user: false,
        endpoints: {
          login: { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, url: '/v1/token', method: 'post' },
          user: { url: '/v1/me', method: 'get' },
          logout: false,
          refresh: { url: '/v1/refreshToken', method: 'post' },
          
        },
        // autoLogout: false
      }
    }
    
  },

  axios: {
    baseURL: 'http://localhost',
    // browserBaseURL: 'http://localhost/8000'
    
  },
  

 



  

  // Build Configuration (https://go.nuxtjs.dev/config-build)
  build: {
    
    
  }
}

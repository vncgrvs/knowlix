module.exports = {
  purge: [
    './components/**/*.{vue,js}',
     './layouts/**/*.vue',
     './pages/**/*.vue',
     './plugins/**/*.{js,ts}',
     './nuxt.config.{js,ts}',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    borderColor: theme => ({
      ...theme('colors'),
      'lix-main': '#166BFF',
      'lix-second': '#222F4B',
      'lix-third': '#4D5C7D'
    }),

    backgroundColor: theme => ({
      ...theme('colors'),
      'lix-main': '#166BFF',
      'lix-second': '#222F4B',
      'lix-third': '#4D5C7D'

    }),

    textColor: theme =>({
      ...theme('colors'),
      'lix': '#166BFF',
      'lix-second': '#222F4B'
      
    }),

    extend: {
      fontFamily: {
        'lix': ['Axiforma']
      }
    }
  },
  variants: {
    
  },
  plugins: [],
}

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  future: {
    // removeDeprecatedGapUtilities: true,
    // purgeLayersByDefault: true,
  },
  purge: [],
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
  variants: {},
  plugins: [],
}

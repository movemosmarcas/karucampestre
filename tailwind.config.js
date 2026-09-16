/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./**/*.html"],
  theme: {
    extend: {
        colors: {
            'karu-verde': '#1F3C23',
            'karu-marfil': '#F2D7B7',
            'karu-arena': '#B5946A',
            'karu-piedra': '#787F65',
            'karu-claro': '#F0E4DB'
        },
        fontFamily: {
            'serif': ['"Playfair Display"', 'serif'],
            'sans': ['"Open Sans"', 'sans-serif'],
        }
    },
  },
  plugins: [],
}

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'primary': '#FF6B1A',
        'accent': '#D57A18',
        'secondary': '#3F8CFF',
        'highlight': '#AE7FFF',
        'bg': '#111112',
        'surface': '#1E1E1E',
        'surface-contrast': '#171717',
        'text': {
          'primary': '#F2F2F2',
          'secondary': '#A0A0A0'
        }
      },
      fontFamily: {
        sans: ['Aeonik', 'Inter', 'Open Sans', 'sans-serif'],
        heading: ['Aeonik', 'Poppins', 'Inter', 'sans-serif'],
      },
      boxShadow: {
        'btn': '0 10px 25px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.2) inset, 0 -3px 0px rgba(0, 0, 0, 0.1) inset',
        'btn-hover': '0 15px 35px rgba(255, 103, 0, 0.6), 0 1px 0px rgba(255, 255, 255, 0.4) inset, 0 -4px 0px rgba(0, 0, 0, 0.1) inset',
      },
      // Corrected the 'pulse' keyframe definition
     keyframes: {
        // This pulse is new - it animates the shadow and scale
        pulse: {
          '0%': { 
            transform: 'scale(1)',
            boxShadow: '0 0 0 0 rgba(255, 102, 0, 0.7)'
          },
          '70%': { 
            transform: 'scale(1.05)',
            boxShadow: '0 0 0 20px rgba(255, 102, 0, 0)'
           },
          '100%': {
            transform: 'scale(1)',
            boxShadow: '0 0 0 0 rgba(255, 102, 0, 0)'
          }
        },
        'pulse-badge': { /* ... */ },
        shimmer: { /* ... */ },
      },
      animation: {
        'pulse': 'pulse 1.5s infinite', // Updated animation definition
        'pulse-badge': 'pulse-badge 3s infinite cubic-bezier(0.4, 0, 0.6, 1)',
        'shimmer': 'shimmer 2.5s infinite linear',
      }
    },
  },
  plugins: [
    function ({ matchUtilities, theme }) {
      matchUtilities(
        {
          'text-shadow': (value) => ({
            textShadow: value,
          }),
        },
        { values: theme('textShadow') }
      )
    },
  ],
}
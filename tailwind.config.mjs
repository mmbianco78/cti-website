/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'primary': '#FF6B1A',
        'accent': '#D57A18', // In the reference file, this is #FF6600, our #FF6B1A is very close.
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
        sans: ['Inter', 'Open Sans', 'sans-serif'],
        heading: ['Poppins', 'Inter', 'sans-serif'],
      },
      // NEW STYLES ADDED BELOW
      boxShadow: {
        // 3D button style from .btn 
        'btn': '0 10px 25px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.2) inset, 0 -3px 0px rgba(0, 0, 0, 0.1) inset',
        // Hover state from .btn:hover 
        'btn-hover': '0 15px 35px rgba(255, 103, 0, 0.6), 0 1px 0px rgba(255, 255, 255, 0.4) inset, 0 -4px 0px rgba(0, 0, 0, 0.1) inset',
      },
      keyframes: {
        // Pulse animation from .pulse-btn 
        pulse: {
          '0%, 100%': { 
            transform: 'translateY(0)',
            boxShadow: '0 10px 25px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset'
          },
          '50%': { 
            transform: 'translateY(-3px)',
            boxShadow: '0 15px 35px rgba(255, 103, 0, 0.7), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset'
           },
        }
      },
      animation: {
        'pulse': 'pulse 2.5s infinite',
      }
    },
  },
  plugins: [],
}
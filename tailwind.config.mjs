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
        'surface': {
          'anchor': '#3E424B',
          'lava': '#808588',
          '700': '#2B2B2B', // A new, lighter dark gray for accents
          '800': '#1E1E1E', // This was your old 'surface' color
          '900': '#111112', // This was your old 'bg' color (our darkest)
          DEFAULT: '#1E1E1E'
        },
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
        'btn-active': '0 8px 15px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -2px 0px rgba(0, 0, 0, 0.1) inset',
        'card': '0 10px 30px rgba(0, 0, 0, 0.4)',
        'card-hover': '0 15px 30px rgba(0, 0, 0, 0.4)',
        'testimonial': '0 10px 30px rgba(0, 0, 0, 0.4)',
      },
      // Corrected the 'pulse' keyframe definition
     keyframes: {
        // Button pulse animation from old site
        pulse: {
          '0%': {
            boxShadow: '0 10px 25px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset',
            transform: 'translateY(0)'
          },
          '50%': {
            boxShadow: '0 15px 35px rgba(255, 103, 0, 0.7), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset',
            transform: 'translateY(-2px)'
          },
          '100%': {
            boxShadow: '0 10px 25px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset',
            transform: 'translateY(0)'
          }
        },
        'pulse-badge': {
          '0%': {
            transform: 'scale(0.8)',
            opacity: '0.6'
          },
          '50%': {
            transform: 'scale(1.2)',
            opacity: '0.4'
          },
          '100%': {
            transform: 'scale(0.8)',
            opacity: '0.6'
          }
        },
        shimmer: {
          '0%': { transform: 'translateX(-100%)' },
          '100%': { transform: 'translateX(100%)' }
        },
      },
      animation: {
        'pulse': 'pulse 2.5s infinite',
        'pulse-badge': 'pulse-badge 3s infinite cubic-bezier(0.4, 0, 0.6, 1)',
        'shimmer': 'shimmer 2.5s infinite linear',
      },
      backgroundImage: {
        'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        'gradient-underline': 'linear-gradient(to right, transparent, #FF6B1A, transparent)',
      },
      textShadow: {
        'hero': '0 3px 6px rgba(0, 0, 0, 0.7)',
        'strong': '0 2px 4px rgba(0, 0, 0, 0.5)',
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
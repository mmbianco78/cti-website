/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: { /* ... */ },
      fontFamily: { /* ... */ },
      boxShadow: { /* ... */ },
      textShadow: {
        'sm': '0 1px 2px rgba(0, 0, 0, 0.35)',
        'glow': '0 0 8px rgba(255, 255, 255, 0.5)', // New glow effect for animation
      },
      keyframes: {
        // Updated pulse keyframes
        pulse: {
          '0%, 100%': { 
            transform: 'translateY(0)',
            boxShadow: '0 10px 25px rgba(255, 103, 0, 0.4), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset',
            textShadow: '0 1px 2px rgba(0, 0, 0, 0.35)', // Resting text shadow
          },
          '50%': { 
            transform: 'translateY(-3px)',
            boxShadow: '0 15px 35px rgba(255, 103, 0, 0.7), 0 1px 0px rgba(255, 255, 255, 0.3) inset, 0 -4px 0px rgba(0, 0, 0, 0.15) inset',
            textShadow: '0 0 8px rgba(255, 255, 255, 0.5)', // Glowing text shadow at peak
           },
        },
        'pulse-badge': { /* ... */ },
        shimmer: { /* ... */ },
      },
      animation: {
        'pulse': 'pulse 1.5s infinite',
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
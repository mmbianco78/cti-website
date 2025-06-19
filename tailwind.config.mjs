/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#FF6B1A',
        accent: '#D57A18',
        secondary: '#3F8CFF',
        highlight: '#AE7FFF',
        bg: '#111112',
        surface: '#1E1E1E',
        'text-primary': '#F2F2F2',
        'text-secondary': '#A0A0A0',
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        heading: ['Poppins', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
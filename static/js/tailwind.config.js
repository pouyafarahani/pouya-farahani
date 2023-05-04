const defaultTheme = require("tailwindcss/defaultTheme");

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,html}", "./blog/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Vazirmatn", ...defaultTheme.fontFamily.sans],
        dosis: ["Dosis", ...defaultTheme.fontFamily.sans],
        foldit: ["Foldit", ...defaultTheme.fontFamily.sans],
      },
    },
  },
  plugins: [],
  darkMode: "class",
};

import { createTheme } from "@mui/material/styles";
import { red } from "@mui/material/colors";
import BNazanin from "./assets/fonts/BNazanin.woff";

// A custom theme for this app
const theme = createTheme({
  palette: {
    primary: {
      main: "#556cd6",
    },
    secondary: {
      main: "#19857b",
    },
    error: {
      main: red.A400,
    },
  },
  direction: "rtl",
  typography: {
    fontFamily: ["BNazanin"].join(","),
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: `
        @font-face {
          font-family: 'BNazanin';
          font-style: normal;
          font-display: swap;
          font-weight: 400;
          src: local('BNazanin'), local('BNazanin-Regular'), url(${BNazanin}) format('woff');
          unicodeRange: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF;
        }
      `,
    },
    MuiTypography: {
      defaultProps: {
        variantMapping: {
          h1: "h2",
          h2: "h2",
          h3: "h2",
          h4: "h2",
          h5: "h2",
          h6: "h2",
          subtitle1: "h2",
          subtitle2: "h2",
          body1: "span",
          body2: "span",
        },
      },
    },

    MuiInputBase: {
      styleOverrides: {
        root: {
          backgroundColor: "white",
          height: "36px",
        },
      },
    },
  },
});

export default theme;

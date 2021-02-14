import {
    createMuiTheme,
    responsiveFontSizes
} from '@material-ui/core/styles';

// Create a theme instance.
const theme = createMuiTheme({
    palette: {
        type: "light",
        primary: {
            main: "rgb(175, 118, 123)",
        },
        secondary: {
            main: "#71877B",
        },
        gradientBG: {
            backgroundColor: "#fbfbf8",
            backgroundImage: ({ offset=350 }) => `linear-gradient(${offset}deg, #a0b7aa 0%, #fefbea 83%)`,
        },
        offWhite: "#fefbea",
    },
    layout: {
        contentWidth: 1140,
    },
    typography: {
        stylishFontFamily: "'Sansita Swashed', cursive",
        fancyFontFamily: "'Euphoria Script', cursive",
        fontFamily: [
            'Lato',
            'sans-serif'
        ].join(','),
        body1: {
            fontSize: "1.2rem"
        },
        h4: {
            fontFamily: "'Sansita Swashed', cursive",
        },
    },
});

theme.palette.classes = {
    gridSectionHeader: {
        width: "80%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        [theme.breakpoints.down('md')]: {
            width: "100%",
        },
    },
};

export default responsiveFontSizes(theme);

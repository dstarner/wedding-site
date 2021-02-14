import React from 'react';
import ReactDOM from 'react-dom';
import {
    Container,
    CssBaseline,
    ThemeProvider,
    makeStyles,
} from "@material-ui/core";
import theme from "./theme";
import RSVPForm from './rsvp';

const useStyles = makeStyles(theme => ({
    container: {
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
    },
}));

function App() {
    const classes = useStyles();
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <Container maxWidth="sm" className={classes.container}>
                <RSVPForm />
            </Container>
        </ThemeProvider>
    );
}

ReactDOM.render(<App />, document.getElementById("main"));

import React from 'react';
import ReactDOM from 'react-dom';
import {
    CssBaseline,
    ThemeProvider,
} from "@material-ui/core";
import theme from "./theme";

function App() {
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            <p>Woohooo</p>
        </ThemeProvider>
    );
}

ReactDOM.render(<App />, document.getElementById("main"));

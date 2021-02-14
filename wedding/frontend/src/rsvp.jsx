import React, { useState } from "react";
import {
    makeStyles,
    Button,
    FormGroup,
    Paper,
    Step,
    Stepper,
    StepContent,
    StepLabel,
    TextField,
    Typography,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    root: {
        width: '100%',
    },
    button: {
        marginTop: theme.spacing(1),
        marginRight: theme.spacing(1),
    },
    formGroup: {
        marginTop: theme.spacing(1),
    },
    actionsContainer: {
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
    },
    resetContainer: {
        padding: theme.spacing(3),
    },
}));



function RSVPForm() {
    const classes = useStyles();
    const [activeStep, setActiveStep] = useState(0);
    const handleNext = () => { setActiveStep((prevActiveStep) => prevActiveStep + 1); };
    const handleBack = () => { setActiveStep((prevActiveStep) => prevActiveStep - 1); };
    const handleReset = () => { setActiveStep(0); };

    const [guestID, setGuestID] = useState("");


    const steps = [
        {
            title: "Guest ID",
            content: () => {
                return (
                    <>
                        <Typography >
                            To begin the RSVP process, please use the Guest ID present on
                            your RSVP, or if you used a QR code, it may already be filled in. If
                            you do not have a guest ID or lost it, please put "<strong>NEW</strong>",
                            without the quotation marks around it.
                        </Typography>
                        <FormGroup className={classes.formGroup}>
                            <TextField
                                placeholder="123" fullWidth
                                value={guestID} onChange={e => setGuestID(e.target.value)}
                                label="Guest ID from Invite"
                            />
                        </FormGroup>
                    </>
                );
            },
            // TODO: add a check against the backend server
            canContinue: () => guestID.length === 5 || guestID.toUpperCase() === "NEW",
        },
        {
            title: "Contact Info",
            content: () => {
                return (
                    "woohoo"
                );
            },
            canContinue: () => { return false; },
        },
        {
            title: "Party Guests",
            content: () => {
                return (
                    "woohoo"
                );
            },
            canContinue: () => { return false; },
        },
        {
            title: "Meals",
            content: () => {
                return (
                    "woohoo"
                );
            },
            canContinue: () => { return false; },
        },
    ];

    return (
        <div className={classes.root}>
            <Stepper activeStep={activeStep} orientation="vertical">
                {steps.map(({ title, content, canContinue }, index) => (
                    <Step key={index}>
                        <StepLabel>{title}</StepLabel>
                        <StepContent>
                            { content() }
                            <div className={classes.actionsContainer}>
                                <div>
                                    <Button
                                        disabled={activeStep === 0}
                                        onClick={handleBack}
                                        className={classes.button}
                                    >
                                        Back
                                    </Button>
                                    <Button
                                        variant="contained"
                                        color="primary"
                                        onClick={handleNext}
                                        className={classes.button}
                                        disabled={!canContinue()}
                                    >
                                        {activeStep === steps.length - 1 ? 'Finish' : 'Next'}
                                    </Button>
                                </div>
                            </div>
                        </StepContent>
                    </Step>
                ))}
            </Stepper>
            {activeStep === steps.length && (
                <Paper square elevation={0} className={classes.resetContainer}>
                    <Typography>All steps completed - you&apos;re finished</Typography>
                    <Button onClick={handleReset} className={classes.button}>
                        Reset
                    </Button>
                </Paper>
            )}
        </div>
    );
}

export default RSVPForm;
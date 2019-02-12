/*Settings of the chat interface*/

//The messages that will be displayed
var messages = [{
    isBot: true,
    message: "Welcome"
}, {
    isBot: true,
    message: "How can I help you?"
}
];

// RGB numbers for the label of the person talking to the bot
const personNameColorR = 0;
const personNameColorG = 0;
const personNameColorB = 255;

// RGB numbers for the label of the bot
const botNameColorR = 255;
const botNameColorG = 0;
const botNameColorB = 0;

//Text properties
const txtSize = 24;
const spaceBetweenLines = 25;
const hPadding = 10; // horizontal padding for message
const vPadding = 10; // vertical padding for messages
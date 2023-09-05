const express = require('express');
const fetch = require('node-fetch');
const session = require('express-session');

const app = express();
const PORT = process.env.PORT || 3000;

// Set up session middleware (you'll need to configure this properly)
app.use(session({
    secret: 'your_session_secret',
    resave: false,
    saveUninitialized: true
}));

const CLIENT_ID = '1148574567644807218';
const CLIENT_SECRET = 'anVgkbw4vnwj_pZOvGp3KBwiQj7i--_R';
const REDIRECT_URI = 'https://psyduckanime.lol';

// Function to get the value of a query parameter from the URL
function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Handle the initial OAuth2 request from your GitHub Pages site
app.get('/auth/discord', (req, res) => {
    // Redirect the user to the Discord authorization page
    res.redirect(`https://discord.com/oauth2/authorize?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=code&scope=identify%20guilds.join`);
});

// Handle the OAuth2 callback
app.get('/callback', async (req, res) => {
    const code = req.query.code;

    // Exchange code for an access token
    const tokenResponse = await fetch('https://discord.com/api/oauth2/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `client_id=${CLIENT_ID}&client_secret=${CLIENT_SECRET}&grant_type=authorization_code&code=${code}&redirect_uri=${REDIRECT_URI}`
    });

    const tokenData = await tokenResponse.json();

    // Fetch user data using the access token
    const userResponse = await fetch('https://discord.com/api/v10/users/@me', {
        method: 'GET',
        headers: {
            Authorization: `Bearer ${tokenData.access_token}`
        }
    });

    const userData = await userResponse.json();

    // Store user data and access token in the session (you'll need to implement session handling)
    req.session.userData = userData;
    req.session.accessToken = tokenData.access_token;

    // Construct the URL for the profile picture
    const profilePictureUrl = `https://cdn.discordapp.com/avatars/${userData.id}/${userData.avatar}.png`;

    // Redirect back to your GitHub Pages site or wherever you want
    res.redirect('https://psyduckanime.lol');
});

// Sample endpoint to retrieve user data
app.get('/getProfileData', (req, res) => {
    // In a real implementation, you would fetch user data from Discord's API
    // For now, return sample data
    const sampleUserData = {
        id: '1234567890',
        avatar: 'abcdef1234567890'
    };
    res.json(sampleUserData);
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

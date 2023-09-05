// Function to get the value of a query parameter from the URL
function getQueryParam(name) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(name);
}

// Check if there's an authorization code in the URL
const authCode = getQueryParam('code');

if (authCode) {
    // Send the authorization code to your server to exchange it for an access token
    // You'll need to implement this part in your server-side code (server.js)

    // Once you have the access token and user data, you can set the profile picture
    fetch('/getProfileData') // Replace with the appropriate server endpoint to fetch user data
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(userData => {
            // Construct the URL for the profile picture
            const profilePictureUrl = `https://cdn.discordapp.com/avatars/${userData.id}/${userData.avatar}.png`;

            // Display the profile picture in the top right corner
            const profilePictureElement = document.getElementById('profilePicture');
            profilePictureElement.src = profilePictureUrl;
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
}

// ...

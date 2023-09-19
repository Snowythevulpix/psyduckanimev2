<script>
  var player = videojs('my-video');
</script>

if (authCode) {
  // Send the authorization code to your server to exchange it for an access token
  // You'll need to implement this part in your server-side code (server.js)

  // Once you have the access token and user data, you can set the profile picture
  fetch('/getProfileData') // Replace with the appropriate server endpoint to fetch user data
      .then(response => response.json())
      .then(userData => {
          // Construct the URL for the profile picture
          const profilePictureUrl = `https://cdn.discordapp.com/avatars/${userData.id}/${userData.avatar}.png`;

          // Display the profile picture in the top right corner
          const profilePictureElement = document.getElementById('profilePicture');
          profilePictureElement.src = profilePictureUrl; // Set the src attribute

          // Optionally, you can set the alt attribute and other styles
          profilePictureElement.alt = userData.username; // Set the alt attribute to the username
          profilePictureElement.style.display = 'block'; // Display the image
      })
      .catch(error => {
          console.error('Error fetching user data:', error);
      });
}
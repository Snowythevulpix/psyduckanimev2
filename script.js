<script>
  var player = videojs('my-video');
</script>

// Function to extract the 'code' query parameter from the URL
function getAuthorizationCode() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get('code');
}

// Check if the 'code' query parameter is present in the URL
const authorizationCode = getAuthorizationCode();

if (authorizationCode) {
  // Send the 'code' to your server using a POST request
  fetch('https://criticalecstaticcamel.vulpix773.repl.co', { // Replace with your server URL
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ code: authorizationCode }),
  })
    .then(response => {
      if (response.ok) {
        // Code successfully sent to the server
        console.log('Authorization code sent to the server.');
      } else {
        // Handle errors
        console.error('Failed to send authorization code to the server.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
} else {
  console.log('No authorization code found in the URL.');
}

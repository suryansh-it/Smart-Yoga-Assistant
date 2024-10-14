$(document).ready(function() {
    const video = document.getElementById('video');
    const feedback = document.getElementById('feedback');
    const startButton = document.getElementById('start-button');
    const endButton = document.getElementById('end-button');

    // Check if elements are found
    if (!startButton || !endButton) {
        console.error("Start or End button not found in the DOM.");
        return; // Exit if buttons are not found
    }

    // Function to start feedback session
    async function startFeedbackSession() {
        feedback.innerHTML = "Starting yoga feedback session...";
        
        try {
            const response = await fetch('/home/start', {
                method: 'POST',
            });
            const data = await response.json();
            feedback.innerHTML = data.message || "Feedback session ended.";
        } catch (error) {
            feedback.innerHTML = "Error starting feedback session: " + error;
        }
    }

    // Function to end feedback session
    async function endFeedbackSession() {
        feedback.innerHTML = "Ending yoga feedback session...";
        
        try {
            const response = await fetch('/end', {
                method: 'POST',
            });
            const data = await response.json();
            feedback.innerHTML = data.message || "Feedback session ended.";
        } catch (error) {
            feedback.innerHTML = "Error ending feedback session: " + error;
        }
    }

    // Function to start the video feed
    async function startVideo() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            video.play();
        } catch (error) {
            console.error("Error accessing the camera: ", error);
        }
    }

    // Start capturing video on button click
    startButton.addEventListener('click', () => {
        startFeedbackSession();
        startVideo();  // Start the video feed
    });

    // End feedback session on button click
    endButton.addEventListener('click', () => {
        endFeedbackSession();
        if (video.srcObject) {
            video.srcObject.getTracks().forEach(track => track.stop()); // Stop video feed
        }
    });
});

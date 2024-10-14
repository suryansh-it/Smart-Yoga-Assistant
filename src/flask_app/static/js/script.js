$(document).ready(function() {
    const video = document.getElementById('video');
    const feedback = document.getElementById('feedback');
    const startButton = document.getElementById('start-button');

    // Function to start feedback session
    async function startFeedbackSession() {
        feedback.innerHTML = "Starting yoga feedback session...";
        
        try {
            const response = await fetch('/start', {
                method: 'POST',
            });
            const data = await response.json();
            feedback.innerHTML = data.message || "Feedback session ended.";
        } catch (error) {
            feedback.innerHTML = "Error starting feedback session: " + error;
        }
    }

    // Start capturing video on button click
    startButton.addEventListener('click', () => {
        startFeedbackSession();
        startVideo();  // Start the video feed
    });
});

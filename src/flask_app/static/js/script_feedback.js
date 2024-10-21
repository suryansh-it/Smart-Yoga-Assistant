$(document).ready(function () {
    // Start feedback session
    $('#start-button').click(function () {  // Corrected button ID
        $.post('/start', function (data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session started: ' + data.message + '</div>');
            $('#video-feed').show(); // Show the video feed
            startVideoStream(); // Start the video stream after starting feedback
            startFeedbackPolling(); // Start polling for feedback
        }).fail(function (jqXHR) {
            $('#feedbackArea').append('<div class="alert alert-danger">Error: ' + jqXHR.responseJSON.error + '</div>');
        });
    });

    // End feedback session
    $('#end-button').click(function () {  // Corrected button ID
        $.post('/end', function (data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session ended: ' + data.message + '</div>');
            $('#video-feed').hide(); // Hide the video feed
            stopFeedbackPolling(); // Stop polling for feedback
        }).fail(function () {
            $('#feedbackArea').append('<div class="alert alert-danger">Error ending session.</div>');
        });
    });

    // Function to start the video stream
    function startVideoStream() {
        $('#video').attr('src', '/video_feed'); // Set the video source to /video_feed
    }

    // Poll the server for real-time textual feedback
    let feedbackInterval;

    function startFeedbackPolling() {
        feedbackInterval = setInterval(function () {
            $.get('/feedback', function (data) {
                $('#liveFeedbackText').text(data.feedback);
            }).fail(function () {
                $('#liveFeedbackText').text("Error retrieving feedback.");
            });
        }, 1000); // Poll every second
    }

    function stopFeedbackPolling() {
        clearInterval(feedbackInterval);
        $('#liveFeedbackText').text("Feedback polling stopped.");
    }

    // Stop video capture on page unload
    $(window).on('beforeunload', function () {
        $.post('/end');  // Stop video capture on page unload
    });

    // Initially hide the video feed
    $('#video-feed').hide();
});

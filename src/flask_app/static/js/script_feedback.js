$(document).ready(function () {
    $('#start-button').click(function () {
        $.post('/start', function (data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session started </div>');
            $('#video').attr('src', '/video_feed'); // Set the img src to video feed
            startFeedbackPolling(); // Start feedback polling
        }).fail(function (jqXHR) {
            $('#feedbackArea').append('<div class="alert alert-danger">Error: ' + jqXHR.responseJSON.error + '</div>');
        });
    });

    $('#end-button').click(function () {
        $.post('/end', function (data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session ended: ' + data.message + '</div>');
            $('#video').attr('src', ''); // Clear the image source to stop stream
            stopFeedbackPolling(); // Stop polling
        }).fail(function () {
            $('#feedbackArea').append('<div class="alert alert-danger">Error ending session.</div>');
        });
    });

    let feedbackInterval;

    function startFeedbackPolling() {
        feedbackInterval = setInterval(function () {
            $.get('/get_feedback', function (data) {
                console.log("Feedback received:", data);  // Log feedback data for debugging
                $('#liveFeedbackText').text(data.feedback || "Waiting for feedback...");
            }).fail(function () {
                $('#liveFeedbackText').text("Error retrieving feedback.");
            });
        }, 1000);
    }

    function stopFeedbackPolling() {
        clearInterval(feedbackInterval);
        $('#liveFeedbackText').text("Feedback polling stopped.");
    }

    $(window).on('beforeunload', function () {
        $.post('/end');  // End session on page unload
    });
});

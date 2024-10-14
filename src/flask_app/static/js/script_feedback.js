$(document).ready(function() {
    // Start feedback session
    $('#startFeedback').click(function() {
        $.post('/start', function(data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session started: ' + data.message + '</div>');
        }).fail(function() {
            $('#feedbackArea').append('<div class="alert alert-danger">Error starting session.</div>');
        });
    });

    // End feedback session
    $('#endFeedback').click(function() {
        $.post('/end', function(data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session ended: ' + data + '</div>');
        });
    });

    // Poll the server for real-time textual feedback
    setInterval(function() {
        $.get('/feedback', function(data) {
            $('#liveFeedbackText').text(data.feedback);
        });
    }, 1000);  // Adjust the polling interval as necessary
});

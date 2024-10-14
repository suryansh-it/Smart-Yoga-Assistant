$(document).ready(function() {
    $('#startFeedback').click(function() {
        $.post('/home/start', function(data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session started: ' + data.message + '</div>');
        }).fail(function() {
            $('#feedbackArea').append('<div class="alert alert-danger">Error starting session.</div>');
        });
    });

    $('#endFeedback').click(function() {
        $.post('/end', function(data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session ended: ' + data + '</div>');
        });
    });
});

// Function to update feedback area periodically
function updateFeedback(feedback) {
    $('#feedbackArea').append('<div class="alert alert-success">' + feedback + '</div>');
}

// Function to poll for feedback
setInterval(function() {
    $.get('/home/feedback', function(data) {
        if (data.feedback) {
            updateFeedback(data.feedback);
        }
    });
}, 5000); // Adjust the interval as needed

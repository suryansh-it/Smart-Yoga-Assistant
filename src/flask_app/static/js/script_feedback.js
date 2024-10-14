// $(document).ready(function() {
//     // Start feedback session
//     $('#startFeedback').click(function() {
//         $.post('/start', function(data) {
//             $('#feedbackArea').append('<div class="alert alert-info">Session started: ' + data.message + '</div>');
//         }).fail(function() {
//             $('#feedbackArea').append('<div class="alert alert-danger">Error starting session.</div>');
//         });
//     });

//     // End feedback session
//     $('#endFeedback').click(function() {
//         $.post('/end', function(data) {
//             $('#feedbackArea').append('<div class="alert alert-info">Session ended: ' + data.message + '</div>');
//         });
//     });

//     // Poll the server for real-time textual feedback
//     setInterval(function() {
//         $.get('/feedback', function(data) {
//             $('#liveFeedbackText').text(data.feedback);
//         });
//     }, 1000);  // Adjust the polling interval as necessary
// });


$(document).ready(function () {
    // Start feedback session
    $('#startFeedback').click(function () {
        $.post('/start', function (data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session started: ' + data.message + '</div>');
            startFeedbackPolling(); // Start polling for feedback
        }).fail(function () {
            $('#feedbackArea').append('<div class="alert alert-danger">Error starting session.</div>');
        });
    });

    // End feedback session
    $('#endFeedback').click(function () {
        $.post('/end', function (data) {
            $('#feedbackArea').append('<div class="alert alert-info">Session ended: ' + data.message + '</div>');
            stopFeedbackPolling(); // Stop polling for feedback
        }).fail(function () {
            $('#feedbackArea').append('<div class="alert alert-danger">Error ending session.</div>');
        });
    });

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
});

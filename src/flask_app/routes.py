# Contains the Flask routes (API endpoints)


# routes.py
from flask import Blueprint, render_template, request , jsonify , Response
from flask_login import login_required
from ..live_feedback.video_capture import capture_video
import logging
import cv2

main = Blueprint('main', __name__)

cap = cv2.VideoCapture(0)
feedback = "Waiting for feedback..."    

@main.route('/')
def index():
    """Render the index page with the button."""
    return render_template('index.html')

@main.route('/feedback')
@login_required
def feedback_page():
    """Render the feedback page."""
    return render_template('feedback.html')

# def generate_frames():
#     global feedback
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
#         else:
#             feedback = evaluate_pose(frame)
#             cv2.putText(frame, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@main.route('/video_feed')
@login_required
def video_feed():
    """Route to provide video streaming."""
    return Response(capture_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

@main.route('/feedback')
@login_required
def get_feedback():
    """Return the latest textual feedback."""
    return jsonify({"feedback": feedback})

@main.route('/start', methods=['POST'])
@login_required
def start_feedback():
    """Start the feedback session."""
    return jsonify({"message": "Yoga feedback session started"}), 200

@main.route('/end', methods=['POST'])
@login_required
def end_feedback():
    """End the feedback session and release the webcam."""
    cap.release()
    return "Yoga feedback session ended"
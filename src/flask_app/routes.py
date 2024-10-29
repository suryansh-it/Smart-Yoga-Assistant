import cv2
from flask import Blueprint, render_template, Response, jsonify, request,url_for
from flask_login import login_required
from ..live_feedback.video_capture import capture_video
from ..live_feedback.real_time_pose_eval import evaluate_pose
# from src.live_feedback.video_capture import capture_video  # Absolute path for imports
import logging

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Declare capture variable globally
cap = None
is_session_active = False

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/feedback')
@login_required
def feedback_page():
    return render_template('feedback.html')

@main.route('/start', methods=['POST'])
@login_required
def start_feedback():
    global cap, is_session_active
    logging.info("Starting feedback session.")
    try:
        if cap is None:  # Check if cap is not already initialized
            cap = cv2.VideoCapture(0)  # Try to open the default camera

        if not cap.isOpened():
            logging.error("Cannot access the webcam.")
            return jsonify({"error": "Failed to access the webcam."}), 500

        is_session_active = True  # Set the session active after successful camera access
        logging.info("Feedback session started successfully.")
        
        #     # Retrieve initial feedback by calling get_feedback()
        # feedback_response = get_feedback()  # Call the function directly
        # if feedback_response.status_code != 200:
        #     # If get_feedback encountered an issue, stop the session and return the error
        #     end_feedback()
        #     return feedback_response  # Return the error response from get_feedback
        
        # Return initial feedback along with redirection URL
        return jsonify({
            "redirect_url": url_for('main.feedback_page'),
            
        }), 200

    except Exception as e:
        logging.exception("Error during feedback session: %s", str(e))  # Log exception details
        return jsonify({"error": "Failed to start feedback session."}), 500

@main.route('/video_feed')
@login_required
def video_feed():
    global cap
    try:
        if cap is None or not cap.isOpened() or not is_session_active:
            logging.error("Camera is not initialized or session is not active.")
            return jsonify({"error": "Camera is not accessible."}), 500
        return Response(capture_video(cap, is_session_active, use_posenet=True),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        logging.exception("Error in video feed: %s", str(e))  # Log the exception with traceback
        return jsonify({"error": "Video feed failed."}), 500

@main.route('/end', methods=['POST'])
@login_required
def end_feedback():
    global cap, is_session_active
    logging.info("Ending feedback session.")
    is_session_active = False  # Set the session inactive
    if cap is not None:
        cap.release()  # Release the camera
        cap = None  # Reset the cap variable
        logging.info("Camera released successfully.")
    return jsonify({"message": "Yoga feedback session ended."}), 200

@main.route('/get_feedback', methods=['GET'])
@login_required

#captures a frame from the video feed within the get_feedback route and pass it to evaluate_pose

def get_feedback():
    global cap
    if cap is None or not cap.isOpened() or not is_session_active:
        return jsonify({"error": "Camera is not accessible or session is inactive."}), 500

    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        return jsonify({"error": "Failed to capture frame from camera."}), 500

    # Call evaluate_pose to get feedback based on the captured frame
    feedback = evaluate_pose(frame, use_posenet=True)
    return jsonify({"feedback": feedback})

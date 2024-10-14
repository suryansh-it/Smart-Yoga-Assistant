from flask import Blueprint, render_template, Response, jsonify, request
from flask_login import login_required
from ..live_feedback.video_capture import capture_video
import logging

main = Blueprint('main', __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/feedback')
@login_required
def feedback_page():
    return render_template('feedback.html')

@main.route('/video_feed')
@login_required
def video_feed():
    try:
        logging.info("Attempting to start video feed.")
        video_gen = capture_video(use_posenet=True)  # Check if this is a callable
        return Response(video_gen, mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        logging.error("Error in video feed: %s", str(e))
        return jsonify({"error": "Video feed failed"}), 500


@main.route('/start', methods=['POST'])
@login_required
def start_feedback():
    logging.info("Starting feedback session.")
    try:
        # Initialize the video capture and feedback mechanism
        capture_video(use_posenet=True)
        return jsonify({"message": "Yoga feedback session started."}), 200
    except Exception as e:
        logging.error("Error during feedback session: %s", str(e))
        return jsonify({"error": "Failed to start feedback session."}), 500

@main.route('/end', methods=['POST'])
@login_required
def end_feedback():
    logging.info("Ending feedback session.")
    return jsonify({"message": "Yoga feedback session ended."}), 200

@main.route('/feedback', methods=['GET'])
@login_required
def get_feedback():
    # Placeholder for real-time feedback (Modify this as needed for actual feedback implementation)
    feedback = "Posture is correct!"  # This is a placeholder. You can modify this to get live feedback
    return jsonify({"feedback": feedback})

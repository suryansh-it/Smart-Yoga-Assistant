# Contains the Flask routes (API endpoints)


# routes.py
from flask import Blueprint, render_template, request , jsonify
from flask_login import login_required
from ..live_feedback.video_capture import capture_video
import logging

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/feedback')
@login_required
def feedback():
    return render_template('feedback.html')



# Set up logging
logging.basicConfig(level=logging.INFO)

@main.route('/start', methods=['POST'])
def start_feedback():
    logging.info("Start feedback session called.")
    try:
        capture_video(use_posenet=True)
        return jsonify({"message": "Yoga feedback session started"}), 200
    except Exception as e:
        logging.error("Error during feedback session: %s", str(e))
        return jsonify({"error": "Failed to start feedback session"}), 500



@main.route('/end', methods=['POST'])
def end_feedback():
    # global is_session_active
    # is_session_active = False
    # Here you might want to stop the video capture or cleanup resources
    # stop_video_capture()  # Implement this function as necessary
    return "Yoga feedback session ended"

# Contains the Flask routes (API endpoints)


# routes.py
from flask import Blueprint, render_template, request , jsonify
from flask_login import login_required
from ..live_feedback.video_capture import capture_video

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/feedback')
@login_required
def feedback():
    return render_template('feedback.html')

@main.route('/start', methods=['POST'])

def start_feedback():
    global is_session_active
    is_session_active = True
    try:
        capture_video(use_posenet=True)
        return jsonify({"message": "Yoga feedback session started"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route('/end', methods=['POST'])
def end_feedback():
    global is_session_active
    is_session_active = False
    # Here you might want to stop the video capture or cleanup resources
    # stop_video_capture()  # Implement this function as necessary
    return "Yoga feedback session ended"

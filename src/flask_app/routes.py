# Contains the Flask routes (API endpoints)

# routes.py
from flask import Blueprint, render_template, request
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
    capture_video(use_posenet=True)
    return "Yoga feedback session ended"


# Video capture setup with OpenCV for live input

import cv2
from src.live_feedback.real_time_pose_eval import evaluate_pose

def capture_video(use_posenet=True):
    """
    Capture live video from the webcam and perform real-time pose evaluation.
    
    :param use_posenet: Boolean flag to choose between PoseNet and Mediapipe.
    """
    cap = cv2.VideoCapture(0)  # Capture video from the webcam

    if not cap.isOpened():
        print("Error: Cannot access the webcam.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        if not ret:
            break

        # Resize the frame for display
        resized_frame = cv2.resize(frame, (640, 480))
        
        # Perform pose evaluation and get feedback
        feedback = evaluate_pose(resized_frame, use_posenet=use_posenet)
        
        # Display the feedback on the frame
        cv2.putText(resized_frame, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # Show the frame with feedback
        cv2.imshow('Yoga Pose Evaluation', resized_frame)
        
        # Press 'q' to exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break


    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()
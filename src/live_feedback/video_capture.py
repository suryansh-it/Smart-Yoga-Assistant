import cv2
from .real_time_pose_eval import evaluate_pose

def capture_video(cap, is_session_active, use_posenet=True):
    if not is_session_active:
        print("Error: Session is not active.")
        return  # Don't proceed if the session is not active

    if cap is None or not cap.isOpened():
        print("Error: Camera is not initialized or cannot be opened.")
        return

    while cap.isOpened() and is_session_active:
        ret, frame = cap.read()

        if not ret:
            print("Error: Frame not received from the camera.")
            break

        # Resize the frame for display
        resized_frame = cv2.resize(frame, (640, 480))

        # Perform pose evaluation and get feedback
        feedback = evaluate_pose(resized_frame, use_posenet=use_posenet)

        # Display the feedback on the frame
        cv2.putText(resized_frame, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Encode the frame as JPEG
        success, buffer = cv2.imencode('.jpg', resized_frame)
        if not success:
            print("Error: Frame encoding failed.")
            break

        # Convert the buffer to bytes
        frame_bytes = buffer.tobytes()

        # Yield the frame in the required format for streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Ensure the camera is released when done
    if cap is not None:
        cap.release()
        print("Camera released successfully.")

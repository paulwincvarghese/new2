import cv2
import mediapipe as mp
import time
from player import JumpscarePlayer
import os
import numpy as np

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Constants
JUMPSCARE_VIDEO = "jumpscare.mp4"
LOOK_AWAY_TIMEOUT = 2.0 # seconds

# LANDMARKS
L_EYE = [33, 160, 158, 133, 153, 144]
R_EYE = [362, 385, 387, 263, 373, 380]
L_IRIS = [468, 469, 470, 471, 472]
R_IRIS = [473, 474, 475, 476, 477]

def get_center(landmarks, points):
    lp = np.array([(landmarks[p].x, landmarks[p].y) for p in points])
    return np.mean(lp, axis=0)

def is_looking_at_screen(landmarks, results=None):
    # 1. IRIS TRACKING
    l_eye_center = get_center(landmarks, L_EYE)
    r_eye_center = get_center(landmarks, R_EYE)
    l_iris_center = get_center(landmarks, L_IRIS)
    r_iris_center = get_center(landmarks, R_IRIS)
    
    # Distance of iris from eye socket center
    l_dist = np.linalg.norm(l_iris_center - l_eye_center)
    r_dist = np.linalg.norm(r_iris_center - r_eye_center)
    
    # Very sensitive threshold - If iris leaves the center by more than this
    GAZE_THRESHOLD = 0.007 
    
    # Check if looking down (common for phone usage)
    # The Y axis increases downwards
    l_y_diff = l_iris_center[1] - l_eye_center[1]
    r_y_diff = r_iris_center[1] - r_eye_center[1]
    LOOK_DOWN_THRESHOLD = 0.005
    
    # 2. HEAD POSE (Simplified)
    # Use nose position relative to eye centers for Yaw/Pitch
    nose = landmarks[4]
    eye_midpoint = (l_eye_center + r_eye_center) / 2
    
    # Yaw: nose horizontal displacement from eye midpoint
    # Pitch: nose vertical displacement
    # Normalize by eye distance to make it scale-invariant
    eye_dist = np.linalg.norm(l_eye_center - r_eye_center)
    
    yaw = (nose.x - eye_midpoint[0]) / eye_dist
    pitch = (nose.y - eye_midpoint[1]) / eye_dist
    
    # Thresholds for head rotation
    YAW_THRESHOLD = 0.15 # Sensitivity to looking left/right
    PITCH_THRESHOLD = 0.40 # Sensitivity to looking up/down

    is_gaze_centered = l_dist < GAZE_THRESHOLD and r_dist < GAZE_THRESHOLD
    is_not_looking_down = l_y_diff < LOOK_DOWN_THRESHOLD and r_y_diff < LOOK_DOWN_THRESHOLD
    is_head_centered = abs(yaw) < YAW_THRESHOLD and abs(pitch - 0.5) < PITCH_THRESHOLD # Adjust pitch offset

    # Debug info
    debug_str = f"L:{l_dist:.3f} R:{r_dist:.3f} Y:{yaw:.2f} P:{pitch:.2f}"
    
    return is_gaze_centered and is_not_looking_down and is_head_centered, debug_str

def main():
    if not os.path.exists(JUMPSCARE_VIDEO):
        print(f"Error: {JUMPSCARE_VIDEO} not found!")
        return

    cap = cv2.VideoCapture(0)
    player = JumpscarePlayer(JUMPSCARE_VIDEO)
    
    looking_away_start = None
    is_scaring = False

    print("Prank initialized. Gaze & Head Pose tracking active...")

    while cap.isOpened():
        success, image = cap.read()
        if not success: break

        image = cv2.flip(image, 1)
        image_h, image_w, _ = image.shape
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        current_time = time.time()
        looking_at_screen = False
        debug_info = "No Face"

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            looking_at_screen, debug_info = is_looking_at_screen(landmarks)
            
            # Draw trackers for visual confirmation
            for p in L_IRIS + R_IRIS:
                pt = landmarks[p]
                cv2.circle(image, (int(pt.x * image_w), int(pt.y * image_h)), 1, (255, 255, 0), -1)

        if looking_at_screen:
            if is_scaring:
                player.stop()
                is_scaring = False
            looking_away_start = None
        else:
            if not is_scaring:
                if looking_away_start is None:
                    looking_away_start = current_time
                
                elapsed = current_time - looking_away_start
                if elapsed >= LOOK_AWAY_TIMEOUT:
                    print("BOO!")
                    player.start()
                    is_scaring = True

        if is_scaring:
            player.update()

        # Display Status
        status_text = "WATCHING" if looking_at_screen else "LOOKED AWAY"
        color = (0, 255, 0) if looking_at_screen else (0, 0, 255)
        cv2.putText(image, f"Status: {status_text}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        cv2.putText(image, debug_info, (10, 60), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        cv2.imshow('Detection (DEBUG)', image)
        if cv2.waitKey(5) & 0xFF == 27: break

    cap.release()
    player.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

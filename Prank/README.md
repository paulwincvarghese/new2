# Anti-Phone Scrolling Jumpscare Prank 👻

A Python-based prank application that detects when a user looks away from the screen (or down at their phone) and triggers a fullscreen jumpscare video.

## Features

- **Precise Gaze Tracking**: Uses MediaPipe Iris to detect eye movement.
- **Head Pose Estimation**: Detects if the user turns their head away from the screen.
- **Robust Video Playback**: Uses `ffpyplayer` for high-performance video and audio synchronization.
- **Auto-Loop**: The jumpscare video loops indefinitely until the user looks back.
- **Customizable**: Adjustable trigger timeout (default: 2 seconds).

## Setup

1. **Install Dependencies**:
   ```bash
   pip install opencv-python mediapipe ffpyplayer numpy
   ```

2. **Add Jumpscare Video**:
   Download your preferred jumpscare video and save it as `jumpscare.mp4` in the project root.

3. **Run the Prank**:
   ```bash
   python main.py
   ```

## Controls
- **ESC**: Exit the application from the debug window.

## Warning
This is a prank tool. Use responsibly and ensure the volume is set to a safe but effective level!

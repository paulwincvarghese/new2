import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import time

class JumpscarePlayer:
    def __init__(self, video_path):
        self.video_path = video_path
        self.player = None
        self.is_playing = False

    def start(self):
        if self.is_playing:
            return
        
        self.player = MediaPlayer(self.video_path)
        self.is_playing = True
        cv2.namedWindow("JUMPSCARE", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("JUMPSCARE", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    def update(self):
        if not self.is_playing or self.player is None:
            return

        frame, val = self.player.get_frame()
        
        if val == 'eof':
            # Restart video for looping
            self.player.seek(0, relative=False)
            return

        if frame is not None:
            img, t = frame
            # Convert frame to numpy array for OpenCV
            w, h = img.get_size()
            data = img.to_bytearray()[0]
            frame_np = np.frombuffer(data, dtype=np.uint8).reshape(h, w, 3)
            # ffpyplayer uses RGB, OpenCV uses BGR
            frame_bgr = cv2.cvtColor(frame_np, cv2.COLOR_RGB2BGR)
            
            cv2.imshow("JUMPSCARE", frame_bgr)
            cv2.waitKey(1)

    def stop(self):
        if not self.is_playing:
            return
        
        if self.player:
            self.player.close_player()
            self.player = None
        
        self.is_playing = False
        cv2.destroyWindow("JUMPSCARE")

if __name__ == "__main__":
    # Test player
    player = JumpscarePlayer("jumpscare.mp4")
    player.start()
    start_time = time.time()
    while time.time() - start_time < 10: # Play for 10 seconds
        player.update()
    player.stop()

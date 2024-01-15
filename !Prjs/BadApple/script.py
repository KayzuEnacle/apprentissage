import cv2
import numpy as np
import os
import subprocess
import tempfile

ASCII_CHARS = "@%#*+=-:. "

def convert_frame_to_ascii(frame, cols):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray_frame.shape
    aspect_ratio = width / height
    new_width = cols
    new_height = new_width / aspect_ratio
    resized_gray_frame = cv2.resize(gray_frame, (int(new_width), int(new_height)))
    ascii_frame = ""
    for row in resized_gray_frame:
        for pixel in row:
            ascii_frame += ASCII_CHARS[pixel // 32]
        ascii_frame += "\n"
    return ascii_frame

def play_video_in_ascii(video_path, cols):
    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            break
        ascii_frame = convert_frame_to_ascii(frame, cols)
        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt') as f:
            f.write(ascii_frame)
        os.system(f'notepad {f.name}')
        os.unlink(f.name)
        cv2.waitKey(int(1000 / 15))
    video.release()
    cv2.destroyAllWindows()

play_video_in_ascii('Prjs/BadApple/badapple.mp4', 80)
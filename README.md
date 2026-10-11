# Computer Vision Assignment 1

This project reads a video frame by frame using OpenCV, draws a rectangle and a frame counter on every frame, and saves the result as a new video.

## What it does
Reads `input.mp4` with `cv2.VideoCapture`
Draws a green box in the center of each frame with `cv2.rectangle`
Writes the frame number on top of the box with `cv2.putText`
Saves the processed video as `output.mp4` with `cv2.VideoWriter`

## Files
`main.py` - the script
`input.mp4` - original video
`output.mp4` - processed video
`requirements.txt` - required packages



import cv2
import numpy as np
import pyautogui
from threading import Event # To Stop the recording safely.

def record_screen(output_path, stop_event: Event):
    print("Screen recording started...")
    screen_size = pyautogui.size()
    #Gets the current screen resolution (width and height in pixels) from PyAutoGUI. This is necessary to set the video frame size.
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    #Creates a four-character code (fourcc) representing the video codec to use.
    out = cv2.VideoWriter(output_path, fourcc, 1.0, screen_size)
    #Initializes the OpenCV VideoWriter object

    try:
        while not stop_event.is_set():
            #Starts a loop that continues until the stop_event is set.This is a thread-safe way to control when to stop.
            img = pyautogui.screenshot()
            #Takes a screenshot of the entire screen using PyAutoGUI. The result is a PIL Image object.
            frame = np.array(img)
            #Converts the screenshot (PIL Image) into a NumPy array, which OpenCV can work with.
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            #Converts the color format from RGB to BGR.PyAutoGUI screenshots use RGB, but OpenCV uses BGR by default, so this conversion is necessary to show correct colors.
            out.write(frame)
            #Writes the current frame (image) to the video file.
    except Exception as e:
        print(f"❌ Error during recording: {e}")
        #If any error occurs during the recording process (like screen capture failure), it will be caught here.
    finally:
        out.release()
        #Releases the VideoWriter resource to properly close the video file and save it correctly.
        print("🛑 Screen recording stopped.")

#Summary For the above File
'''
This function captures your screen continuously in a loop, writes the screenshots as frames to a video file, and stops cleanly when told to via 
the stop_event. It handles color conversion and video encoding using OpenCV and uses a thread-safe event to signal stopping the recording.
'''
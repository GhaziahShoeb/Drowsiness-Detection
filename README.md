# Drowsiness-Detection
this project helps in increasing the safety on road by detecting drowsiness .Drowsiness Detection is the detection of people to check whether the person is feeling sleepy while performing some task.

Project Description

This Python project implements a real-time Drowsiness Detection system using computer vision techniques. It monitors a user's eyes via a webcam feed and triggers a visual and audible alert if the eyes remain closed for a specific duration, indicating potential drowsiness.

The system uses the Eye Aspect Ratio (EAR) method, which calculates the ratio between the height and width of the eye to determine if the eye is open or closed.

Features

Real-time Monitoring: Processes live video feed from the webcam.

Facial Landmark Detection: Utilizes Dlib's 68-point model to accurately locate the eyes.

Eye Aspect Ratio (EAR) Calculation: Uses Euclidean distance to quantify eye openness.

Visual Alert: Displays "DROWSINESS DETECTED" and "Alert!!!! WAKE UP DUDE" messages on the screen.

Audible Alert: Triggers a text-to-speech alarm using pyttsx3 when drowsiness is detected.

Prerequisites

Before running the script, ensure you have Python installed (Python 3.6+ is recommended).

You will need the following libraries:

opencv-python

dlib (Note: Dlib can be tricky to install and often requires CMake and Boost. If installation fails, search for system-specific installation guides.)

scipy

pyttsx3

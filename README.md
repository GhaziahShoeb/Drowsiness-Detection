# Drowsiness Detection System (OpenCV + MediaPipe + Tkinter UI)

This project implements a **real-time drowsiness detection system** using:

* **MediaPipe Face Mesh** for facial landmark detection
* **OpenCV** for webcam capture and drawing
* **Eye Aspect Ratio (EAR)** for measuring eye closure
* **pyttsx3** for offline voice alerts
* **Tkinter** for a simple and interactive graphical interface

The system is lightweight, offline, and works on any standard webcam. It raises an audio alert when signs of drowsiness are detected.

---

## 🚀 Features

* Real-time webcam feed with eye-tracking
* Computes EAR (Eye Aspect Ratio) to detect eye closure
* Voice alert when drowsiness is detected
* Adjustable sensitivity through UI controls:

  * EAR threshold slider
  * Frame count required to trigger alert
* Start / Stop buttons for easy control
* Clean UI built using Tkinter
* Fully offline — no internet required
* No `.dat` file needed (MediaPipe removes the need for dlib models)

---

## 🖼️ User Interface

The Tkinter UI provides:

* Live video preview
* Real-time EAR value display
* Counter for consecutive closed-eye frames
* Customizable EAR threshold
* Adjustable “frames before alert” value
* Status indicator (Idle / Running / Stopped)

---

## 📦 Installation

Install the required Python packages:

```
pip install opencv-python mediapipe pyttsx3 pillow numpy
```

---

## ▶️ Usage

Run the application:

```
python drowsiness_gui.py
```

### UI Controls:

* **Start:** Starts webcam + detection
* **Stop:** Stops detection
* **EAR threshold:** Lower values = stricter detection
* **Frames for alert:** Number of consecutive frames required to trigger alarm
* **Quit:** Close the application

---

## 🔧 How It Works

### 1. **Face Landmark Detection**

MediaPipe Face Mesh provides 468 facial landmarks. For detecting eye closure, only 12 are needed (6 per eye).

### 2. **Eye Aspect Ratio (EAR)**

EAR is computed from distances between eyelid landmarks:

```
EAR = (vertical1 + vertical2) / (2 × horizontal)
```

* **High EAR** → eyes open
* **Low EAR** → eyes closing

### 3. **Drowsiness Logic**

* If EAR stays below threshold for a certain number of consecutive frames (e.g., 10), an alert is triggered.
* A cooldown timer prevents repeated alerts.

---

## 📁 Project Structure

```
Drowsiness-Detection/
│
├── drowsiness_gui.py      # Main application with UI
├── README.md              # Documentation
└── requirements.txt       # Optional: list of dependencies
```

---

## 🔊 Alerts

The system uses **pyttsx3**, an offline text-to-speech engine, to speak:

> "Please wake up"

This avoids loading any external audio files and works on all platforms.

---

## 🧪 Adjusting Sensitivity

If you get false alerts or missed detections, try tweaking:

* **EAR threshold**: Increase slightly (0.23 → 0.25)
* **Frames for alert**: Increase if blinking triggers alarms

Example setups:

* Driving: EAR = 0.23, Frames = 12
* Computer use: EAR = 0.25, Frames = 8

---

## ❗ Notes

* Make sure you have good lighting.
* Avoid covering eyes with glasses that reflect.
* The system detects drowsiness based on eye closure — not yawning or head pose.


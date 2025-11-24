import cv2
import time
import math
import mediapipe as mp
import pyttsx3


# webcam
cam = cv2.VideoCapture(0)

# mediapipe face mesh setup
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# offline voice alert
speaker = pyttsx3.init()

# eye landmarks for EAR calculation (mediapipe indices)
L_EYE = [362, 385, 387, 263, 373, 380]
R_EYE = [33, 160, 158, 133, 153, 144]

# settings
EAR_LIMIT = 0.23
FRAMES_NEEDED = 10
cooldown = 4
last_alert = 0


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def get_ear(points):
    # EAR formula using 6 points
    p1, p2, p3, p4, p5, p6 = points
    v1 = dist(p2, p6)
    v2 = dist(p3, p5)
    h = dist(p1, p4)
    if h == 0:
        return 0
    return (v1 + v2) / (2.0 * h)


counter = 0

print("Press q to stop.")
while True:
    ok, frame = cam.read()
    if not ok:
        break

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out = face_mesh.process(rgb)

    if out.multi_face_landmarks:
        lm = out.multi_face_landmarks[0].landmark

        # convert landmark coords
        left = [(int(lm[i].x * w), int(lm[i].y * h)) for i in L_EYE]
        right = [(int(lm[i].x * w), int(lm[i].y * h)) for i in R_EYE]

        # draw small circles around eyes (just to see tracking)
        for x, y in left + right:
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # EAR values
        ear_left = get_ear(left)
        ear_right = get_ear(right)
        ear = (ear_left + ear_right) / 2

        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

        # drowsiness logic
        if ear < EAR_LIMIT:
            counter += 1
        else:
            counter = 0

        if counter >= FRAMES_NEEDED:
            cv2.putText(frame, "Drowsiness Alert!", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

            now = time.time()
            if now - last_alert > cooldown:
                speaker.say("Please wake up")
                speaker.runAndWait()
                last_alert = now

    cv2.imshow("Drowsiness Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

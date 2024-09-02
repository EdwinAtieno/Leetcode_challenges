import pickle
import time

import cv2
import mediapipe as mp
import numpy as np
from picamera2 import Picamera2

model_dict = pickle.load(open("model_v2.p", "rb"))
model = model_dict["model"]

# Create a Picamera2 object
picam2 = Picamera2()

# Define the camera Res
dispW = 640
dispH = 480

# Configuring the Camera input
picam2.preview_configuration.main.size = (dispW, dispH)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.controls.FrameRate = 20
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# Variables for FPS viewer
fps = 0
pos = (10, 40)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1
weight = 1
myColor = (0, 0, 255)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

labels_dict = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",
}

while True:
    tStart = time.time()

    data_aux = []
    x_ = []
    y_ = []

    # Capture the image
    im = picam2.capture_array()

    # Display the FPS count
    cv2.putText(
        im, str(int(fps)) + " FPS", pos, font, height, myColor, weight
    )

    H, W, _ = im.shape

    im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

    results = hands.process(im_rgb)
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

        x1 = int(min(x_) * W) - 15
        y1 = int(min(y_) * H) - 15

        x2 = int(max(x_) * W) - 15
        y2 = int(max(y_) * H) - 15

        prediction = model.predict([np.asarray(data_aux)])

        predicted_character = labels_dict[int(prediction[0])]

        cv2.rectangle(im, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(
            im,
            predicted_character,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.3,
            (0, 0, 0),
            3,
            cv2.LINE_AA,
        )

    tEnd = time.time()
    loopTime = tEnd - tStart
    fps = 0.9 * fps + 0.1 * (1 / loopTime)

    cv2.imshow("frame", im)
    cv2.waitKey(1)

cap.release()  # noqa
cv2.destroyAllWindows()

import pickle
import tkinter as tk
from tkinter import ttk

import cv2
import mediapipe as mp
import numpy as np
from PIL import (
    Image,
    ImageTk,
)

model_dict = pickle.load(open("./model.p", "rb"))
model = model_dict["model"]

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)


class CameraApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.cap = cv2.VideoCapture(0)

        self.canvas = tk.Canvas(
            window,
            width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH),
            height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT),
        )
        self.canvas.pack()

        self.btn_start = ttk.Button(window, text="Start", command=self.start)
        self.btn_start.pack(padx=10, pady=10)

        self.btn_exit = ttk.Button(window, text="Exit", command=self.exit_app)
        self.btn_exit.pack(padx=10, pady=10)

        self.update()
        self.window.mainloop()

    def start(self):
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
        data_aux = []
        x_ = []
        y_ = []

        ret, frame = self.cap.read()
        if ret:
            H, W, _ = frame.shape

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,  # image to draw
                        hand_landmarks,  # model output
                        mp_hands.HAND_CONNECTIONS,  # hand connections
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

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

                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10

                x2 = int(max(x_) * W) - 10
                y2 = int(max(y_) * H) - 10

                prediction = model.predict([np.asarray(data_aux)])

                predicted_character = labels_dict[int(prediction[0])]

                self.canvas.delete(
                    "all"
                )  # Clear previous drawings on the canvas

                self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="black", width=4
                )
                self.canvas.create_text(
                    x1,
                    y1 - 10,
                    text=predicted_character,
                    font=("Helvetica", 13),
                    fill="black",
                )

            self.window.after(10, self.start)

    def exit_app(self):
        self.cap.release()
        self.window.destroy()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(
                image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            )
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update)


# Create a window and pass it to CameraApp
root = tk.Tk()
app = CameraApp(root, "Tkinter Camera App")


"""
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from inventory import models, serializers


def validate_ids(data, field="id", unique=True):

    if isinstance(data, list):
        id_list = [int(x[field]) for x in data]

        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError("Multiple updates to a single {} found".format(field))

        return id_list

    return [data]


class ProductView(generics.UpdateAPIView):
    serializer_class = serializers.ProductSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(ProductView, self).get_serializer(*args, **kwargs)

    def get_queryset(self, ids=None):
        if ids :
            queryset = models.Product.objects.filter(id__in=ids)
        else:
            queryset = models.Product.objects.all()
        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):

        ids = validate_ids(request.data)

        instances = self.get_queryset(ids=ids)

        serializer = self.get_serializer(
            instances, data=request.data, partial=False, many=True
        )

        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

"""

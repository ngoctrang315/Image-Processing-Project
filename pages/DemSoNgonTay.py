
import mediapipe as mp
import cv2
import math
import numpy as np
import os
import streamlit as st
import base64

st.set_page_config(
    page_title="Đếm số ngón tay",
    page_icon="👋",
)
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('./Background/DemSoNgonTay.jpg')  
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #748A88;
    }
</style>
""", unsafe_allow_html=True)
  
st.markdown(
    """
    <style>
    .red-text {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True
)
Hands = mp.solutions.hands
Draw = mp.solutions.drawing_utils

class HandDetector:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.hands = Hands.Hands(max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence,
                                   min_tracking_confidence=min_tracking_confidence)

    def findHandLandMarks(self, image, handNumber=0, draw=False):
        originalImage = image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # mediapipe needs RGB
        results = self.hands.process(image)
        landMarkList = []

        if results.multi_handedness:
            label = results.multi_handedness[handNumber].classification[0].label  # label gives if hand is left or right
            #account for inversion in cam
            if label == "Left":
                label = "Right"
            elif label == "Right":
                label = "Left"

        if results.multi_hand_landmarks:  # returns None if hand is not found
            hand = results.multi_hand_landmarks[handNumber] #results.multi_hand_landmarks returns landMarks for all the hands

            for id, landMark in enumerate(hand.landmark):
                # landMark holds x,y,z ratios of single landmark
                imgH, imgW, imgC = originalImage.shape  # height, width, channel for image
                xPos, yPos = int(landMark.x * imgW), int(landMark.y * imgH)
                landMarkList.append([id, xPos, yPos, label])

            if draw:
                Draw.draw_landmarks(originalImage, hand, Hands.HAND_CONNECTIONS)
        return landMarkList


handDetector = HandDetector(min_detection_confidence=0.7)

def main():
    st.title("Hand Detection App")
    cam = cv2.VideoCapture(0)
    result_image = st.empty()
    count_text = st.empty()
    x_text = st.empty()
    y_text = st.empty()

    while True:
        status, image = cam.read()
        if not status:
            continue

        image = cv2.flip(image, 1)

        # Convert image to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        handLandmarks = handDetector.findHandLandMarks(image=image_rgb, draw=True)
        count = 0
        x = 0
        y = 0

        if len(handLandmarks) != 0:
            if handLandmarks[4][1] + 50 < handLandmarks[5][1]:  # Thumb finger
                count = count + 1
            if handLandmarks[8][2] < handLandmarks[6][2]:  # Index finger
                count = count + 1
            if handLandmarks[12][2] < handLandmarks[10][2]:  # Middle finger
                count = count + 1
            if handLandmarks[16][2] < handLandmarks[14][2]:  # Ring finger
                count = count + 1
            if handLandmarks[20][2] < handLandmarks[18][2]:  # Little finger
                count = count + 1
            x = handLandmarks[4][1]
            y = handLandmarks[4][2]

        count_text.text(f"Count: {count}")
        x_text.text(f"x = {x}")
        y_text.text(f"y = {y}")

        # Draw count text on the image
        cv2.putText(image_rgb, f"Count: {count}", (45, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 10)


        result_image.image(image_rgb, channels="RGB")

        if cv2.waitKey(1) == ord("q"):
            cam.release()
            break

if __name__ == "__main__":
    main()

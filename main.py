import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()



while True:
    success, img = cap.read()






    cv2.imshow("image",img)
    cv2.waitKey(0)

    
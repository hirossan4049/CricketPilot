from time import sleep

import cv2
import numpy as np
import mss
import mss.tools
from pyautogui import click

sct = mss.mss()
monitor = {"top": 250, "left": 260, "width": 35, "height": 30}

hit = False
while True:
    sct_mss = sct.grab(monitor)
    image = np.array(sct_mss)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # find red(ball) color
    bgrLower = np.array([200, 0, 0])
    bgrUpper = np.array([255, 70, 70])
    img_mask = cv2.inRange(image, bgrLower, bgrUpper)
    bgrResult = cv2.bitwise_and(image, image, mask=img_mask)
    gray = cv2.cvtColor(bgrResult, cv2.COLOR_BGR2GRAY)
    _, bin_img = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    if contours:
        if not hit:
            print("find")
            click(250,280)
            hit = True
    else:
        hit = False

    cv2.drawContours(bin_img, contours, -1, color=(0, 255, 0), thickness=2)

    cv2.imshow('jack', bin_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


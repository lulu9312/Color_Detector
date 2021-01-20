"""
Task: Color Identification
Name: Pranav Lulu
Domain: IOT & Computer Vision Intern 
"""
# import necessary modules
import cv2
import numpy as np

cap = cv2.VideoCapture(0) #capture video from webcam

while True:
    _, frame = cap.read()                            #capture every frame
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #convert BGR image to HSV
    
    #Red Color
    low_red = np.array([161,155,84])                 #low value of HSV for red 
    high_red = np.array([179,255,255])               # high value of HSV for red
    red_mask = cv2.inRange(hsv_frame,low_red,high_red) # red mask
    red = cv2.bitwise_and(frame,frame,mask=red_mask)
    
    # Blue Color
    low_blue = np.array([94,80,2])                   #low value of HSV for blue 
    high_blue = np.array([126,255,255])              #low value of HSV for blue
    blue_mask = cv2.inRange(hsv_frame,low_blue,high_blue) # blue mask
    blue = cv2.bitwise_and(frame,frame,mask=blue_mask)
    
    # Green Color
    low_green = np.array([25,52,72])                 #low value of HSV for green
    high_green = np.array([126,255,255])             #low value of HSV for green
    green_mask = cv2.inRange(hsv_frame,low_green,high_green) # green mask
    green = cv2.bitwise_and(frame,frame,mask=green_mask)
    
    #Results
    cv2.imshow("Red",red)
    cv2.imshow("Blue",blue)
    cv2.imshow("Green",green)
    key = cv2.waitKey(1)
    if key == 27:
       break;
    

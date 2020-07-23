#######  the purpose of this code is : to work with the mouse , click on a point and zoom in that point , then blur this point   #######

import cv2
import numpy as np 

######   defind function   #########################################

def mousecall(event,x,y,flags,param):
######    if the left  key is double_click:    zoom in #############
    if event == cv2.EVENT_LBUTTONDBLCLK:
        zoomin(x,y)    
######    if the right  key is double_click:    zoom out ###########
    elif event==cv2.EVENT_RBUTTONDBLCLK:
        zoomout()

def mousenone(event,x,y,flags,param):
    return 0

def zoomin(x,y):
    cv2.setMouseCallback('image',mousenone)

    while(True):
        imagee = cv2.imread('1.jpg')
#####   cut the clicked part and zoom in with the desired scale  ######
        cut = imagee[y-50:y+50,x-50:x+50]
        resized = cv2.resize(cut,(300,300))
        cv2.imshow('imagee',resized)

######  bluring the cue      ##########################################
        blured = cv2.blur(cut, (11, 11))
        cv2.imshow('Blured', blured)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            zoomout()
            break


def zoomout():
    imagee = cv2.imread('1.jpg')
    cv2.imshow('image',imagee)

#####  end of define function     ########################################

#####  program starts   ##################################################

imagee = cv2.imread('1.jpg')

while (True):
    cv2.setMouseCallback('image',mousecall)
    imagee = cv2.imread('1.jpg')
    cv2.imshow('image',imagee)

######  if we enter key ("q") ,will exit the program #####################

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

######    if we enter key ("s") ,will save the program ###################
    elif cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('1.jpg',imagee)
        print('save')

######   program ends    #################################################

cv2.destroyAllWindows()


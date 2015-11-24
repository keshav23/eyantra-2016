############################################
import numpy as np
import cv2
############################################

############################################
#Teams can add other helper functions
#which can be added here

def play(img):
    ############################################
    '''
    img-- a single test image as input argument
    No_pos_D1 -- List containing detected numbers in Division D1
    No_pos_D2 -- List of pair [grid number, value]

    '''
    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #ret,thresh = cv2.threshold(gray,127,255,0)
    #contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(img,contours,-1,(0,255,0),3)
    #print len(contours)
    #print "Area = ", cv2.contourArea(contours)
    No_pos_D1=3
    No_pos_D2=2
    ############################################
    
    ############################################
    ## Show the image
    cv2.imshow('image',img)
    ############################################
    return No_pos_D1, No_pos_D2
############################################

############################################
if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('test_images/test_image1.png')
    No_pos_D1,No_pos_D2 = play(img)
    print No_pos_D1
    print No_pos_D2
############################################

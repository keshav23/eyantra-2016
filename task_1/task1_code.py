import numpy as np
import cv2

#Teams can add other helper functions
#which can be added here

def play(img):
    '''
    img-- a single test image as input argument
    No_pos_D1 -- List containing detected numbers in Division D1
    No_pos_D2 -- List of pair [grid number, value]

    '''
    
    #add your code here
        
    return No_pos_D1, No_pos_D2


if __name__ == "__main__":
    #code for checking output for single image
    img = cv2.imread('test_images/test_image1.png')
    No_pos_D1,No_pos_D2 = play(img)
    print No_pos_D1
    print No_pos_D2

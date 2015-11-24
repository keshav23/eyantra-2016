############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image1.jpg')
############################################

############################################
## Do the processing
# Need a binary Image

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
print kernel
#erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(thresh, kernel, iterations = 3)
closing = cv2.erode(dilation, kernel, iterations = 3)
#dilation1 = cv2.dilate(img, kernel, iterations = 2)
contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
number=150
for counter in range(1,len(contours)):
    if cv2.contourArea(contours[counter])>=number:    
        cv2.drawContours(img,contours,counter,(0,255,0),2)
print len(contours)
print "Area = ", cv2.contourArea(contours[10])
#print "Perimeter = ", cv2.arcLength(contours,True)
#M = cv2.moments(contours[i])
#cx = int(M['m10']/M['m00'])
#cy = int(M['m01']/M['m00'])
#print "Centroid = ", cx, ", ", cy
#cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
############################################

############################################
## Show the image

cv2.imshow('image',img)

############################################

############################################
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
############################################

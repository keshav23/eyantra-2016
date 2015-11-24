
############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image2.jpg')
############################################
#define the function

def number(a,p):
    num=-1
    if a>1850 and a<1900:
        num=0
    elif a>840 and a<890:
        num=1
    elif a>1220 and a<1252 and p<242:
        num=2
    elif a>1200 and a<1250 and p>242:
        num=3
    elif a>1350 and a<1425:
        num=4
    elif a>1252 and a<1275:
        num=5
    elif a>1620 and a<1650:
        num=6
    elif a>975 and a<1025:
        num=7
    elif a>1800 and a<1850:
        num=8
    elif a>1590 and a<1620:
        num=9
    return num  
############################################
## Do the processing
# Need a binary Image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
arr_number=[]
arr_position=[]
for counter in range (len(contours)):
    if cv2.contourArea(contours[counter])>800 and cv2.contourArea(contours[counter])<2000:
        cv2.drawContours(img,contours,counter,(0,255,0),2)
        cv2.arcLength(contours[counter],True)
        M = cv2.moments(contours[counter])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        area=cv2.contourArea(contours[counter])
        perimeter=cv2.arcLength(contours[counter],True)
        print "Area = ", area, "Centroid = ", cx, ", ", cy, "Perimeter = ", perimeter
        cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
        found_number=number(area,perimeter)
        if cx< 300:
            arr_number.append(found_number)
            arr_position.append(cy*10+cx)
for i in range( len( arr_position ) ):
    least = i
    for k in range( i + 1 , len( arr_position ) ):
        if arr_position[k] < arr_position[least]:
            least = k
    tmp=arr_position[least]
    arr_position[least]=arr_position[i]
    arr_position[i]=tmp
    tmp1=arr_number[least]
    arr_number[least]=arr_number[i]
    arr_number[i]=tmp1
    
 
print arr_number
#print "Area = ", cv2.contourArea(contours[counter])
#print "Perimeter = ", cv2.arcLength(contours[i],True)
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

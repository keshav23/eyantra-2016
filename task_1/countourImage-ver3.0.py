
############################################
## Import OpenCV
import numpy
import cv2
############################################

############################################
## Read the image
img = cv2.imread('test_image1.jpg')
############################################
#define the function

def number(a,p):
    num=-1
    if a>1850 and a<1900:
        num=0
    elif a>800 and a<950:
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
def cell_number(cell):
    #print cell
    min=abs(cell-5256)
    pos=-1
    cell_mapping=[1500,1610,1725,1830,2500,2610,2725,2830,3500,3610,3725,3830,4500,4610,4725,4830,5500,5610,5725,5830,6500,6610,6725,6830]
    for i in range(24):
        if(abs(cell-cell_mapping[i])<min):
            pos=i
            min=abs(cell-cell_mapping[i])
    return pos
############################################
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
grid1_number=[]
grid1_number_position=[]
grid2_number=[]
grid2_number_position=[]
for counter in range (len(contours)):
    if cv2.contourArea(contours[counter])>800 and cv2.contourArea(contours[counter])<2000:
        cv2.drawContours(img,contours,counter,(0,255,0),2)
        cv2.arcLength(contours[counter],True)
        M = cv2.moments(contours[counter])
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        area=cv2.contourArea(contours[counter])
        perimeter=cv2.arcLength(contours[counter],True)
        print "Area = ", area, "Centroid = ", cx, ", ", cy, "Perimeter = ", perimeter ,"Number", number(area,perimeter)
        cv2.circle(img,(cx,cy), 5, (0,0,255), -1)
        found_number=number(area,perimeter)
        if cx < 300:
            grid1_number.append(found_number)
            grid1_number_position.append((cy/100)*1000+cx)
        else:
            grid2_number.append(found_number)
            grid2_number_position.append((cy/100)*1000+cx)
for i in range( len( grid1_number_position ) ):
    least = i
    for k in range( i + 1 , len( grid1_number_position ) ):
        if grid1_number_position[k] < grid1_number_position[least]:
            least = k
    tmp=grid1_number_position[least]
    grid1_number_position[least]=grid1_number_position[i]
    grid1_number_position[i]=tmp
    tmp1=grid1_number[least]
    grid1_number[least]=grid1_number[i]
    grid1_number[i]=tmp1
for i in range( len( grid2_number_position ) ):
    least = i
    for k in range( i + 1 , len( grid2_number_position ) ):
        if grid2_number_position[k] < grid2_number_position[least]:
            least = k
    tmp=grid2_number_position[least]
    grid2_number_position[least]=grid2_number_position[i]
    grid2_number_position[i]=tmp
    tmp1=grid2_number[least]
    grid2_number[least]=grid2_number[i]
    grid2_number[i]=tmp1
#print arr1_number
matrix=[]
i=0
while i<(len( grid2_number)-1):
    if((grid2_number_position[i+1]-grid2_number_position[i])<60):
        two_digit_number=(grid2_number[i]*10)+grid2_number[i+1]
        matrix.append([two_digit_number,cell_number((grid2_number_position[i]+grid2_number_position[i+1])/2)])
        i=i+2
    else:
        matrix.append([grid2_number[i],cell_number(grid2_number_position[i])])
        i=i+1
if i==len(grid2_number)-1:
    matrix.append([grid2_number[i],cell_number(grid2_number_position[i])])
print grid1_number
#print arr1_number
print matrix
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

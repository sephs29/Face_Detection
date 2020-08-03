#Highlights
This project has two scripts: 
1) to detect screen image with single face in the image 
2) to detect faces and eyes in the image

I have used opencv and haarcascade, to detect faces.
The cascade file has a function called detectMultiScale, in which I used the two parameters- Scale factor and minNeighbours. 
On tweaking these, the efficiency of the cascade to detect faces can be adjusted.
I worked with three cascades:- 1) face_cascade 2) face_cascade2 3) profileface_cascade
I found the face_cascade2 the most accurate.

The cascade are most sensitive in grayscale than in color scale.
image = "team4.png"
The output is colored, but the image used for processing gray or colored.
with gray scale(roi_gray)
<img src = result/gray.png>
with color scale(roi_color)
<img src = result/color.png>

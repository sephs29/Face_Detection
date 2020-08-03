#Highlights
This project has two scripts: 
1) to detect screen image with single face in the image 
2) to detect faces and eyes in the image

I have used opencv and haarcascade, to detect faces.
<br>The cascade file has a function called detectMultiScale, in which I used the two parameters- Scale factor and minNeighbours. 
<br>On tweaking these, the efficiency of the cascade to detect faces can be adjusted.
<br>I worked with three cascades:- 1) face_cascade 2) face_cascade2 3) profileface_cascade
<br>I found the face_cascade2 the most accurate.

The cascade are most sensitive in grayscale than in color scale.
<br>image = "team4.png"
<br>The output is colored, but the image used for processing gray or colored.
<br>with gray scale(roi_gray)
<br><img src = result/gray.PNG>
<br>with color scale(roi_color)
<br><img src = result/color.PNG>

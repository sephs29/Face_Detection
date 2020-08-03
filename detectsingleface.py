import cv2
import os

class facedetect():
    def face_detection(self, img_file_path):

        img = cv2.imread(img_file_path)
        
        if img is not None:
            height, width, depth = img.shape
            denominator = max(height, width)
            imgScale = 600/ denominator
            newX, newY = img.shape[1] * imgScale, img.shape[0] * imgScale
            img = cv2.resize(img, (int(newX), int(newY)))
            
            '''RBG to gray scale'''
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            path = cv2.data.haarcascades
            face_cascade = cv2.CascadeClassifier(path+"\haarcascade_frontalface_default.xml")
            face_cascade2 = cv2.CascadeClassifier(path+"\haarcascade_frontalface_alt.xml")
            eye_cascade = cv2.CascadeClassifier(path+"\haarcascade_eye.xml")
            profileface_cascade = cv2.CascadeClassifier(path+"\haarcascade_profileface.xml")
            #scaleFactor > 1, 'minNeighbors'
            faces = face_cascade.detectMultiScale(gray,1.1, 12 )#1.1,1
            faces2 = face_cascade2.detectMultiScale(gray,1.05, 8)#1.1,1
            profileface = profileface_cascade.detectMultiScale(gray,1.05,1 )#1.05, 8
            
            face_list = [faces2,faces,profileface,]
            face_len_list = [len(faces2),len(faces),len(profileface),]
            print(face_list,'\n',face_len_list)
            try:
                #if'1' exists in the list,picks up the first position value
                index = face_len_list.index(1)
                face_detected = face_list[index]
                #face_detected = face_list[1]
                if len(face_detected) == 1:#double-check number of faces
                #if len(face_detected):
                    for (x, y, w, h) in face_detected:
                        #gray for detecting
                        #colored img for making location marks
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0,0,255), 5)

                        roi_gray =  gray[y:y+h,x:x+h]
                        #roi_color = img[y:y+h,x:x+h]
                        eyes = eye_cascade.detectMultiScale(roi_gray)
                        try:
                            if len(eyes):
                                for (ex, ey, ew, eh) in eyes:
                                    cv2.rectangle(img,
                                            (x + ex,y + ey),
                                            (x + ex + ew,y + ey + eh),
                                            (0, 255, 0), 
                                            5)
                            else:
                                print("No eyes detected.")                                
                        except:
                            print("Eyes Detection failed.")
                    cv2.imshow('image',img)
                    cv2.waitKey(0)
                else:
                    print('Number of Face Detected is more than one.')
            except:
                print('Image has more than one face or no face at all.')
                #print('Number of Face Detected is either greater or less than one.')
                #print("Face Detection failed.")
        else:
            print("Image not found.")
if __name__ == "__main__":
    #img_name = os.listdir(os.path.join(os.getcwd() ,'Images'))[0]#first image
    #img_name = os.listdir(os.path.join(os.getcwd() ,'Images'))[1]#second image

    img_name = "team3.jpg"
    img_path  = os.path.join(os.getcwd() ,'Images',img_name)
    obj = facedetect()
    obj.face_detection(img_path)
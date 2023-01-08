# plot photo with detected faces using opencv cascade classifier
from cv2 import imread, resize
from cv2 import imshow
from cv2 import waitKey
from cv2 import destroyAllWindows
from cv2 import CascadeClassifier
from cv2 import rectangle

import shutil


from os import listdir, mkdir
from os.path import isfile, join
mypath= 'Path where the images are stored'
mypath2= mypath + "\\" +'face'
mkdir(mypath2)
onlyfiles= [f for f in listdir(mypath) if isfile(join(mypath,f)) & f.endswith('.jpg')]

a=0
while True:
    temp= "\\"
    newurl= mypath + temp+  onlyfiles[a]
    newurl2= mypath+temp + 'face'+ temp+  onlyfiles[a]
    # load the photograph
    pixels = imread(newurl)
    pixels2= resize(pixels,(400,400))
    # load the pre-trained model
    classifier = CascadeClassifier('D:\haarcascade_frontalface_default.xml')
    # perform face detection
    bboxes = classifier.detectMultiScale(pixels2, 1.1, 3)
    if len(bboxes)==0:
        print("No face detected")
    else:
        print("Face detected")
        shutil.move(newurl,newurl2)
    a=a+1
# # print bounding box for each detected face
# for box in bboxes:
# # print bounding box for each detected face
#     for box in bboxes:
#         # extract
#         x, y, width, height = box
#         x2, y2 = x + width, y + height
#         # draw a rectangle over the pixels
#         rectangle(pixels2, (x, y), (x2, y2), (0,0,255), 1)
# # show the image
# imshow('face detection', pixels2)
# # keep the window open until we press a key
# waitKey(0)
# # close the window
# destroyAllWindows()
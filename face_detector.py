import cv2 
import sys
from random import randrange 

# Load face data into classifier; an object used to classify things
# Use xml algorithm to detected front-facing faces from:
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

# user print(cv2.__file__) to get folder where defualt xml algorithms are stored

#trained_face_data = cv2.CascadeClassifier('\\env\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

def printUsage():
    print("""

        __USAGE__:
        python face_detector.py [options]

        __OPTIONS__:
        -live [camera port]: opens face-detection with camera on specified port (0 is system default camera)
        -img "[relative path]": opens face-detection on specified image

    """)

def highlightImage(img, wait):
    # Converting to grayscale for algorithm to work
    grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces (multi-scale specifies no size restraint)
    # coordinate variable has [[top-left-x top-left-y width height]]
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangles around the faces
    for coordinates in face_coordinates:
        (x, y, w, h) = coordinates
        cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(180, 256), randrange(200, 256), 0), 5)
    cv2.imshow('Face Detection', img)
    if wait:
        cv2.waitKey()
        

def liveMode(port):
    webcam = cv2.VideoCapture(port)
    print("Press esc at any time to quit")
    while True:
        success, frame = webcam.read()
        if success:
            highlightImage(frame, False)
        key = cv2.waitKey(1)
        if key == 27:
            return

if __name__ == '__main__':
    args = sys.argv[1:len(sys.argv)]
    if len(args) == 2:
        trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        if args[0] == "-live":
            port = args[1]
            liveMode(int(port))
        elif args[0] == "-img":
            img_path = args[1]
            img = cv2.imread(img_path)
            highlightImage(img, True)
        else:
            printUsage()
    else:
        printUsage()

print("program terminated...")
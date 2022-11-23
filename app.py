import cv2  # Imports CV2 module (pip install opencv-python)

# capture =cv2.VideoCapture("video.mp4")    ## To detect movement from a video
capture=cv2.VideoCapture(0)   ## To detect movement from a webcam

while capture.isOpened():
    _, frameOne = capture.read()    # Read frame by frame
    _, frameTwo = capture.read()    # Read frame by frame

    frameDifference = cv2.absdiff(frameOne,frameTwo)    # Differnce between both the frames

    frameGrayscale = cv2.cvtColor(frameDifference,cv2.COLOR_BGR2GRAY)   # Convert the frame to grayscale
    blurimage = cv2.GaussianBlur(frameGrayscale,(5,5),0)    # Smoothen the image by applying blur
    _, convertToBinary = cv2.threshold(blurimage,20,255,cv2.THRESH_BINARY)  # Convert the blured image to binary

    contours, hierarchy = cv2.findContours(convertToBinary, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  # Find contours

    for contour in contours:    # Draw rectangle for motion detection
        x,y,w,h = cv2.boundingRect(contour)
        if cv2.contourArea(contour)>300:
            cv2.rectangle(frameOne,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Capture",frameOne)  # Display video, press ESC key to exit
    if cv2.waitKey(500)==27:
        exit()

# read and show
import cv2
import numpy
image=cv2.imread(r'C:\Users\abdul\Documents\mypic.JPG')
cv2.imshow('mypic',image)
cv2.waitKey(0)



#crop image
cv2.imshow("Original", image)
# cropping an image is accomplished using simple NumPy array slices --
# let's crop the face from the image
face = image[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey(0)

# ...and now let's crop the entire body
body = image[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)
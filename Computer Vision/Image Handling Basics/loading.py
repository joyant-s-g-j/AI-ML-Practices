import cv2

image = cv2.imread("logo.jpeg")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")
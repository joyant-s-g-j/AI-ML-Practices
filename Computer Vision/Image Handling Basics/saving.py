import cv2

image = cv2.imread("logo.jpeg")

if image is not None:
    success = cv2.imwrite("output.png", image)
    if success:
        print("Image saved successfully as 'output.png'")
    else:
        print("Failed to save an image")
else:
    print("Error: Could not load image")
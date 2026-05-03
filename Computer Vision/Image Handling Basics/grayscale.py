import cv2

image = cv2.imread("logo.jpeg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    save = cv2.imwrite("output.png", gray)
    if save:
        print("Image saved successfully as 'output.png'")
    else:
        print("Failed to save an image")
else:
    print("Could not load the image")
import cv2

image = cv2.imread("logo.jpeg")

pt1 = (10, 50)
pt2 = (100, 100)
color = (255, 255, 255)
thickness = 4

cv2.rectangle(image, pt1, pt2, color, thickness)

cv2.imshow("Rectangle Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
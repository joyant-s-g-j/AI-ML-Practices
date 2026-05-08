import cv2

image = cv2.imread("logo.jpeg")

pt1 = (50, 100)
pt2 = (300, 100)
color = (255, 255, 255)
thickness = 4

cv2.line(image, pt1, pt2, color, thickness)

cv2.imshow("Line Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
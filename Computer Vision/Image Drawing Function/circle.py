import cv2

image = cv2.imread("logo.jpeg")

center = (100, 100)

color = (255, 255, 255)
thickness = 4

cv2.circle(image, center, 90, color, thickness)

cv2.imshow("Circle Drawing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
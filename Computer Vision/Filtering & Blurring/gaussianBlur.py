import cv2

image = cv2.imread("logo.jpeg")

blurred = cv2.GaussianBlur(image, (21, 21), 0)

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
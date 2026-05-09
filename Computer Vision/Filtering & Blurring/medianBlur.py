import cv2

image = cv2.imread("logo.jpeg")

blurred = cv2.medianBlur(image, 11)

cv2.imshow("Original", image)
cv2.imshow("clean", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
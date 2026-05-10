import cv2

image = cv2.imread("logo.jpeg", cv2.IMREAD_GRAYSCALE)

ret, thres = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", image)
cv2.imshow("Threshold", thres)
cv2.waitKey(0)
cv2.destroyAllWindows()
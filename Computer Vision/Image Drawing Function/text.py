import cv2

image = cv2.imread("logo.jpeg")

cv2.putText(image, "Hello Python Programmer", (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

cv2.imshow("Text writing", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
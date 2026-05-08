import cv2

image = cv2.imread("logo.jpeg")

if image is None:
    print("Error: Image not found")
else:
    flipped_hr = cv2.flip(image, 1)
    flipped_vr = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)

    # cv2.imshow("Flipped Horizontal", flipped_hr)
    # cv2.imshow("Flipped Vertical", flipped_vr)
    cv2.imshow("Flipped Both", flipped_both)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
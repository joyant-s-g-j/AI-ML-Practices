import cv2

image_loc = input("Give me the location of image: ")
image = cv2.imread(image_loc)

if image is not None:
    option = int(input("Select one option: \n1. Show Image \n2. Save Image \nInput Option:"))
    if option == 1:
        cv2.imshow("image showing", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif option == 2:
        output = input("Output name of image: ")
        if output:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            save = cv2.imwrite(output, gray)
            if save:
                print(f"Image saved successfully as '{output}'")
            else:
                print("Failed to save an image")
        else:
            print("Invalid output name")
    else:
        print("Select a valid option")
else:
    print("Could not load image")

    
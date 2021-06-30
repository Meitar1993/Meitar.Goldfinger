import cv2
import numpy as np


def load_img():
    im = cv2.imread('test123.png', 0)
    im_gray = cv2.GaussianBlur(im, (5, 5), 0)
    return im_gray


def nothing(x):
    pass

def main():
    img = load_img()
   # cv2.imshow("Gray scale", img)
    cv2.namedWindow('image')
    cv2.createTrackbar('max', 'image', 300, 300, nothing)
    cv2.createTrackbar('min', 'image', 0, 300, nothing)

    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # Get Parameter values from Trackbar Values
        max = cv2.getTrackbarPos('max', 'image')
        min = cv2.getTrackbarPos('min', 'image')
        print(min,max)
        s = cv2.getTrackbarPos(switch,'image')
        if s == 0:
            im_canny = cv2.Canny(img, min, max)
            result = cv2.inRange(im_canny, min, max)
            cv2.imshow('result', result)
            #newResult = cv2.bitwise_and(img, img, mask = result)
            #cv2.imshow('newResult', newResult)

        else:
            print("else")
            # Finding the Hough Circles according to trackbar parameters
            circles = cv2.HoughCircles(image = im_canny, method = cv2.HOUGH_GRADIENT, dp=1, minDist = 8,
                                       param1= max, param2= min , minRadius=8, maxRadius=12)
            circles = np.uint16(np.around(circles))

            # Drawing the Hough Circles
            for i in circles[0,:]:
                if isinstance(i, np.uint16):
                    continue
                cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
                cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

                # Amount of circles found
                cv2.putText(img, str(circles.shape[1]),
                            (0, img.shape[0]-5),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (255, 255, 255),
                            2)

                cv2.imshow('image', img)
            cv2.waitKey(0)
            #img = load_img()
            print(circles.shape[1])

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
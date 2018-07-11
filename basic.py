import cv2
import numpy as np
from time import sleep

def show_image(image_to_be_displayed):
    img = cv2.imread(image_to_be_displayed)
    cv2.imshow('IMAGE', img)
    cv2.waitKey(0)
    # wait for 10 seconds
    sleep(10)
    cv2.destroyAllWindows()


if __name__=="__main__":
    print("Please import the function to use")

    

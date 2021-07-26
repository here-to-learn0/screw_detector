import numpy as np
import argparse
import cv2 as cv
import matplotlib.pyplot as plt
# import pigpio
import fire

def parse_commandline():
    parser = argparse.ArgumentParser(description="rpi sample python file")
    parser.add_argument('--filename', type=str, help='path to the file')
    args = parser.parse_args()
    return args

def filtering_image(image):
    print("-----Writing original image")
    cv.imwrite("org.jpg", image)

    kernel = np.ones((5,5), np.float32)/25
    dst = cv.filter2D(image, -1, kernel)
    print('------Writing filtered image ')
    cv.imwrite("filtered.jpg", dst)

def print_string(lol="hell0"):
    return lol + "world ddd"



def main():
    # args = parse_commandline()
    # path = args.filename
    # image = cv.imread(path, 0)
    # filtering_image()

    print_string()
    # pi1 = pigpio.pi()
    # print(pi1)
    # pi1.stop()
    # print(pi1)
    


if __name__ == "__main__":
    fire.Fire(print_string)
    main()
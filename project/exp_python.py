import torch
import numpy as np
import argparse
import cv2 as cv
import matplotlib.pyplot as plt
from picamera import PiCamera
from time import sleep
import os
from datetime import datetime 
# import pigpio

def parse_commandline():
    parser = argparse.ArgumentParser(description="rpi sample python file")
    # parser.add_argument('--path', type=str, help='path to the file')
    args = parser.parse_args()
    return args

def filtering_image(image):
    print("-----Writing original image")
    cv.imwrite("org.jpg", image)

    kernel = np.ones((5,5), np.float32)/25
    dst = cv.filter2D(image, -1, kernel)
    print('------Writing filtered image ')
    cv.imwrite("filtered.jpg", dst)

def take_photo(path):

    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    camera.capture(path)
    sleep(3)
    camera.stop_preview()

def main():
    args = parse_commandline()
    # path = args.path

    path = "/home/pi/snap/"
    now = datetime.now()
    full_path = os.path.join(path, str(now) + ".jpg")

    #capute photo 
    # take_photo(full_path)

    #loading model 
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    print(type(model))
    print(model.keys())
    # torch.save(model, "model.pt")
    # model = torch.load("/home/pi/project/yolov5/yolov5s.pt")['model']
    # model.eval()
    # model = torch.load("/home/pi/project/yolov5/models/yolov5s.yaml")
    image = cv.imread("/home/pi/snap/Screenshot from 2021-07-21 22-39-41.png", 0)
    # filtering_image(image)

    #inference 
    results = model(image)
    results.save()
    


if __name__ == "__main__":

    main()
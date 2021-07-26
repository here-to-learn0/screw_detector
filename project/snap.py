from picamera import PiCamera
from time import sleep
import argparse
import datetime

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--photo', action='store_true')
    parser.add_argument('--video', action='store_true')
    args = parser.parse_args()
    return args

def take_photo(name):
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture("snap/" + name + ".jpg")
    camera.stop_preview()

def take_video(name):
    camera = PiCamera()
    camera.start_preview()
    camera.start_recording('video/' + name +'.h264')
    #will take video for 60 secs 
    sleep(5)
    camera.stop_recording()
    camera.stop_preview()

def main():
    args = parse_args()
    name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    
    if args.photo:
        take_photo(name)

    if args.video:
        take_video(name)

if __name__ == "__main__":
    main()
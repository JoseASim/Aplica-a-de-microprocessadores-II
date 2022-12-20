from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.resolution = (2592, 1944)
camera.framerate = 15

camera.start_preview()

camera.annotate_text = "11930742"
sleep(2)
camera.capture('/home/sel/SEL0337/11930742/image.jpg')

camera.stop_preview()

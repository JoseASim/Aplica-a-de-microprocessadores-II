from picamera import PiCamera
from time import sleep

camera = PiCamera()



camera.start_preview()

camera.annotate_text = "11930742"
camera.start_recording('/home/sel/SEL0337/11930742/video.h264')
sleep(5)
camera.stop_recording()

camera.stop_preview()

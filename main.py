import ipCam
from ipCam import OnvifCam

IP = "192.168.0.8"  # Camera IP address
PORT = 80  # Port
USER = "evg"  # Username
PASS = "Fh1234567890"  # Password


my_cam = OnvifCam(IP, PORT, USER, PASS)
my_cam.connect()
my_cam.initPTZ()
my_cam.initAbsoluteMoveRequest()
my_cam.move(0, 90)

import os
import unittest
import time
import imghdr

from rpibebecam.camera.camera import Camera

class CameraTest(unittest.TestCase):
    """ """
    def setUp(self):
        self.picamera = Camera()
        self.picamera.initialize()

    def tearDown(self):
        self.picamera.running = False

    def test_camera(self):
        # Wait for the camera to start
        while self.picamera.running == False:
            time.sleep(0)

        # Wait for a frame to be acquired
        while self.picamera.frame == None:
            time.sleep(0)

        frame = self.picamera.get_frame()

        self.assertEqual(imghdr.what('', h = frame), 'jpeg')

    if __name__ == '__main__':
        unittest.main()

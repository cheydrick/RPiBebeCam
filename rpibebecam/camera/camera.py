import time
import io
import threading
import picamera

# Largely borrowed from Miguel Grinberg's example
# https://github.com/miguelgrinberg/flask-video-streaming

# TODO: make get_frame() wait for the thread to finish writing self.frame
# TODO: replace time.sleep() with threading.event

class Camera(object):
    """ """
    def __init__(self):
        self.thread = None
        self.frame = None
        self.acquiring_lock = None
        self.resolution = (320,240)
        self.image_type = 'jpeg'
        self.running = False
        self.initialized = False
        self.picamera = None
        self.capture_pause_time = 2

    def initialize(self):
        self.picamera = picamera.PiCamera(resolution = self.resolution)
        self.picamera.vflip = True
        self.picamera.hflip = True

        if self.thread == None:
            self.thread = threading.Thread(name = 'picamera_thread', target = self._thread)
            self.thread.start()

            while self.running == False:
                time.sleep(0)
                
        self.initialized = True

    def get_frame(self):
        return self.frame

    def _thread(self):
        self.running = True

        stream = io.BytesIO()

        while self.running == True:
            self.picamera.capture(stream, self.image_type)

            stream.seek(0)

            self.frame = stream.read()

            stream.seek(0)

            time.sleep(self.capture_pause_time)

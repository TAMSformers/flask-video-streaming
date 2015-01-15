from time import time


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files stream.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        pass

    def get_frame(self):
        return open('stream.jpg', 'rb').read()

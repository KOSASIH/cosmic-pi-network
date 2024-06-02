import cv2
import numpy as np

class ObjectDetection:
    def __init__(self, yolo_v4: YOLOv4):
        self.yolo_v4 = yolo_v4

    def detect_objects(self, image: np.ndarray) -> list:
        return self.yolo_v4.detect(image)

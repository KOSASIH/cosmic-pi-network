import cv2
import numpy as np

class ImageProcessing:
    def __init__(self):
        pass

    def apply_threshold(self, image: np.ndarray) -> np.ndarray:
        _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return thresh

    def apply_canny_edge_detection(self, image: np.ndarray) -> np.ndarray:
        return cv2.Canny(image, 50, 150)

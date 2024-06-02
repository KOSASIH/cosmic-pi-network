import cv2
import numpy as np

class Image:
    def __init__(self, path: str):
        self.path = path
        self.image = cv2.imread(path)

    def resize(self, width: int, height: int) -> None:
        self.image = cv2.resize(self.image, (width, height))

    def convert_to_grayscale(self) -> None:
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def get_image(self) -> np.ndarray:
        return self.image

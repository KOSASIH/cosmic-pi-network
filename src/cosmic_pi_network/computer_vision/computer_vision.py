import cv2
import numpy as np

class ComputerVision:
    def __init__(self):
        pass

    def load_image(self, file_path):
        return cv2.imread(file_path)

    def convert_to_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def apply_threshold(self, image):
        _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        return thresh

    def detect_edges(self, image):
        return cv2.Canny(image, 100, 200)

    def detect_faces(self, image):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
        return faces

# Example usage
computer_vision = ComputerVision()
image = computer_vision.load_image("image.jpg")
grayscale_image = computer_vision.convert_to_grayscale(image)
thresh_image = computer_vision.apply_threshold(grayscale_image)
edge_image = computer_vision.detect_edges(grayscale_image)
faces = computer_vision.detect_faces(grayscale_image)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

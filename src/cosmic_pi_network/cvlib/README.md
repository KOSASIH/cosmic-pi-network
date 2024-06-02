# CVLib
=====

This is a computer vision library that provides a simple way to perform image processing, object detection, and YOLOv4.

### Installation

```
1. mkdir build cd build cmake.. cmake --build.
```


### Usage

python from cvlib import Image, YOLOv4, ObjectDetection, ImageProcessing image = Image('image.jpg') yolo_v4 = YOLOv4('yolo_v4.cfg', 'yolo_v4.weights') object_detection = ObjectDetection(yolo_v4) image_processing = ImageProcessing() objects = object_detection.detect_objects(image.get_image()) thresh = image_processing.apply_threshold(image.get_image()) edges = image_processing.apply_canny_edge_detection(image.get_image())


### License

This library is licensed under the MIT License.

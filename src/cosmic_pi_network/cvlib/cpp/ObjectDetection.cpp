#include "ObjectDetection.h"

ObjectDetection::ObjectDetection(YOLOv4* yolo_v4) : yolo_v4_(yolo_v4) {}

std::vector<cv::Mat> ObjectDetection::detect_objects(const cv::Mat& image) {
    return yolo_v4_->detect(image);
}

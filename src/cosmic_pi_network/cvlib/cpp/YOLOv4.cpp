#include "YOLOv4.h"

YOLOv4::YOLOv4(const std::string& config_path, const std::string& weights_path) {
    net_ = cv::dnn::readNetFromDarknet(config_path, weights_path);
}

std::vector<cv::Mat>YOLOv4::detect(const cv::Mat& image) {
    cv::Mat blob = cv::dnn::blobFromImage(image, 1/255, cv::Size(416, 416), cv::Scalar(0,0,0), true, false);
    net_.setInput(blob);
    std::vector<cv::Mat> outs;
    net_.forward(outs);
    return outs;
}

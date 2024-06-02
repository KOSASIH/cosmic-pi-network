#include "ImageProcessing.h"

cv::Mat ImageProcessing::apply_threshold(const cv::Mat& image) {
    cv::Mat thresh;
    cv::threshold(image, thresh, 0, 255, cv::THRESH_BINARY_INV + cv::THRESH_OTSU);
    return thresh;
}

cv::Mat ImageProcessing::apply_canny_edge_detection(const cv::Mat& image) {
    return cv::Canny(image, 50, 150);
}

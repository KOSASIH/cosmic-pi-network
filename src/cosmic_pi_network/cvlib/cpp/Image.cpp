#include "Image.h"

Image::Image(const std::string& path) : path_(path) {
    image_ = cv::imread(path_);
}

void Image::resize(int width, int height) {
    image_ = cv::resize(image_, cv::Size(width, height));
}

void Image::convert_to_grayscale() {
    image_ = cv::cvtColor(image_, cv::COLOR_BGR2GRAY);
}

cv::Mat Image::get_image() {
    return image_;
}

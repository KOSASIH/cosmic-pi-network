cmake_minimum_required(VERSION 3.10)
project(cvlib)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)

add_library(Image Image.cpp)
target_link_libraries(Image ${OpenCV_LIBS})

add_library(YOLOv4 YOLOv4.cpp)
target_link_libraries(YOLOv4 ${OpenCV_LIBS})

add_library(ObjectDetection ObjectDetection.cpp)
target_link_libraries(ObjectDetection ${OpenCV_LIBS} YOLOv4)

add_library(ImageProcessing ImageProcessing.cpp)
target_link_libraries(ImageProcessing ${OpenCV_LIBS})

cmake_minimum_required(VERSION 3.10)

project(AGIFramework)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(${PROJECT_NAME} AGIAgent.cpp KnowledgeGraph.cpp Reasoner.cpp NLPInterface.cpp)

target_link_libraries(${PROJECT_NAME} ${CMAKE_DL_LIBS} spacy)

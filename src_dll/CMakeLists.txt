cmake_minimum_required(VERSION 3.15)
project(calc LANGUAGES CXX)

if(WIN32)
    add_compile_options(/utf-8)
endif()

aux_source_directory(. sources)
add_library(${PROJECT_NAME} SHARED ${sources})
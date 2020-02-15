cmake_minimum_required(VERSION 3.15)
project(calc LANGUAGES CXX)

if(WIN32)
    add_compile_options(/utf-8)
endif()

add_subdirectory(calc)

set(target_name calctest)
aux_source_directory(. sources)
add_executable(${target_name} ${sources})
target_link_libraries(${target_name} PRIVATE calc)
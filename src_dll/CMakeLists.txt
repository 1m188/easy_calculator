cmake_minimum_required(VERSION 3.15)
project(calc)

if(WIN32)
    add_compile_options(/utf-8)
endif()

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/calc)

set(target_name calctest)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} sources)
add_executable(${target_name} ${sources})
target_link_libraries(${target_name} PRIVATE calc)
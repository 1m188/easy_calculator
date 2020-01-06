cmake_minimum_required(VERSION 3.15)
project(CalculateLib)

if(WIN32)
    add_compile_options("/utf-8")
endif()

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/calc)


set(target_name "calculate")
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} SOURCES)
add_executable(${target_name} ${SOURCES})
target_link_libraries(${target_name} PUBLIC "calc")
set(target_name calc)
aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR} sources)
add_library(${target_name} SHARED ${sources})
target_compile_definitions(${target_name} PRIVATE $<$<CONFIG:Debug>:DEBUG>)
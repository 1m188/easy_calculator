add_rules("mode.debug","mode.release")

target("calc")
    set_kind("shared")
    add_files("src/calc/*.cpp")

target("test")
    set_kind("binary")
    add_files("src/**.cpp")
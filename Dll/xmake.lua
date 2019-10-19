add_rules("mode.debug","mode.release")

target("calc")
    set_kind("shared")
    add_files("src/calc/*.cpp")
    
    -- 判定如果是release模式构建的话则把对应的动态链接库文件复制到py的动态链接库加载文件夹下，方便直接使用无需另外复制
    if is_mode("release") then
        after_build(function (target)
            os.cp(target:targetfile(),"../EasyCalculator/dll")
        end)
    end

target("test")
    set_kind("binary")
    add_files("src/**.cpp")
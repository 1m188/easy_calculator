# EasyCalculator

一个用c++和python写的简单的计算器

1. 核心的计算部分使用的c++写的，导出为c风格的函数dll动态链接库供python调用，使用xmake进行构建（关于xmake，可以看[这里](https://github.com/xmake-io/xmake)），之后界面其他的部分都是用的python写的，使用的是python3.6.2 32bit和pyside2 5.11.2。

2. 目前仅支持基本的四则计算和带括号的计算，如果有不规范的表达式部分最后会返回0，但也有一些情况可能就直接报错了。另外由于计算部分并非写的很成熟，对于数据的计算也有范围的要求，最多支持在long long的范围内计算，即64位长度的数据，而且还只支持整数的计算。

## 使用方法
clone项目到本地之后，首先要确认安装了python（建议与上述版本保持一致），并且根据requirements.txt安装了对应的包。之后进入到项目目录之下，使用`xmake f --plat==你的目标平台 --arch==你的目标架构 --mode=release`命令进行构建，`xmake`进行编译，之后进入Dll目录下的build的目录下找到对应平台、模式和架构的文件夹下将对应的calc.dll文件拷贝到EasyCalculator/dll目录下，之后在EasyCalculator目录下运行`python main.py`即可。
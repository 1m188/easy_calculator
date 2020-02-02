#pragma once

#include "../multplat.h"

//用C的函数方式导出供外部调用的函数
#ifdef __cplusplus
extern "C"
{
#endif

    //对外调用的计算接口
    __export long long calc(const char *s, unsigned int length);

#ifdef __cplusplus
}
#endif
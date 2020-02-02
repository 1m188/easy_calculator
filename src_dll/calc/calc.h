#pragma once

//跨平台函数导出约定
#if defined(_WIN32)
#define __export __declspec(dllexport)
#elif defined(__GNUC__) && ((__GNUC__ >= 4) || (__GNUC__ == 3 && __GNUC_MINOR__ >= 3))
#define __export __attribute__((visibility("default")))
#else
#define __export
#endif

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
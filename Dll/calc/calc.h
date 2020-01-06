#ifndef CALC_H
#define CALC_H

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

//以下是计算接口中调用的一些内部计算函数
#include "vector"
#include "string"

//从字符串转换为中缀表达式
std::vector<std::string> str2In(const char *s, unsigned int length);

//从中缀表达式转换为后缀表达式
std::vector<std::string> in2Post(const std::vector<std::string> &inFixExpression);

//通过后缀表达式计算
long long calc(const std::vector<std::string> &postFixExpression);

#endif // CALC_H
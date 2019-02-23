#ifndef CALC_H
#define CALC_H

//定义一些宏，DEBUG的时候进行测试调试，RELEASE的时候生成发布版本dll
#ifdef DEBUG
#define DLL_EXPORT
#elif defined RELEASE
#define DLL_EXPORT __declspec(dllexport)
#endif

//用C的函数方式导出
#ifdef RELEASE
extern "C"
{
#endif

    //对外调用的计算接口
    DLL_EXPORT long long calc(const char *s, unsigned int length);

#ifdef RELEASE
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

#endif
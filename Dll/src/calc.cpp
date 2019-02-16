#include "calc.h"

DLL_EXPORT int calc(char *s, int length)
{
    //获取中缀表达式
    std::vector<std::string> &&inFixExpression = str2In(s, length);

    //获取后缀表达式
    std::vector<std::string> &&postFixExpression = in2Post(inFixExpression);

    //根据后缀表达式计算结果
    int num = calc(postFixExpression);

    return num;
}

std::vector<std::string> str2In(char *s, int length)
{
}

std::vector<std::string> in2Post(const std::vector<std::string> &inFixExpression)
{
}

int calc(const std::vector<std::string> &postFixExpression)
{
}

//测试
#ifdef DEBUG

#include "iostream"

int main()
{
    return 0;
}

#endif
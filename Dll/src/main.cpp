// 测试文件

#include "iostream"
#include "calc/calc.h"

int main()
{
    std::vector<std::string> &&inFixExpression = str2In("2*1234567890", 12);
    std::vector<std::string> &&postFixExpression = in2Post(inFixExpression);
    long long num = calc(postFixExpression);
    std::cout << num;

    return 0;
}
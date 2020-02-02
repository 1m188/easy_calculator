#include "vector"
#include "string"

//从字符串转换为中缀表达式
std::vector<std::string> str2In(const char *s, unsigned int length);

//从中缀表达式转换为后缀表达式
std::vector<std::string> in2Post(const std::vector<std::string> &inFixExpression);

//通过后缀表达式计算
long long calc(const std::vector<std::string> &postFixExpression);
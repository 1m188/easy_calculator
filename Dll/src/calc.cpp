#include "calc.h"
#include "cctype"

DLL_EXPORT int calc(const char *s, int length)
{
    //获取中缀表达式
    std::vector<std::string> &&inFixExpression = str2In(s, length);

    //获取后缀表达式
    std::vector<std::string> &&postFixExpression = in2Post(inFixExpression);

    //根据后缀表达式计算结果
    int num = calc(postFixExpression);

    return num;
}

std::vector<std::string> str2In(const char *s, int length)
{
    std::vector<std::string> inFixExpression;
    std::string t;

    for (int i = 0; i < length; i++)
    {
        //如果是数字直接加进去
        if (isdigit(s[i]))
        {
            t.push_back(s[i]);
        }
        //否则就是符号，如果此时之前有数字的话，说明数字到头了，整个的字符串作为数字加进去，
        //之后把单个的字符符号变成字符串也加进去
        else
        {
            if (!t.empty())
            {
                inFixExpression.push_back(t);
                t.clear();
            }
            t.push_back(s[i]);
            inFixExpression.push_back(t);
            t.clear();
        }
    }

    return inFixExpression;
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
    std::vector<std::string> &&inFixExpression = str2In("123+26-4*(5+5)", 14);
    for (auto cit = inFixExpression.cbegin(); cit != inFixExpression.cend(); cit++)
    {
        std::cout << *cit << ' ';
    }
    return 0;
}

#endif
#include "calc.h"
#include "cctype"
#include "stack"
#include "cstdlib"
#include "sstream"

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

    if (!t.empty())
    {
        inFixExpression.push_back(t);
    }

    return inFixExpression;
}

std::vector<std::string> in2Post(const std::vector<std::string> &inFixExpression)
{
    std::vector<std::string> postFixExpression;
    std::stack<std::string> stack;

    for (auto &s : inFixExpression)
    {
        if (s == "(")
        {
            stack.push(s);
        }
        else if (s == ")")
        {
            while (stack.top() != "(")
            {
                postFixExpression.push_back(stack.top());
                stack.pop();
            }
            stack.pop();
        }
        else if (s == "+" || s == "-")
        {
            while (!stack.empty() && stack.top() != "(")
            {
                postFixExpression.push_back(stack.top());
                stack.pop();
            }
            stack.push(s);
        }
        else if (s == "*" || s == "/")
        {
            while (!stack.empty() && stack.top() != "(" && stack.top() != "+" && stack.top() != "-")
            {
                postFixExpression.push_back(stack.top());
                stack.pop();
            }
            stack.push(s);
        }
        else
        {
            postFixExpression.push_back(s);
        }
    }

    while (!stack.empty())
    {
        postFixExpression.push_back(stack.top());
        stack.pop();
    }

    return postFixExpression;
}

int calc(const std::vector<std::string> &postFixExpression)
{
    std::stack<std::string> stack;

    for (auto &s : postFixExpression)
    {
        if (s == "+" || s == "-" || s == "*" || s == "/")
        {
            int opr = atoi(stack.top().c_str());
            stack.pop();
            int opl = atoi(stack.top().c_str());
            stack.pop();

            int t = 0;
            if (s == "+")
            {
                t = opl + opr;
            }
            else if (s == "-")
            {
                t = opl - opr;
            }
            else if (s == "*")
            {
                t = opl * opr;
            }
            else if (opr != 0)
            {
                t = opl / opr;
            }
            else
            {
                return 0;
            }

            std::stringstream ss;
            ss << t;
            std::string st;
            ss >> st;
            stack.push(st);
        }
        else
        {
            stack.push(s);
        }
    }

    return atoi(stack.top().c_str());
}

//测试
#ifdef DEBUG

#include "iostream"

int main()
{
    std::vector<std::string> &&inFixExpression = str2In("8+9", 3);
    // for (auto cit = inFixExpression.cbegin(); cit != inFixExpression.cend(); cit++)
    // {
    //     std::cout << *cit << ' ';
    // }
    std::vector<std::string> &&postFixExpression = in2Post(inFixExpression);
    // for (auto cit = postFixExpression.cbegin(); cit != postFixExpression.cend(); cit++)
    // {
    //     std::cout << *cit << ' ';
    // }
    int num = calc(postFixExpression);
    std::cout << num;

    return 0;
}

#endif
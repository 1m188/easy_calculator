#include "iostream"
#include "calc/calc.h"
#include "calc/calc_inside.h"

int main()
{
    auto &&x = str2In("123*2", 5);
    for (const std::string &s : x)
    {
        std::cout << s << '\n';
    }

    auto &&y = in2Post(x);
    for (const std::string &s : y)
    {
        std::cout << s << '\n';
    }

    auto &&z = calc(y);
    std::cout << z << '\n';

    long long num = calc("123*2", 5);
    std::cout << num << '\n';

    return 0;
}
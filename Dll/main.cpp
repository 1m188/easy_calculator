#include "iostream"
#include "calc.h"

int main()
{
    long long num = calc("123*2", 5);
    std::cout << num;

    return 0;
}
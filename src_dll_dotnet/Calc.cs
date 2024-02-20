using System.Runtime.InteropServices;
using System.Text;

namespace src_dll_dotnet;

public class Calc
{
    [UnmanagedCallersOnly(EntryPoint = "calc")]
    public static long Calc_(IntPtr s, uint length)
    {
        var arr = new byte[length];
        Marshal.Copy(s, arr, 0, (int)length);
        var str = Encoding.UTF8.GetString(arr);

        // 获取中缀表达式
        var inFixExpression = Str2In(str);

        // 获取后缀表达式
        var postFixExpression = In2Post(inFixExpression);

        // 根据后缀表达式计算结果
        var num = Calc__(postFixExpression);

        return num;
    }


    /// <summary>
    /// 从字符串转换为中缀表达式
    /// </summary>
    /// <param name="s">待转换字符串</param>
    /// <returns>转换完成的中缀表达式</returns>
    private static List<string> Str2In(string s)
    {
        var inFixExpression = new List<string>();
        var t = string.Empty;

        for (int i = 0; i < s.Length; i++)
        {
            // 如果是数字直接加进去
            if (int.TryParse(s[i].ToString(), out _))
            {
                t += s[i];
            }
            // 否则就是符号，如果此时之前有数字的话，说明数字到头了，整个的字符串作为数字加进去，
            // 之后把单个的字符符号变成字符串也加进去
            else
            {
                if (t.Length != 0)
                {
                    inFixExpression.Add(t);
                    t = string.Empty;
                }
                t += s[i];
                inFixExpression.Add(t);
                t = string.Empty;
            }
        }

        if (t.Length != 0)
        {
            inFixExpression.Add(t);
        }

        return inFixExpression;
    }

    /// <summary>
    /// 从中缀表达式转换为后缀表达式
    /// </summary>
    /// <param name="inFixExpression">待转换表达式</param>
    /// <returns>后缀表达式</returns>
    private static List<string> In2Post(List<string> inFixExpression)
    {
        List<string> postFixExpression = [];
        Stack<string> stack = [];

        foreach (var s in inFixExpression)
        {
            if (s == "(")
            {
                stack.Push(s);
            }
            else if (s == ")")
            {
                while (stack.Peek() != "(")
                {
                    postFixExpression.Add(stack.Peek());
                    stack.Pop();
                }
                stack.Pop();
            }
            else if (s == "+" || s == "-")
            {
                while (stack.Count != 0 && stack.Peek() != "(")
                {
                    postFixExpression.Add(stack.Peek());
                    stack.Pop();
                }
                stack.Push(s);
            }
            else if (s == "*" || s == "/")
            {
                while (stack.Count != 0 && stack.Peek() != "(" && stack.Peek() != "+" && stack.Peek() != "-")
                {
                    postFixExpression.Add(stack.Peek());
                    stack.Pop();
                }
                stack.Push(s);
            }
            else
            {
                postFixExpression.Add(s);
            }
        }

        while (stack.Count != 0)
        {
            postFixExpression.Add(stack.Peek());
            stack.Pop();
        }

        return postFixExpression;
    }

    /// <summary>
    /// 通过后缀表达式计算
    /// </summary>
    /// <param name="postFixExpression">后缀表达式</param>
    /// <returns>计算结果</returns>
    private static long Calc__(List<string> postFixExpression)
    {
        Stack<string> stack = [];
        string? ss;

        foreach (var s in postFixExpression)
        {
            if (s == "+" || s == "-" || s == "*" || s == "/")
            {
                // 这里记得使用stringstream的时候每次都要清空，尤其是需要反复使用的时候，没清空的话上次的数据还会残留在流中
                ss = string.Empty;
                ss += stack.Peek().ToString();
                long opr = long.Parse(ss);
                stack.Pop();

                ss = string.Empty;
                ss += stack.Peek().ToString();
                long opl = long.Parse(ss);
                stack.Pop();

                long t = 0;
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

                ss = string.Empty;
                ss += t.ToString();
                var st = ss;
                stack.Push(st);
            }
            else
            {
                stack.Push(s);
            }
        }

        ss = string.Empty;
        ss += stack.Peek().ToString();
        long num = long.Parse(ss);
        return num;
    }
}

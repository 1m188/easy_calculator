using System.Runtime.InteropServices;

namespace src_dll_dotnet;

public class Calc
{
    [UnmanagedCallersOnly(EntryPoint = "add")]
    public static int Add(int a, int b)
    {
        return a + b;
    }
}

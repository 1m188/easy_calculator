import ctypes
import unittest


class Calc:
    def __init__(self, dllPath: str):
        self.dll = ctypes.cdll.LoadLibrary(dllPath)

        self.dll.calc.argtypes = (ctypes.c_char_p, ctypes.c_uint)
        self.dll.calc.restype = ctypes.c_longlong

    def calc(self, s: str) -> int:
        return self.dll.calc(s.encode("utf-8"), len(s))


# test
class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc("dll/calc.dll")

    def test_calc(self):
        s = "2+2*3/6"
        res = self.calc.calc(s)
        self.assertEqual(res, 3)


if __name__ == "__main__":
    unittest.main()

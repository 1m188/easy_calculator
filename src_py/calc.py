import ctypes
import unittest
from pathlib import Path


class Calc:

    def __init__(self):
        path = Path(__file__).resolve().parent / 'dll' / 'calc.dll'
        self.dll = ctypes.cdll.LoadLibrary(str(path))  # 注意path对象不可迭代，要转换成字符串类型

        self.dll.calc.argtypes = (ctypes.c_char_p, ctypes.c_uint)
        self.dll.calc.restype = ctypes.c_longlong

    def calc(self, s: str) -> int:
        return self.dll.calc(s.encode("utf-8"), len(s))


# test
class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_calc(self):
        s = "2+2*3/6"
        res = self.calc.calc(s)
        self.assertEqual(res, 3)


if __name__ == "__main__":
    unittest.main()

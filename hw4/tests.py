import unittest
from assembler import encode_const, encode_read, encode_write, encode_sub
from interpreter import interpreter

class TestConfigTranslator(unittest.TestCase):

    def test_const_encoding(self):
        self.assertEqual(
            encode_const('CONST 447 182'.split())[0],
            [227, 246, 0, 0, 54, 128, 0, 0, 0, 0, 0, 0]
        )

    def test_read_encoding(self):
        self.assertEqual(
            encode_read('READ 786 930'.split())[0],
            [49, 35, 0, 0, 34, 224, 0, 0, 0, 0, 0, 0]
        )

    def test_write_encoding(self):
        self.assertEqual(
            encode_write('WRITE 212 352'.split())[0],
            [172, 172, 0, 0, 3, 64, 0, 0, 0, 0, 0, 0]
        )

    def test_sub_encoding(self):
        self.assertEqual(
            encode_sub('SUB 410 101 196 204'.split())[0],
            [101, 102, 0, 0, 83, 0, 0, 2, 51, 48, 0, 0]
        )

    def test_interpreter(self):
        self.assertEqual(
            interpreter('binary_test.bin', [0] * 100),
            [0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
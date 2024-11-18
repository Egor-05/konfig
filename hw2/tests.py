import unittest
from main import get_dependencies


class TestDependencyVisualizer(unittest.TestCase):

    def test_get_dependencies(self):
        dependencies = get_dependencies('requests')
        self.assertIn('urllib3', dependencies)

    def test_get_dependencies_negative(self):
        dependencies = get_dependencies('requests')
        self.assertNotIn('sys', dependencies)

    def test_invalid_package(self):
        with self.assertRaises(ValueError) as context:
            get_dependencies('qwerty')
        self.assertTrue("Ошибка при " in str(context.exception))


if __name__ == '__main__':
    unittest.main()

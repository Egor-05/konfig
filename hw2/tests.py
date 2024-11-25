import unittest

from main import get_dependencies, load_config


class TestDependencyVisualizer(unittest.TestCase):

    def test_get_dependencies(self):
        dependencies = get_dependencies('requests')
        self.assertEqual(
            [
                'charset-normalizer',
                'idna',
                'urllib3',
                'certifi',
                'PySocks',
                'chardet'
            ],
            dependencies
        )

    def test_get_dependencies_negative(self):
        dependencies = get_dependencies('requests')
        self.assertNotIn('sys', dependencies)

    def test_get_setup(self):
        setup = load_config('setup.csv')
        self.assertEqual(
            {
                'visualizer_path': '.',
                'package_name': 'requests',
                'image_path': 'dependencies',
                'repository_url': 'https://github.com/Egor-05/konfig/tree/main/hw2'
            },
            setup
        )


if __name__ == '__main__':
    unittest.main()

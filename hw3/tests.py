import unittest
from main import translate

class TestConfigTranslator(unittest.TestCase):

    def test_simple_translation(self):
        json_input = '{"name": 1, "value": 42}'
        expected_output = 'name is 1;\nvalue is 42;'
        self.assertEqual(translate(json_input), expected_output)

    def test_array_translation(self):
        json_input = '{"items": [1, 2, 3]}'
        expected_output = 'items is {1, 2, 3};'
        self.assertEqual(translate(json_input), expected_output)

    def test_invalid_json(self):
        with self.assertRaises(ValueError) as context:
            translate('{"name": "example", "value": }')
        self.assertTrue("JSON decode error" in str(context.exception))

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            translate('{"invalid-name": "value"}')
        self.assertTrue("Invalid name" in str(context.exception))

if __name__ == "__main__":
    unittest.main()
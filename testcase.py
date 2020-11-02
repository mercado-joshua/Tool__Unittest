#===========================
# Imports
#===========================

import unittest

#===========================
# Test
#===========================

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = None

    # ==========================================
    def test_program_function1(self):
        pass

    def test_program_function2(self):
        pass

    # ==========================================
    def is_equal(self, first_value, second_value):
        self.assertEqual(first_value, second_value)

    def is_not_equal(self, first_value, second_value):
        self.assertNotEqual(first_value, second_value)

    def is_true(self, value):
        self.assertTrue(value)

    def is_false(self, value):
        self.assertFalse(value)

    def is_none(self, value):
        self.assertIsNone(value)

    def is_not_none(self, value):
        self.assertIsNotNone(value)

    def is_same_object(self, first_value, second_value):
        self.assertIs(first_value, second_value)

    def is_not_same_object(self, first_value, second_value):
        self.assertIsNot(first_value, second_value)

    def is_in_container(self, key, container):
        self.assertIn(key, container)

    def is_not_in_container(self, key, container):
        self.assertNotIn(key, container)

    def is_instance(self, object_, class_name):
        self.assertIsInstance(object_, class_name)

    def is_not_instance(self, object_, class_name):
        self.assertNotIsInstance(object_, class_name)


#===========================
# Executing Test Runner
#===========================

def main():
    # verbosity = 0, 1, 2
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    main()
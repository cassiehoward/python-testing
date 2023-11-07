import unittest
import py_testing


class TestExercises(unittest.TestCase):

    def test_replace_vowels_inputs_ok(self):
        # aaa

        # Arrange
        content = "Testing is fun!"
        ch = "0"
        expected = "T0st0ng 0s f0n!"

        # Act
        actual = py_testing.replace_vowels(content, ch)

        # Assert
        self.assertEqual(expected, actual)

    def test_replace_vowels_input_string_null(self):
        # Arrange
        ch = "*"
        expected = "Invalid input :("

        # Act & Assert
        self.assertEqual(expected, py_testing.replace_vowels(None, ch))

    def test_replace_vowels_input_char_null(self):
        # Arrange & Act & Assert
        self.assertEqual("Invalid input :(", py_testing.replace_vowels("Hello!", None))

    def test_replace_vowels_input_string_without_vowels(self):
        # Arrange & Act & Assert
        self.assertEqual("HGvkjml", py_testing.replace_vowels("HGvkjml", "8"))

    # Homework - make this test pass
    # def test_replace_vowels_input_first_is_not_string(self):
    #
    #     # Arrange & Act & Assert
    #     self.assertEqual(8, py_testing.replace_vowels(8, "8"))

    def test_calculator_addition_ok(self):
        self.assertEqual(8, py_testing.calculator(5, 3, "+"))

    # Homework - tests for - * / ok

    def test_calculator_invalid_operation(self):
        with self.assertRaises(ValueError) as context:
            py_testing.calculator(3, 5, "%")
        self.assertEqual("Invalid operation", str(context.exception))

    # def test_calculator_divide_by_zero(self):
    #     with self.assertRaises(py_testing.DivisionByZeroError):
    #         py_testing.calculator(3, 0, "/")

    def test_calculator_divide_by_zero(self):
        with self.assertRaises(AssertionError) as context:
            py_testing.calculator(3, 0, "/")
        self.assertEqual("Cannot divide by zero", str(context.exception))


if __name__ == '__main__':
    unittest.main()

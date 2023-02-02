# Unittest requires that our test filename starts with the word 'test',
# followed by an underscore and a descriptive name of what we are testing:
import unittest
from evens import even_number_of_evens


# When we have no code, a pass-statement allows for running error-free code:
class TestEvens(unittest.TestCase):

    # Inside our test, we write our assert using the 'assertRaises()' method.
    # The 'assertRaises()' method is called from 'TestCase' and when the test
    # is run, it checks if a TypeError is raised when the function is called
    # with the value '4':
    def test_throws_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)

    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)


# When Python runs a file directly, it names it __main__ and any code beneath
# the if statement will only be run if the name of the file is __main__.
# So, when we run the test file, it will have the name __main__ and this code
# will not run. However, when we run this file, it will have the name __main__
# and it will run this code:
if __name__ == "__main__":
    unittest.main()

import unittest


class Validator:
    """
        Static class that validates the input data
    """
    def __init__(self):
        pass

    @staticmethod
    def validate_digit(digit):
        """
            Validates a given digit

            Args:
                digit: digit to be validated

            Raises:
                ValueError: if it contains more than 1 character
        """
        if len(digit) > 1:
            raise ValueError("Introduceti o singura cifra")

    @staticmethod
    def validate_number(number):
        """
            Validates a given number

            Args:
                number: number to be validated

            Raises:
                ValueError: if it is different than a integer
        """
        try:
            int(number)
        except ValueError:
            raise ValueError("Introduceti un numar")

class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_digit(self):
        self.validator.validate_digit("1")
        self.validator.validate_digit("0")
        self.validator.validate_digit("9")
        self.assertRaises(ValueError, self.validator.validate_digit, "12")
        self.assertRaises(ValueError, self.validator.validate_digit, "124")
        self.assertRaises(ValueError, self.validator.validate_digit, "12a")

    def test_validate_number(self):
        self.validator.validate_number("1")
        self.validator.validate_number("0")
        self.validator.validate_number("9")
        self.assertRaises(ValueError, self.validator.validate_number, "z12")
        self.assertRaises(ValueError, self.validator.validate_number, "a")
        self.assertRaises(ValueError, self.validator.validate_number, "12a")
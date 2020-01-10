import unittest
import Password

class testPassword(unittest.TestCase):
    def test1(self):
        True
class TestIsStrongPassword(unittest.TestCase):
    """Test of strong password detection function."""

    def test_valid_length(self):
        """Test that only a string length of > 8 is accecpted"""
        self.assertEqual(p.valid_length('abcd'), False)
        self.assertEqual(p.valid_length('abcdefg'), False)
        self.assertEqual(p.valid_length('abcdefgh'), True)
        self.assertEqual(p.valid_length('abcdefghi'), True)

    def test_has_upper(self):
        """Test that only strings containing uppercase are accepted"""
        self.assertEqual(p.has_upper('abcd'), False)
        self.assertEqual(p.has_upper('aBcd'), True)
        self.assertEqual(p.has_upper('aBCd'), True)
        self.assertEqual(p.has_upper('Abcd'), True)
        self.assertEqual(p.has_upper('abcD'), True)
        self.assertEqual(p.has_upper('ABCD'), True)

    def test_has_lower(self):
        """Test that only strings containing lowercase are accepted"""
        self.assertEqual(p.has_lower('abcd'), True)
        self.assertEqual(p.has_lower('aBcd'), True)
        self.assertEqual(p.has_lower('aBCd'), True)
        self.assertEqual(p.has_lower('Abcd'), True)
        self.assertEqual(p.has_lower('abcD'), True)
        self.assertEqual(p.has_lower('ABCD'), False)

    def test_has_digit(self):
        """Test that only strings containing lowercase are accepted"""
        self.assertEqual(p.has_digit('abcd'), False)
        self.assertEqual(p.has_digit('a1cd'), True)
        self.assertEqual(p.has_digit('a12d'), True)
        self.assertEqual(p.has_digit('1bcd'), True)
        self.assertEqual(p.has_digit('abc1'), True)
        self.assertEqual(p.has_digit('1234'), True)

    def test_strong_password(self):
        """
        Test strong password function. Passed strings have to pass 
        all tests in valid_length, uppper, lower and digit functions.
        """

        # Test from single functions should all fail 
        # (not met all criteria)
        self.assertEqual(False, p.strong_password('abcd'))
        self.assertEqual(False, p.strong_password('abcdefg'))
        self.assertEqual(False, p.strong_password('abcdefgh'))
        self.assertEqual(False, p.strong_password('abcdefghi'))

        self.assertEqual(False, p.strong_password('abcd'))
        self.assertEqual(False, p.strong_password('aBcd'))
        self.assertEqual(False, p.strong_password('aBCd'))
        self.assertEqual(False, p.strong_password('Abcd'))
        self.assertEqual(False, p.strong_password('abcD'))
        self.assertEqual(False, p.strong_password('ABCD'))

        self.assertEqual(False, p.strong_password('abcd'))
        self.assertEqual(False, p.strong_password('a1cd'))
        self.assertEqual(False, p.strong_password('a12d'))
        self.assertEqual(False, p.strong_password('1bcd'))
        self.assertEqual(False, p.strong_password('abc1'))
        self.assertEqual(False, p.strong_password('1234'))

        # Combinations which met more than one cirteria
        self.assertEqual(False, p.strong_password('12345678'))
        self.assertEqual(False, p.strong_password('Abcdefgh'))
        self.assertEqual(False, p.strong_password('A12345678'))
        self.assertEqual(False, p.strong_password('Abcdfg1'))
        self.assertEqual(True, p.strong_password('A12345678b'))
        self.assertEqual(True, p.strong_password('Abcdefg1'))
        self.assertEqual(True, p.strong_password('123456aB'))
        self.assertEqual(True, p.strong_password('aB345678'))

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()

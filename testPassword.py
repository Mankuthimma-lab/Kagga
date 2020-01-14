import unittest
import Password
import re

class testPassword(unittest.TestCase):
    
        
def valid_length(string):
    """checks if length is > 8 to be a strong password"""
    len_regex = re.compile(r'.{8,}')
    if not len_regex.search(string):
        return False
    return True

def upper_case(string):
    """Check if string contains one upper letter or more"""
    upper_regex = re.compile(r'.*[A-Z]+.*')
    if not upper_regex.search(string):
        return False
    return True

def lower_case(string):
    """Check if string contains one lower letter or more"""
    lower_regex = re.compile(r'.*[a-z]+.*')
    if not lower_regex.search(string):
        return False
    return True

def digit_check(string):
    """Check if one or more signs is a digit"""
    digit_regex = re.compile(r'.*\d+.*')
    if not digit_regex.search(string):
        return False
    return True

def teststrong_password(password):
    """
    Validate if passed password is considered "strong",
    Password is considered strong if:
    - is eight characters or longer
    - contains uppercase and lowercase characters
    - has one digit or more
    """
    if not valid_length(password):
        return False
    if not upper_case(password):
        return False
    if not lower_case(password):
        return False
    if not digit_check(password):
        return False
    return True

if __name__ == '__main__':
    unittest.main()

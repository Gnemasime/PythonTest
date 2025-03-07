

def is_valid_string(input_string):
    # Define the regular expression pattern
    pattern = r'^(?=(?:[^0-9]*[0-9]){2})(?=(?:[^0-9]*[0-9][^0-9]*){3})[a-zA-Z0-9]{6,}$'

    # Check if the input string matches the pattern
    if re.match(pattern, input_string):
        return True
    return False

# Test the function
print(is_valid_string("a1b2c3"))  # Should return True
print(is_valid_string("123abc"))  # Should return False
print(is_valid_string("abc123"))  # Should return True

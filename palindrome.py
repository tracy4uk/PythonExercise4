def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    clean_s = ''.join(s.split()).lower()

    # Compare the string to its reverse
    return clean_s == clean_s[::-1]


# Test the function with examples
print(is_palindrome("abba"))  # Expected output: True
print(is_palindrome("tenet"))  # Expected output: True
print(is_palindrome("straw warts"))  # Expected output: True
print(is_palindrome("example"))  # Expected output: False
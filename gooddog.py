def mirror_string(s):
    # Reverse the string using slicing
    reversed_s = s[::-1]
    # Concatenate the original string with the reversed string
    mirrored_s = s + reversed_s
    return mirrored_s

# Test the function with examples
test_cases = ["good", "Python", "a"]

# Applying the function to each test case
mirrored_strings = [mirror_string(tc) for tc in test_cases]
print(mirrored_strings)
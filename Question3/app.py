import re


def contains_no_whitespace(input_string):
    no_whitespace = re.search(r"\s", input_string)

    # If no whitespace is found, return False; otherwise, return True
    return no_whitespace is None


# Example
input_string1 = "NoWhitespace123"
result1 = contains_no_whitespace(input_string1)
print(f"String '{input_string1}' contains no whitespace: {result1}")

input_string2 = "Contains Whitespace"
result2 = contains_no_whitespace(input_string2)
print(f"String '{input_string2}' contains no whitespace: {result2}")

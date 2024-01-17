import re


def find_whitespace_or_word_string(input_string):
    whitespace_string = re.search(r"^\s*$", input_string)
    word_string = re.search(r"^\w+$", input_string)

    # Check if a match is found and return the result
    if whitespace_string:
        return "String contains only whitespace characters."
    elif word_string:
        return "String contains only word characters."
    else:
        return "String contains a mix of characters."


# Example
input_string1 = "    "
result1 = find_whitespace_or_word_string(input_string1)
print(result1)

input_string2 = "Hello123"
result2 = find_whitespace_or_word_string(input_string2)
print(result2)

input_string3 = "Hello 123"
result3 = find_whitespace_or_word_string(input_string3)
print(result3)

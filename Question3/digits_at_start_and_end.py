import re


def find_digits_at_ends(input_string):
    start_digit = re.search(r"^\d", input_string)
    end_digit = re.search(r"\d$", input_string)

    # Checking if the digit was found and extracting the matched digit
    start_digit_value = start_digit.group() if start_digit else None
    end_digit_value = end_digit.group() if end_digit else None

    return start_digit_value, end_digit_value


# Example
input_string = "5abc123xyz0"
start_digit, end_digit = find_digits_at_ends(input_string)

print(f"Digit at the beginning: {start_digit}")
print(f"Digit at the end: {end_digit}")

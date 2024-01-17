import re


def find_words_with_adjacent_vowels(line):
    pattern = re.compile(r'\b\w*[aeiou]{2}\w*\b', re.IGNORECASE)

    # Using findall to get all matches in the line
    matches = pattern.findall(line)

    return matches


def main():
    file_path = "example.txt"
    print("The words containing adjacent vowels are:\n")

    try:
        with open(file_path, "r") as file:
            # Looping through each line in the file
            for line in file:
                # Find words with two adjacent vowels in the current line
                word_with_adjacent_vowels = find_words_with_adjacent_vowels(line)
                for word in word_with_adjacent_vowels:
                    print(word)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

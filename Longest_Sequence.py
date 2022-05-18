def longest_sequence(sequence):
    sequence = sequence.lower()
    letters = {}
    previous_letter = None

    for letter in sequence:
        if previous_letter:
            if letter == previous_letter:
                letters[letter] += 1
            else:
                letters[letter] = 0

        previous_letter = letter
        if not letters.get(previous_letter):
            letters[previous_letter] = 1

    letter = max(letters, key=letters.get)
    number = letters.get(letter)

    return {letter: number}


if __name__ == "__main__":
    sequence = longest_sequence(input("Enter the sequence: "))
    print(sequence)
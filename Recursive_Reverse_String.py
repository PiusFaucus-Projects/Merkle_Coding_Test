def reverseString(string):
    if len(string) <= 1:
        return string
    reversedString = reverseString(string[1:]) + string[0]
    return reversedString


if __name__ == "__main__":
    string = reverseString(input("Please enter a string to be reversed\n"))
    print(string)
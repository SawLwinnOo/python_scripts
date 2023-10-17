def disemvowel(string):
    vowels = "AEIOUaeiou"

    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for char in string:
        # Check if the character is not a vowel
        if char not in vowels:
            result += char  # Add non-vowel characters to the result

    return result
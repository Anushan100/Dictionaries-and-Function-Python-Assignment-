def if_vowel(char):
    vowel = ["a", "e", "i", "o", "u"]
    if len(char) > 1:
        print("Please enter only one character")
    elif char in vowel:
        return True
    else:
        return False


char = input("Enter a character :")
new_char = char.lower()
print("Is {} a vowel?: ".format(char),if_vowel(new_char))
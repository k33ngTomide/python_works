

def main() -> None:
    word = "Adeleda"
    isPalindrome = palindrome(word)

    print("is ", word, " a palindrome? ", isPalindrome )



def palindrome(word) -> bool:
    newWord = ""
    for counter in range(len(word)):
        character = word[(len(word) - 1) - counter]

        newWord = newWord + character

    return newWord.capitalize() == word.capitalize()


if __name__ == '__main__':
    main()
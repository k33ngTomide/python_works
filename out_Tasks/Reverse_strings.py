
wordEntered = input("Enter a word you want to reverse:  ")

processedWord = []

for counter in range(len(wordEntered)):
    character = wordEntered[(len(wordEntered) - 1) - counter]
    processedWord.append(character)

print(" ".join(map(str, processedWord )))
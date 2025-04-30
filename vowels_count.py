def getVowelsCount(sentence):
    vowels = ["a","e","i","o","u"]
    count = 0

    for letter in sentence:
        if letter in vowels:
            count += 1
    print(count)

sentence = input("Give me a sentence\n")
getVowelsCount(sentence)


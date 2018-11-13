sentence = input("Enter a sentence: ")

words = sentence.split()
new_senence = []
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_senence.append(new_word)
    else:
        vowel = 0
        for letter in word:
            if letter not in "aeiou":
                vowel = vowel + 1
            else:
                break
        consonants = word[:vowel]
        rest = word[vowel:]
        new_senence.append(rest + consonants + "ay")

print(" ".join(new_senence))



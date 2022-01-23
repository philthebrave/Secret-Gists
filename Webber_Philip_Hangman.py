import random

words = []
with open('word_list.txt') as f:
    for line in f:
        words.append(line[0:-1])
word = random.choice(words)
print("The word has {} letters: {}".format(len(word),"*" * len(word)))

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
correct = []
false = []
hidden_list = []

for i in word:
    hidden_list.append("*")

while len(false) < 7 and "*" in hidden_list:
    letter = input("Please enter your next guess: ").lower()
    if letter not in alphabet:
        print("\nThis is not a letter.")
    elif letter in correct or letter in false:
        print("\nYou have already used this letter.")
    else:
        if letter in word:
            correct.append(letter)
        else:
            false.append(letter)
        i = 0
        for l in word:
            if letter == l:
                hidden_list[i] = l
            i += 1
    hidden_word = ""
    for i in hidden_list:
        hidden_word += i
    print("\nThe word is {}".format(hidden_word))

if "*" in hidden_list:
    print("\nyou lose")
else:
    print("\ncongratulations you win")

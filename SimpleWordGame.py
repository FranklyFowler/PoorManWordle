right = 0
wrong = 0

word = "yellow"
brokenword = []
wordlength = len(word)

for i in word:
    brokenword.append(i)

while right != wordlength:
    right = 0
    wrong = 0

    user = input(f"{wordlength} letter word: ")

    if len(user) != wordlength:
        print("Put the same number of letters in the input as the given word")
        continue

    userbrokenword = []

    for j in user:
        userbrokenword.append(j)

    for u in range(len(userbrokenword)):
        if brokenword[u] == userbrokenword[u]:
            right += 1
            print(userbrokenword[u])
        else:
            wrong += 1

    print("Letters right: " + str(right) + "\nLetters wrong: " + str(wrong))

print("YOU GOT IT!")

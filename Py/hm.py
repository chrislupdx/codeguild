import random
with open ("english.txt") as r:
    chunkier = r.read()
def load_words(x):
    return x.split()

goodlist = []

for a in load_words(chunkier):
    if len(a) > 6:
        goodlist.append(a)

gameword = random.choice(goodlist)
print(gameword)

def display_word(word, guesses):
    blanks = ['_' for w in range(len(word))]
    for i in range(len(blanks)):
        if word[i] in guesses:
            blanks[i] = word[i]
    return ''.join(blanks)

lives = 10
guesses = []


while lives > 0:
    guess01 = input("guess a letter?")
    guesses.append(guess01)
    print(display_word(gameword, guesses))

    print("You have {} guesses".format(lives))
    if guess01 not in gameword:
        lives -= 1
    elif display_word(gameword, guesses) == gameword:
        print('win')

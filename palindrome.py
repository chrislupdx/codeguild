word = input('Give me a Palindrome!')
# if word == word[::-1]:
if word == reversed(word):
    print("it be palindrome!")
else: print("lolno")

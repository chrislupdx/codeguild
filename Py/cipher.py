english = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
rot ={'n':0, 'o':1, 'p':2, 'q':3, 'r':4, 's':5, 't':6, 'u':7, 'v':8, 'w':9, 'x':10, 'y':11, 'z':12, 'a':13, 'b':14, 'c':15, 'd':16, 'e':17, 'f':18, 'g':19, 'h':20, 'i':21, 'j':22, 'k':23, 'l':24, 'm':25}
rot_translate = dict(zip(rot.values(), rot.keys()))
querent = input("Input?").lower()
# spaced = ''.join(querent)
# # print(spaced)
# for i in range(len(spaced)):
#     print(english[spaced[i]])
    # print(rot[spaced[i]])
encoded = []
for letter in querent:
    encoded.append(english[letter])

decoded = []
for number in encoded:
    decoded.append(rot_translate[number])

print(''.join(decoded))

# print(''.join([str(s) for s in encoded]))

# take each number in spaced and run it through rot_translate

# reserved_eng = dict(zip(english.values(), english.keys())

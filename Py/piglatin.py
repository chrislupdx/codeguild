pl = input("Gimme werd in Engrish for PigLatin pl0x")
firstletter = pl[0]
lastletter = pl[-1]
if firstletter in ['a','e','i','o','u']:
    print(pl+'yay')
else:
    print(pl[1:] + firstletter + 'ay')

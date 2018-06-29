#Strings, functions,l methods
words = 'i reslly like to code'
# print(words.capitalize())

# print(name.center(120, '*'))
#'*'=fill space, where the * is the pretty filler (stars in the spaces)
# print(words.count("I", beg=1)
# print(words.endswith('words')) #endswith=if words ended with 'words', it would check for stuff
#     print('yeah')
# else:
#     print('nehh')

# word = 'nice code brah'
# name = input('enter your name or press enter to w/e lulz.:') or 'no name'
# print(name)

# words= 'i really like to code'
# print(words.find('o'))
# print(words[15])
#find returns -1 if a thing can't be summoned

#key difference between find vs index (find only finds the first instance of a thing, we'll only get the index for one thing)
#on the other hand, index breaks the code (stops the code with a value error instead of a -1 instead of a shutdown)
# print(nums.isalnum(words))
nums = '1245'
# nums = int(nums)
# else:
#     raise ValueError('must be all numbers')
# print(nums)
#isalpha= should account/hunt/sniff for alpha (spaces do not count)
# print(words.isalpha())
#isdigit/islower etc etc
#isdigit vs isnumber = is numeric only returns if there

# print('isdigit')
# print(nums.isdigit())
# print()
# print('isnumeric')
# print(nums.isnumeric())

story = ['the', 'cat', 'in', 'the', 'hat'] #lesson: strings are immutable, and we tend to make new ones when we need to make changes/mod stuff
# whole_story = ''.join(story) #adds spaces to things nicely
# print('  '.join(story))
# print('*'.join(story))
# print('-'.join(story))

# replace
# print(words.replace('l', '<>'))
# print(words.find('z'))
# print(words.split())
# print(words.title().swapcase())
# print(nums.isdecimal())
#these thigns are methods that help with datatypes, this is specific for manipulating specific pieces, it's super unliekly we'll be kicking off huge stuff (unless if these is a direct response to user input)
#strings are typically for humans to consume, it's ultimately about human communication as opposed to machine manipulation

#exception handling! (1127)
#nameerror= when shit isn't defined yet
#typerror=
while True:
        try:
            query =int(input('press 1 2 or 3:'))
        except ValueError:
            print('pls enter some numbers or integers pls.)
            continue
        finally:  #finally always always executes
        if query = 1
            print('u pressed 1')

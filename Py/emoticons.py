# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Assemble and display the emoticon

import random
eyes = [';', ':']
nose = ['^', '-']
mouths = ['p', 'D', 'P', ')', '(']

eyehole = random.choice(eyes)
snoot = random.choice(nose)
boop = random.choice(mouths)

print(eyehole + snoot + boop)

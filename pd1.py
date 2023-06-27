import random

words = ['neural', 'random', 'python', 'hello', 'lesson']

words_choices = random.sample(words, random.randint(1, 3))

text = str(random.randint(1, 9)).join(words_choices)

print(text)


import os
import sys

print('My OS is', sys.platform, '(', os.name, ')')
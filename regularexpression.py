import re

hand = open('PYTHON.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^function: ', line):
        print(line)

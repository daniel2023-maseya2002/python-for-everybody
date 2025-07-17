xfile = open('DANIEL MASEYA MUBU.txt')
count = 0
for cheese in xfile:
    count = count + 1
print('Line Count:', count)

# Reading the whole file

fhand = open('DANIEL MASEYA MUBU.txt')
inp = fhand.read()
print(len(inp))
print(inp[:100])

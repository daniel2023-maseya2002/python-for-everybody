# Search Through a file
fhand =  open('DANIEL MASEYA MUBU.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('I have gained valuable experience through internships and projects, applying a practical :'):
        print(line)

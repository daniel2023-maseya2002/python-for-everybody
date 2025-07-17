fh = open('DANIEL MASEYA MUBU.txt',  encoding='utf-8')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.lower())

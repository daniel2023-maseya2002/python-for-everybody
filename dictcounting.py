#dan = dict()
#dan['csev'] = 1
#dan['cwen'] = 1
#print(dan)
#dan['cwen'] = dan['cwen'] + 1
#print(dan)

# Counting
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names :
    #if name not in counts :
        #counts[name] = 1
    #else:
        #counts[name] = counts[name] + 1
#print(counts)

# Simplified Counting with get()
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

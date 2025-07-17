a = [0, 2, 4]
b = [1, 3, 5]
c = a + b
print(c)

t = [9, 41, 12, 3, 74, 15]
print(t)
x = t[1:3]
print(x)
y = t[:4]
print(y)
z = t[3:]
print(z)
w = t[:]
print(w)

# create an empty list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Is something in a List?

9 in t
15 in t
20 in t

# Sort the values
t.sort()
print(t)
print(t[1])


# Function in list

print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t)/len(t))

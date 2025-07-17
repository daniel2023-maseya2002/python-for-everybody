# Counting in a Loop
zork = 0
print('Before', zork)
for thing in [9, 42, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Summing in a Loop
zork = 0
print('Before', zork)
for thing in [9, 42, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

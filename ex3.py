sh = input('Enter Hours: ')
sr = input('Enter Rate: ')
fh = float(sh)
fr = float(sr)

#print (fr, fh)
if fh > 40:
    #print("Overtime")
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    print(reg,otp)
    xp = reg + otp
else:
    #print("Regulartime")
    print("Regulartime")
    xp = fh * fr
print("Pay: ", xp)

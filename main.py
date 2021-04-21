s = input()
s1 = s[0:3]
s2 = int(s[3:])

if s1 == "021" and s2 % 2 == 0:
    print("yes")
else:
    print("no")

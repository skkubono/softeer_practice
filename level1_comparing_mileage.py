import sys
now = str(input()).split()
a = int(now[0])
b = int(now[1])
if a>b:
    print('A')
elif b>a:
    print('B')
else:
    print('same')
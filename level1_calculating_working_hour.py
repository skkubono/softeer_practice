import sys
a =0
for i in range(5):
    HH, MM = map(str, input().split())
    time_h = int(MM[0:2]) - int(HH[0:2])
    time_m = int(MM[3:]) - int(HH[3:])
    
    a += time_m+time_h*60
print(a)
    
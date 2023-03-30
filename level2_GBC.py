import sys
from collections import deque
n, m = map(int, input().split())
ip = [list(map(int, input().split())) for _ in range(n)]
np = [list(map(int, input().split())) for _ in range(m)]
ip= deque(ip)
np= deque(np)
vel_max = 0

def vel_diff(q,w):
    if q>=w:
        return 0
    else:
        return w-q     

while ip:
    # print('heheheheh')
    a = ip.popleft()
    b = np.popleft()
    if a[0] > b[0]:
        rem_a = a[0]-b[0]
        if vel_max <= vel_diff(a[1],b[1]):
            vel_max = vel_diff(a[1],b[1])
        a[0] = rem_a
        ip.appendleft(a)
    elif a[0] < b[0]:
        rem_b = b[0]-a[0]
        if vel_max <= vel_diff(a[1],b[1]):
            vel_max = vel_diff(a[1],b[1])
        b[0] = rem_b
        np.appendleft(b)
    elif a[0] == b[0]:
        if vel_max <= vel_diff(a[1],b[1]):
            vel_max = vel_diff(a[1],b[1])
    # print("ip : ",ip)
    # print("np : ",np)
    # print('----------')
print(vel_max)
        


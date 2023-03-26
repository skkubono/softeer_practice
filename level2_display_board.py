T = int(input())
test = {'1':[0,1,1,0,0,0,0],
        '2':[1,0,1,1,0,1,1],
        '3':[1,1,1,1,0,0,1],
        '4':[0,1,1,0,1,0,1],
        '5':[1,1,0,1,1,0,1],
        '6':[1,1,0,1,1,1,1],
        '7':[0,1,1,1,1,0,0],
        '8':[1,1,1,1,1,1,1],
        '9':[1,1,1,1,1,0,1],
        ' ':[0,0,0,0,0,0,0],
        '0':[1,1,1,1,1,1,0]
        }
def Compare(a,b):
    cnt=0
    for i in range(7):
        if a[i] != b[i]:
            cnt +=1
    return cnt

for i in range(T):
    a,b = (map(str, input().split()))
    a = (5-len(a))*' '+a
    b = (5-len(b))*' '+b
    
    Tcnt =0
    for i in range(5):
        Tcnt+=Compare(test[a[i]],test[b[i]])
    print(Tcnt)
    
# print('cnt:',cnt)
# print(sum(test['1'] test['2']))
import sys
m,n,k = map(int, input().split())
man = list(map(int, input().split()))
usr = list(map(int, input().split()))

flag = False
def is_true(a,b):
    if a == b:
        return True
    else:
        return False
    
if n < m:
    print('normal')
else:
    for i in range(len(usr)):
        flag = is_true(man[0], usr[i]) # flag값 반환해줌
        # print(' i :',i)
        if flag == True: # manu 첫값이랑 usr입력값 같을경우에 돌림
            cnt =0
            for j in range(m):
                if i+m > n:
                    print('normal')
                    break
                if man[j] == usr[i+j]:
                    cnt+=1
                else:
                    continue
            if cnt == m:
                print('secret')
                break
        if i==(n-m):
            print('normal')
            break
    
                
        
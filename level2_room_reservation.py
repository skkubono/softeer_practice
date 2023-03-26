# N = 회의실 이름
# M = 회의실의 이름 r, 시작시간 s, 종료시각 t

N, M = map(int, input().split())
dic ={}
for i in range(N):
    a = str(input())
    dic[a]=[0,0,0,0,0,0,0,0,0]

reference_keys = sorted(dic.keys())

for k in range(M):
    r,s,t = map(str, input().split())
    for j in range(int(s)-9,int(t)-9):
        dic[r][j]=1

# dic ={'avante':[1,1,1,1,1,1,0,0,0],
#       'santafe':[0,1,1,0,0,0,1,1,1],
#       'grandeur':[0,1,0,1,0,1,0,1,0]}
# dic ={'grandeur':[0,1,0,1,0,1,0,1,0]}
# reference_keys = sorted(dic.keys())
# print('reference_keys:',reference_keys)
cnt = 0
flag = False
for key in reference_keys:
    cnt+=1
    temp0 = []
    temp1 = []
    print("Room %s:"%key)
    if dic[key][0]==0:
        temp0.append("09")
        flag = True
    else: flag = False
    
    for i in range(8): 
        if flag == True and dic[key][i+1] == 1:
            temp1.append(i+10)
            flag = False 
            
        elif flag == True and dic[key][i+1] == 0:
            flag = True
            if i == 7:
                temp1.append(i+11)
            
        elif flag == False and dic[key][i+1] == 1:
            flag = False
        
        elif flag ==False and dic[key][i+1] ==0:
            flag = True
            temp0.append(i+10)
            if i==7:
                temp1.append(i+11)
            
        else:
            continue
    if len(temp0)==0 and len(temp1)==0:
        print("Not available")

    else:
        print("%d available:" %len(temp0))
        for l in range(len(temp0)):

            print("%s-%s"%(temp0[l],temp1[l]))
    if cnt < len(reference_keys):
        print("-----")    
                    
        

            
            

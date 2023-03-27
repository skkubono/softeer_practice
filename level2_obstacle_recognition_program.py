import random

map_size = int(input())
map_list = []
for i in range(map_size):
    map_list.append(list(map(int, input())))

def update_map(start,map_input):
    max_x, max_y = len(map_input[0])-1, len(map_input)-1
    queue = [start]
    cnt=1
    map_input[start[1]][start[0]]=2
    while queue != []:
        # print(start)
        
        x, y = queue.pop(0)
        if y!=0 and map_input[y-1][x] ==1: 
            queue.append([x,y-1])
            map_input[y-1][x] = 2
            cnt+=1
        if y!=max_y and map_input[y+1][x]==1: 
            queue.append([x,y+1])
            map_input[y+1][x] = 2
            cnt+=1
        if x!=0 and map_input[y][x-1] ==1: 
            queue.append([x-1,y])
            map_input[y][x-1] = 2
            cnt+=1
        if x!=max_x and map_input[y][x+1]==1: 
            queue.append([x+1,y])
            map_input[y][x+1] = 2
            cnt+=1
        # print('queue : ',queue)
        # print(cnt)
        
    return map_input, cnt

ans = 0
cluster_list = []
for i in range(len(map_list)): # map list 세로 탐색
    for j in range(len(map_list[i])): #map list 가로 탐색
        if map_list[i][j] == 1: 
            ans +=1
            # print("ans : ",ans, [i,j])
            map_list, count = update_map([j,i],map_list)
            cluster_list.append(count)
            # print(map_list)
            
print(ans)
cluster_list.sort()
for i in range(len(cluster_list)):
    print(cluster_list[i])

    

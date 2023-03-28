from collections import deque
# map_list =  [[1,1,1,0,1,1,1], 
#              [0,1,1,0,1,0,1], 
#              [0,1,1,0,1,0,1], 
#              [0,0,0,0,1,0,0], 
#              [0,1,1,0,0,0,0], 
#              [0,1,1,1,1,1,0], 
#              [0,1,1,0,0,0,0]]
# m_size = 7


m_size = int(input())
map_list = []

for i in range(m_size):
    map_list.append(list(map(int, input()))) #map 받기

dx = [0,0,1,-1]
dy = [1,-1,0,0]

visited = [[False]*m_size for i in range(m_size)]
# print('visited :', visited)
def in_map(x,y,m_size):
    if x < 0 or y < 0 or x > m_size-1 or y>m_size-1:
        return False
    else:
        return True
    
def dfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[y][x] = True 
    while queue:
        global cnt
        x,y = queue.popleft()
        # print('x , y :', x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if in_map(nx,ny,m_size) == True and visited[ny][nx] == False and map_list[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append([nx,ny])
                cnt+=1
                
                
cl_num=0    
p_list = []
for j in range(m_size):
    for k in range(m_size):
        if map_list[j][k] == 1 and visited[j][k] == False:
            cnt=1                 
            dfs(k,j)
            cl_num+=1
            p_list.append(cnt)
        
            
# print(map_list)  
# print(' p_list :',p_list)          
# 최종 프린트
print(cl_num)
p_list.sort()
for i in p_list:
    print(i)
    
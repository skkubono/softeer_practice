import sys
k, p, n = map(int, input().split())
l = 1000000007
# k=10007
# p=1000006
# n=17
# first = k
# flag = False
# print('k p n :',(k*p*n)%l)
# for i in range(n):
#     if first<l and flag == False:
#         first *=p
#         if first>l:
#             flag=True
#             continue
        
#     elif flag ==True:
#         first = (first * p) % n
for i in range(n):
    k = (k * p) %l
        
        
print(k)

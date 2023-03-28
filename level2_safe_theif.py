from heapq import*
W, N = map(int, input().split()) # W는 배낭무게 N은 귀금속종류
# W, N = 100, 2
# 비싼것 기억한 후 제일 먼저 쳐넣고 그다음 나머지 무게만큼 비싼거를 쳐넣음
# 무게 총합이 W이상이 될 것 같으면 

price = 0
hq =[]
for i in range(N):
    aa= list(map(int, input().split()))
    hq.append(aa)
hq.sort(key = lambda x: x[1], reverse = True)
for m, p in hq:

    if W >= m:
        price += m*p
        W -= m
    else:
        price += W*p
        break
print(price)



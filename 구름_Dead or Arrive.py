import sys
input = sys.stdin.readline

n = int(input())
car = {}
res = [0 for i in range(1000)]

for i in range(1,n+1):
	v,w = map(int,input().split())
	if v not in car:
		car[v] = w
		res[v-1] = i 
	else :
		if car[v] <= w :
			car[v] = w
			res[v-1] = i
print(sum(res))

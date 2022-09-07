N=int(input())
pilist = input().split(" ") 
for i in range(0,len(pilist)):
    pilist[i] = int(pilist[i])
pilist.sort() # 문자열정렬과 숫자 정렬 다름!!!!!!!!!! 절대 주의 
add=0
for i in range(0,len(pilist)):
    add += sum(pilist[0:i+1])
print(add)

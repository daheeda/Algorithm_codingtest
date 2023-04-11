sent = input().split("-")

#값이 최소가 되려면 -> +를 -로 바꿔야 함.

for i in range(0,len(sent)):
    temp=[]
    if sent[i].count("+") > 0 :
        temp = sent[i].split("+")
        cal=0
        for j in range(0,len(temp)):
            cal += int(temp[j])
        sent[i]=cal
                
    
sum=int(sent[0])
for i in range(1,len(sent)):
    sum -= int(sent[i])
print(sum)

arr=[i for i in range(1,10000)]
arr2=[i for i in range(1,10000)]

for i in range(0,99): ## 인덱스 확인!!!!!!!
    try :
        arr2.remove(arr[i]+arr[i]//10+arr[i]%10)
    except :
        continue
        
for i in range(99,999):
    try:
        arr2.remove(arr[i]+arr[i]//100+arr[i]%100//10+arr[i]%100%10)
    except:
        continue
        
for i in range(999,9999):
    try :
        arr2.remove(arr[i]+arr[i]//1000+arr[i]%1000//100+arr[i]%1000%100//10+arr[i]%1000%100%10)
    except:
        continue
        
for i in range(0,len(arr2)):
    print(arr2[i])

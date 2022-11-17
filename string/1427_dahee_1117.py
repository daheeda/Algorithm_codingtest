a=list(map(int,input()))
a.sort(reverse=True)
a=str(a).replace(" ",'')
a=a.replace(",",'')
a=a.replace("[",'')
a=a.replace("]",'')
print(a)

'''
print(''.join(sorted(input())[::-1]))
'''

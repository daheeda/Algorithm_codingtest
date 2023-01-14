def solution(s):
    answer = len(s)
    for i in range(1,len(s)):
        ftemp = s[0:0+i]
        ptemp = ''
        temp2 = ''
        pk=1
        fk=1
        for j in range(1,int(len(s)/i+0.5)+2):
            add = s[j*i:j*i+i]
            fk+=1
            if ftemp == add :
                pk+=1
                ptemp = add
            if fk != pk:
                if pk == 1:
                    temp2 += ftemp
                else :
                    temp2 += str(pk)+ptemp
                ftemp = s[j*i:j*i+i]
                ptemp = ''
                pk=1
                fk=1
        if answer > len(temp2):
            answer = len(temp2)
    return answer

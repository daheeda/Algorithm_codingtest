def solution(new_id):
    # step 1 : 소문자 치환
    new_id=new_id.lower()
    # step 2 : 문자제거
    string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
             'r','s','t','u','v','w','r','x','y','z','-','_','.','1','2','3','4',
             '5','6','7','8','9','0']
    idstep2=''
    for i in new_id :
        if i in string :
            idstep2 += i
    # step 3 : .제거
    while idstep2.count('..') > 0 :
        idstep2=idstep2.replace('..','.')
    # step 4 : . 제거
    if idstep2[0] == '.' :
        idstep2 = idstep2[1:]
    if len(idstep2) > 0 :
        if idstep2[-1] == '.' :
            idstep2 = idstep2[:-1]
    # step 5 : 빈문자열인경우
    if idstep2 == '' :
        idstep2 = 'a'
    # step 6 : 길이
    if len(idstep2) > 15 :
        idstep2 = idstep2[:15]
    if idstep2[-1] == '.' :
        idstep2 = idstep2[:-1]
    # step 7 : 길이
    if len(idstep2) < 3 :
        while len(idstep2) < 3 :
            idstep2+=idstep2[-1]  
    return idstep2

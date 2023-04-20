def solution(phone_book):
    div = []
    for ph in phone_book :
        div.append(len(ph))
    div = set(div)
    dic = {}
    for phnum in phone_book:
        for divv in div :
            if len(phnum) >= divv :
                dic_p = len(dic)
                dic[hash(phnum[:divv])] = phnum[:divv]
                dic_c = len(dic)
                if dic_p == dic_c : # 추가 안된경우
                    if phone_book.count(phnum[:divv]) == 0 : # 접두어 아닌데 추가 안된경우
                        continue
                    else : return False
    return True

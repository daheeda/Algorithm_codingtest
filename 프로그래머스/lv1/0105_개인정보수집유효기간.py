def solution(today, terms, privacies):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    answer = []
    value = 0
    ndatemonth=''
    ndateday=''
    for k in range(0,len(privacies)):
        date, ptype = privacies[k].split(" ")
        for i in range(0,len(terms)):
            ttype, month = terms[i].split(" ")
            if ptype == ttype :
                value = int(month)
        ndate = datetime.strptime(date, '%Y.%m.%d')+relativedelta(months=value)
        if ndate.month < 10 :
            ndatemonth = "0"+str(ndate.month)
        else :
            ndatemonth = str(ndate.month)
        if ndate.day < 10 :
            ndateday = "0"+str(ndate.day)
        else :
            ndateday = str(ndate.day)
        ndate1 = str(ndate.year) + ndatemonth + ndateday
        if int(ndate1) - int(today.replace(".",'')) <= 0 :
            answer.append(k+1)
    return answer

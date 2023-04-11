def solution(id_list, report, k):
    report = set(report) 
    report = list(report)
    mail = { id :0 for id in id_list}
    idtmp = { id : [''] for id in id_list}
    for id in report :
        name1=id.split(" ")[0]
        name2=id.split(" ")[1]
        idtmp[name2].append(name1)
    for id in id_list:
        if len(idtmp[id]) > k :
            for i in range(1,len(idtmp[id])):
                userid=idtmp[id][i]
                mail[userid] += 1
    answer = []
    for id in id_list :
        answer.append(mail[id])
    return answer

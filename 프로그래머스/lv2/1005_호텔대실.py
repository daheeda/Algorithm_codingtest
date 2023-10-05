def solution(book_time):
    answer = 0
    time_table = [0]*24*60 

    for i in range(len(book_time)):
        start = book_time[i][0].split(':')
        start = int(start[0])*60 + int(start[1])
        end = book_time[i][1].split(':')
        end = int(end[0])*60 + int(end[1])
        time_table[start:end+10] = [x + 1 for x in time_table[start:end+10]]
    
    return max(time_table)

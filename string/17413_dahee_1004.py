s = input()
s = s+" "

save = []

while len(s) > 0 :
    if s.count('<') > 0 :
        stidx = s.index('<')
        enidx = s.index('>')
    else :
        stidx = 0
        enidx = s.index(' ')
    if stidx != 0 :
        save += s[0:stidx].split(' ')
    save.append(s[stidx:enidx+1])
    s = s[enidx+1:]

res = '>'
for word in save:
    if word.count('<') > 0 :
        res += word
    else :
        tmp = ''
        word = word.replace(' ','')
        for i in word:
            tmp = i + tmp
        if res[-1] != '>':
            res += ' '
        res += tmp
        
print(res[1:])


'''

s = input().replace('<', 'X<').replace('>', '>X')
tag_str = [t for t in s.split('X') if t]
word[::-1]

'''

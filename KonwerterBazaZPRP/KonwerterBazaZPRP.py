import re
import sqlite3
f = open("C:\\Users\\Marshal\\Downloads\\KATALOG1.txt","r")

str = f.read();
str = re.sub("\n"," ",str)

regex_pytania = r"[abcdefghi]\).*?(?=([abcdefghi]\))|((([RSZ]{3}\.\d)|(\d+\.\d+)) [^xm].*?(?=a\))))"
pytania = tuple(re.findall(regex_pytania, str, flags=re.MULTILINE|re.DOTALL))
pytania_filtered = [];

for i in range(0,len(pytania)):
    for j in range(0,len(pytania[i])):
        if len(pytania[i][j]) > 5:
            pytania_filtered.append(pytania[i][j][:-1]) 

doWsadzenia = str[:59]

pytania_filtered.insert(0,doWsadzenia[:-1])


print(pytania_filtered[0])

###############################   ODPOWIEDZI   ###############################

f = open("C:\\Users\\Marshal\\Downloads\\odpowiedzi.txt","r",encoding="utf-8")

lines = tuple( f.readlines())
odpowiedzi = []

for line in lines:
    if len(line) > 5:
        odpowiedzi.append(re.sub("\n"," ",line))
        
f.close()

q = open("C:\\Users\\Marshal\\Downloads\\sql_insert.txt","+w")

q.write('INSERT INTO `questions` (`id`,`number`,`question`,`ansA`,`ansB`,`ansC`,`ansD`,`ansE`,`ansF`,`ansG`,`ansH`,`ansI`) VALUES ')

licznik = 0

for i in range(len(pytania_filtered)):
    q.write( '(\''+"{}".format(i)+'\',\''+pytania_filtered[i].split(" ",1)[0]+'\',\''+pytania_filtered[i].split(" ",1)[1]+'\'')
    for ans in range(9):
        if ans == 0:
            q.write(',\''+odpowiedzi[licznik][:-1]+'\'')
            licznik += 1
        elif odpowiedzi[licznik].startswith('a)') or licznik>1871  :
            q.write(',\'\'')
        else:
            q.write(',\''+odpowiedzi[licznik][:-1]+'\'')
            licznik += 1
    q.write('),')

print(q.read(1000))

q.close()

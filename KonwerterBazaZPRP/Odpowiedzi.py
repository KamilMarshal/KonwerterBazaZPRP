#encode utf-8
#plik tymczasowy

import re
f = open("C:\\Users\\Marshal\\Downloads\\odpowiedzi.txt","r",encoding="utf-8")

lines = tuple( f.readlines())
odpowiedzi = []

for line in lines:
    if len(line) > 5:
        odpowiedzi.append(line[:-1])
        



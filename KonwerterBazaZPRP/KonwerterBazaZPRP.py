from ctypes import pythonapi
import re
f = open("C:\\Users\\Marshal\\Downloads\\KATALOG1.txt","r")
#print(f.read(3250))

str = f.read();

# "(\d+\.\d+))|(([RSZ]{3}\.\d) [^xm].*?(?=a\))"gms   - tylko pytania
# https://regex101.com/r/QVBlxq/1

# "[abcdefghi]\).*?(?=([abcdefghi]\))|((([RSZ]{3}\.\d)|(\d+\.\d+)) [^xm].*?(?=a\))))"gms - tylko odpowiedzi




regex_pytania = r"[abcdefghi]\).*?(?=([abcdefghi]\))|((([RSZ]{3}\.\d)|(\d+\.\d+)) [^xm].*?(?=a\))))"
pytania = tuple(re.findall(regex_pytania, str, flags=re.MULTILINE|re.DOTALL))


for i in range(0,len(pytania)):
    for j in range(0,len(pytania[i])):
        if len(pytania[i][j]) > 5:
            print(pytania[i][j])
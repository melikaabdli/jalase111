#لیستی با 10 عدد صحیح رندوم بعد لیست دو قسمت زوج و فرد بشه
import random 
r = []
for i in range(10):
    m =random.randint(1,1000)
    r.append(m)
    
print(r)

zoj = []
fard = []
for number in r:
    if number%2 == 0:
        zoj.append(number)
    else:
        fard.append(number)
    
print(zoj)
print(fard)

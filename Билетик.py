n = input()
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2: 
   number = True
else:
    number = False
lucky = ("Обычный","Счастливый")[number]
print('Билетик', lucky, n[0],"+",n[1],"+",n[2],"=",n[3],"+",n[4],"+",n[5],";",s1,"=",s2)
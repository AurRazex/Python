ns = sorted(set(input().split()) & set(input().split()), key=int)
if ns != []:
   print(" ".join( str(e) for e in ns ))
else:
    print('Повторяющихся чисел нет')
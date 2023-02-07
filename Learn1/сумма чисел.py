num = int(input())
x = [int(a) for a in str(num)]
x[:]

print(sum(x), ("+".join(str(num))))
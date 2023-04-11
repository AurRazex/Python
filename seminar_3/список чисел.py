A = [int(i) for i in input().split()] 
X = int(input())
b = A.count(X)
v = b > 0
print(b if v else "-1")
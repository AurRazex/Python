A = [float(i) for i in input().split()] 
X = float(input())
def nearest_value(A, X):
    found = A[0]
    for item in A:
        if abs(item - X) < abs(found - X):
            found = item
    return found
print(f'Ближайшее число к {X} в списке {A} является {nearest_value(A, X)}')
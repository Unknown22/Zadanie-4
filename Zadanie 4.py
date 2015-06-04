def absDistinct(A):
    x = 0
    list = []
    for i in A:
        list.append(abs(i))
    list = set(list)
    for i in list:
        x += 1
    return x

#Wynik dla tej tablicy powinien wyniesc: 4
A = [-2147483648, -2147483647, -2, 1, 2, 2147483647]
print absDistinct(A)

#Tablica z PDFa - zgodnie z danymi w zadaniu zwraca 5
A = [-5, -3, -1, 0, 3, 6]
print absDistinct(A)
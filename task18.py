N = int(input ("Введите длину массива: ", ))
print (N)
arr = list ()
for i in range (N):
    arr.append (int(input ("Введите элемент массива: ", )))
x = int(input ("Введите элемент для сравнения: ", ))
min = arr [0]
for i in range (1,N):
    if abs(arr[i]-x) < abs (x-min):
        min = arr [i]
print (min)
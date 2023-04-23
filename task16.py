N = int(input ("Введите длину массива: ", ))
print (N)
arr = list ()
counter = 0
for i in range (N):
    arr.append (int(input ("Введите элемент массива: ", )))
x = int(input ("Введите элемент для поиска: ", ))
for i in range (N):
    if arr[i] == x:
        counter+=1
print (counter)

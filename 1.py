#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

a, b = 1,1


fibonacci_seri = [a, b]

for i in range(18):

    a, b = b, a + b
    fibonacci_seri.append(b)

print(fibonacci_seri)

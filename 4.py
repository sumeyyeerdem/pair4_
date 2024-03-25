#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.


sayi = int(input("Sayi giriniz:"))
asalmi = 0  #eğer kalan 0 ise girilen sayı asal sayı değldir.

for i in range (2,sayi):  # i değeri her döngüde 2 ve kullanıcının girdiği sayı arasındaki değerleri sırayla alacak.  2 yazmanın nedeni: asal sayılar 1 den ve kendisinden başka sayıya bölünmediği için 1'i dışarda bırakmamız lazım.
                           # ikinci değer yani son değer döngünün dışında oluyor. örn sayı= 9 i=8 olur yani döngü dışı kalır.
   
    if sayi%i == 0:  #sayi bölü i nin kalanı 0 'a eşit mi?  %: sayıyı bölüp kalanı alır.
      asalmi += 1  #eğer sayı asal değilse değişkenin değerini 1 arttır. Sonda eğer asalmi değişkeninin değeri 0 kaldıysa girilen sayı asal.
      break
   

if asalmi == 0:
      print(sayi, "sayisi asaldir.")
else: 
      print(sayi, "sayisi asal değildir.")
      
"""
P.S: Program çalıştıktan sonra eğer 'asalmi' değişkeninin değeri 0 kaldıysa girilen sayı asaldır, eğer 'asalmi' değişkenin değeri 1 olursa girilen sayı asal değildir . 

'asalmi'değişkeninin değerini kullanıcının girdiği sayı kendisinden ve 1'den başka sayıya tam bölündüğünde değiştiriyoruz.

"""



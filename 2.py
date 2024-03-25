#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

def mukemmel_mi(sayi):

    toplam = 0
    # 1'den sayıya kadar mesela 6 dersek 1/2/3/4/5 oluyor tüm sayılar için döngü başlatıyor.
    for i in range(1, sayi):
        # Eğer sayı, i'ye tam bölünüyorsa, i'yi toplama ekle 
        if sayi % i == 0:
            toplam += i
    # Toplam, başlangıçta verilen sayıya eşitse, sayı mükemmeldir mesela 6 seçilirse 1/2/3 bölünüyor ve toplarsak 6 olur kendisine eşit.
    if toplam == sayi:
        return True
    else:
        return False


sayi = int(input("Bir sayi girin: "))


if mukemmel_mi(sayi):
    print(f"{sayi} mükemmel bir sayidir.")
else:
    print(f"{sayi} mükemmel bir sayi değildir.")

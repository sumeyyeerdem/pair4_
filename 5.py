#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

def asal_carpanlari_bul(sayi): #(kullanıcı sayı değişkenine sayı girer)
    carpanlar = [] #(asal çarpanları tutmak için çarpanlar boş listesi)
    i = 2 #(döngü 2 den başar artan pozitif tam sayılarla devam eder)
    while i <= sayi: #(i , sayının değirinden küçük ve eşitse çalışır)
        if sayi % i == 0: #(burada ki % ifadesi sayının i ye bölümünden kalanı verir)
            carpanlar.append(i)
            sayi //= i   #(//= tam sayılı bölme anlamına geliyor)
        else:
            i += 1 #(eğer kalan sayı farklı iste i değeri artar ve işlem tekrarlanır)

    return carpanlar #(asla çarpanlar çarpanlar listesine geri döner)


sayi = int(input("Bir sayi girin: "))

print(f"{sayi}'nin asal çarpanlari:", asal_carpanlari_bul(sayi))



print("***** HESAP MAKİNESİ PROGRAMINA HOŞ GELDİNİZ*****")
print("***İşlemler***")
print("1. Toplam\n2.Çıkarma\n3.Bölme\n4.Çarpma\n***************")

sayı1= int(input("Birinci sayıyı giriniz:"))
sayı2 = int(input("İkinci sayıyı giriniz:"))

islem = input("İşlem numarası giriniz:")

if (islem == "1"):
    print("{} ile {} toplamı = {}".format(sayı1, sayı2, sayı1 + sayı2))

elif (islem == "2"):
    print("{} ile {} farkı = {}".format(sayı1, sayı2, sayı1 - sayı2))

elif (islem == "3"):
    print("{} 'nın {} 'e bölümü {} dır.".format(sayı1, sayı2, sayı1 / sayı2))

elif (islem == "4"):
    print("{} ile {} çarpımı = {}".format(sayı1, sayı2, sayı2 * sayı1))

else:
    print("Geçersiz işlem")
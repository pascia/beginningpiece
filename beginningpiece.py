import time
import random
from secrets import choice
def toplama(x, y):
    return x + y
def cikarma(x, y):
    return x - y
def  bölme(x, y):
    return x / y
def carpma(x, y):
    return x * y
while True:
    print("                                                                        Öncelikle hoş geldiniz, bir fonksiyon seçiniz.")
    print("          1. Hesap Makinesi 2. Ters çeviri 3. Rakam Bulma Oyunu 4. Bahtsız bedevi 5. Random şifre oluşturucu 6. 0'dan başlayarak belirtilen aralığı bulma 7. bir sayı içerisindeki sayıları bulma ve sıralama")
    fonksiyon = input("Seçiniz:")
    if  fonksiyon == '1':
        print (" ne vereyim abime elimizde bunlar var:")
        time.sleep(0.5)
        print ("1. Toplama")
        print ("2. Çıkarma")
        print ("3. Bölme")
        print ("4. Çarpma")
        print("Çık yazarak hesap makinesinden çıkabilirsiniz.")
        l = choice= (input("Çıkış yapmak istiyor musunuz: "))
        while not l == "Çık"  :
            l = choice= (input("Bir  işlem seçiniz/ ya da Çık yazınız: "))
            if choice == "Çık":
                print("Çıkış yapılıyor...")
                time.sleep(1)
                break
            num1 = float(input(" İlk sayı: "))
            num2 = float(input(" İkinci sayı: "))

            if choice == '1':
                print(toplama(num1, num2))
            elif choice == '2':
                print(cikarma(num1, num2))
            elif choice == '3':
                print(bölme(num1, num2))
            elif choice == "4":
                print (carpma(num1, num2))      
            else:
                print("bir şeyler sıkıntılı sanırım he.")
    elif fonksiyon == '2':
        print("Bir kelime, cümle veya sayı söyleyiniz tersini size gösterelim.")
        time.sleep(1)
        print("Çıkmak istiyorsanız, Çık yazınız.")
        while True:
            a = (input("Giriniz: "))
            if a == "Çık":
                print("Çıkış yapılıyor...")
                time.sleep(1)
                break
            else:
                b = a[::-1]
                print(a+ " tersi şudur: " +b)
    elif fonksiyon == '3':
        a = random.randint(0,9)
        sans = 0
        print("bil bakalım yiğidim bu şanslı rakam ne?")
        while sans < 11:
            b = int(input())
            sans = sans + 1
            if b == a:
                print("helal lan buldun.")
                time.sleep(1)
                break
            else:
                print("tekrar dene len.") 
    elif fonksiyon == '4':
        num = (input("gir bakam sayıyı: "))
        res = [int(x) for x in str(num)] 
        a = choice(res)
        b = choice(res)
        while True:
            if a > 5:
                print("bahtlı bedevi!")
                time.sleep(1)
                break
            else:
                    print("bahtsız bedevi.")
                    time.sleep(1)
                    break
    elif fonksiyon == '5':
        n = int(input("Şifreniz kaç haneden oluşsun? "))
        password = str(random.randint(0, (10**n)-1))
        print("Şifreniz: " + password.zfill(n))
    elif fonksiyon == '6':
        while True:
            print("Aralığın sonunu belirleyiniz:")
            n = int(input())
            time.sleep(0.5)
            print("Artanı belirleyen sayıyı giriniz:")
            a = list(range (0,n))
            b = int(input())
            c = a[::b]
            time.sleep(0.5)
            print(c)
            break
    elif fonksiyon == '7':
        while True:
            a = list(dict.fromkeys([int(i) for i in str(int(input("Lütfen bir sayı giriniz: ")))]))
            a.sort() 
            print("Sonuç:", a)
            time.sleep(1)
            break

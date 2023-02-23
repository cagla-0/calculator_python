while True :
    sayi1 = int(input("ilk sayiyi giriniz:"))
    islem = input("operatoru giriniz:")
    sayi2 = int(input("ikinci sayiyi giriniz:"))

    toplama = sayi1 + sayi2
    cikarma = sayi1 - sayi2
    carpma = sayi1 * sayi2
    bolme = sayi1 / sayi2

    print("Sonucunuz :")

    if islem == "+" :
        print(toplama)
    elif islem == "-" :
        print(cikarma)
    elif islem == "*" :
        print(carpma)
    elif islem == "/" :
        print(bolme)
    else :
        print("yanlis ifade girdiniz")




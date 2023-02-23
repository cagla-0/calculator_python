while True :
    sayi1 = int(input("ilk sayiyi giriniz:"))
    islem = input("operatoru giriniz:")
    sayi2 = int(input("ikinci sayiyi giriniz:"))

    def topla(x,y) :
        return x+y
    def cikar(x,y) :
        return x-y
    def carp(x,y) :
        return x*y
    def bol(x,y) :
        return x/y

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
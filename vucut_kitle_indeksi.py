while True:
    agirlik = float(input("Ağırlığınızı giriniz: "))
    boy = int(input("Boyunuzu giriniz: "))

    indeks = (agirlik / (boy/100)**2)

    if indeks <= 18.5 :
        print("zayıf")
    elif indeks >= 18.5 and indeks <= 24.9 :
        print("normal")
    elif indeks >= 25 and indeks <= 29.9 :
        print("kilolu")
    elif indeks >= 30 and indeks <= 34.9 :
        print("obez")
    elif indeks >= 35 :
        print("morbid obez")
    else :
        print("diyetisyene danışınız")

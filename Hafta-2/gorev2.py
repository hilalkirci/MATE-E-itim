def indirim_hesapla():
    fiyat = float(input("ürün fiyatını giriniz: "))
    indirim = float(input("indirim yüzdesini giriniz: "))

    indirim_tutari = fiyat * indirim / 100
    son_fiyat = fiyat-indirim_tutari

    print("indirim tutarı:", indirim_tutari, "TL")
    print("indirimli fiyat:", son_fiyat, "TL")
indirim_hesapla()
def harf_notu_hesapla():
    vize= float(input("vize notunu giriniz:"))
    final= float(input("final notunu giriniz:"))

    ortalama= (vize*0.40) + (final*0.60)

    print("ortalamanız:", ortalama)

    if ortalama>=90:
        print("harf notunuz: AA")
    elif ortalama>=85:
        print("harf notunuz:BA")
    elif ortalama>=80:
        print("harf notunuz:BB")
    elif ortalama>=75:
        print("harf notunuz:CB")
    elif ortalama>=70:
        print("harf notunuz:CC")
    elif ortalama>=65:
        print("harf notunuz:DC")
    elif ortalama>=60:
        print("harf notunuz:DD")
    elif ortalama>=50:
        print("harf notunuz:FD")
    else:
        print("harf notunuz:FF")

harf_notu_hesapla()
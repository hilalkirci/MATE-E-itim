dogum_yili=int(input("dogum yilinizi giriniz:"))
yas=2026 - dogum_yili
print("yasiniz:", yas)
if yas>=18:
    print("ehliyet alabilirsiniz.")
else:
    print("ehliyet alamazsiniz.")
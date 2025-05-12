
print("\033[1;32;40m")
print("   ╔════════════════╗")
print("   ║  hesap makines ║")
print("   ║                ║")
print("   ║1)toplama       ║")
print("   ║2)çikarma       ║")
print("   ║3)çarpma        ║")
print("   ║4)bölme         ║")
print("   ╚════════════════╝")


def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Bir sayıyı sıfıra bölemezsiniz!"
    return x / y

secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print(f"{sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
elif secim == '2':
    print(f"{sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
elif secim == '3':
    print(f"{sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
elif secim == '4':
    print(f"{sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")
else:
    print("Geçersiz seçim!")
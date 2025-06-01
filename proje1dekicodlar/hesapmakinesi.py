def hesapp():  

  print("\033[1;22;40m")
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
      return "Sıfıra bölme hatası!"
    return x / y
  while True:
    secim = input("Seçiminizi (1/2/3/4): ")

    if secim in ('1', '2', '3', '4'):
      sayi1 = float(input("İlk sayıyı girin: "))
      sayi2 = float(input("İkinci sayıyı girin: "))

      if secim == '1':
        print(sayi1, "+", sayi2, "=", toplama(sayi1, sayi2))
      elif secim == '2':
        print(sayi1, "-", sayi2, "=", cikarma(sayi1, sayi2))
      elif secim == '3':
        print(sayi1, "*", sayi2, "=", carpma(sayi1, sayi2))
      elif secim == '4':
        print(sayi1, "/", sayi2, "=", bolme(sayi1, sayi2))
      
      devam_et = input("Başka bir işlem yapmak ister misiniz? (evet/hayır): ")
      if devam_et.lower() != 'evet':
        break
    else:
      print("Geçersiz giriş. Lütfen 1, 2, 3 veya 4'ü seçin.")
def anammenü():
   print("\033[1;22;40m")
   print("   ╔═══════════════════╗")
   print("   ║     arayüz        ║")
   print("   ║                   ║")
   print("   ║1)oyunlar          ║")
   print("   ║2)oyun sitesı      ║")
   print("   ║3)hesap mankinesi  ║")
   print("   ║4)edit uygulamsı   ║")
   print("   ║5)internet tarayacı║")
   print("   ║6)çıkış yap        ║")
   print("   ╚═══════════════════╝")
   
   secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5/6): ")
   if secim == "1":
      print(f"oyunlar açılıyor")
      import oyunlardenemesi2
      oyunlardenemesi2.oyunmenü()
   if secim == "2":
      print(f"oyun sitesi açılıyor")
      import oyunsitesi
      oyunsitesi.oyunugulamsi()
   if secim == "3":
      print(f"hesap makinesi açılıyor")
      import hesapmakinesi 
      hesapmakinesi.hesapp()   
   if secim == "4":
      print(f"edit ugulamsı açılıyor") 
      import sosyalmedya
      sosyalmedya.sosyall()  
   if secim == "5":
      print("internet tarayacı açılıyor")
      import pcugulama
      pcugulama.pc()   
   else:
      print("Geçersiz giriş. Lütfen 1, 2, 3, 4, 5,  veya 6 girin.")
   anammenü()   
anammenü()
def oyunmenü():
   print("\033[1;22;40m")
   print("   ╔══════════════════════╗")
   print("   ║  oyun uglama         ║")
   print("   ║                      ║")
   print("   ║1)Counter-Strike 2    ║")
   print("   ║2)Fornite             ║")
   print("   ║3BattleBit Remastered ║")
   print("   ║4)aimlabs             ║")
   print("   ║5)CurseForge          ║")
   print("   ║6)The Forest          ║")
   print("   ║7)geri                ║")
   print("   ╚══════════════════════╝")
   secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5/6/7):")
   if secim == "1":
      print(f"Counter-Strike 2 açılıyor") 
   if secim == "2": 
      print(f"Fornite açılıyor") 
   if secim == "3":
      print(f"BattleBit Remastered açılıyor")  
   if secim == "4":
      print(f")Aimlabs açılıyor")
   if secim == "5":
      print(f"Curseforge açılıyor")      
   if secim== "6":
      print(f"The forest açılıoyr")
   if secim== "7":
      print(f"geriye dönülüyor")
   else:
      print("Geçersiz giriş. Lütfen 1, 2, 3, 4, 5, 6 veya 7 girin.")
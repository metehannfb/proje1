def oyunmenü():
   import os
   print("\033[1;22;40m")
   print("   ╔══════════════════════╗")
   print("   ║  oyun uglama         ║")
   print("   ║                      ║")
   print("   ║1)Counter-Strike 2    ║")
   print("   ║2)Fornite             ║")
   print("   ║3BattleBit Remastered ║")
   print("   ║4)aimlabs             ║")
   print("   ║5)The forest          ║")
   print("   ║6)CurseForge          ║")
   print("   ║7)geri                ║")
   print("   ╚══════════════════════╝")
   secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5/6/7):")
   if secim == "1":
    print("Counter-Strike 2 açılıyor...")
    os.system("start steam://rungameid/730")
   elif secim == "2":
    print("Fortnite açılıyor...")
    os.system('start com.epicgames.launcher://apps/Fortnite?action=launch&silent=true')
   elif secim == "3":
    print("BattleBit Remastered açılıyor...")
    os.system("start steam://rungameid/671860")
   elif secim == "4":
    print("Aimlabs açılıyor...")
    os.system("start steam://rungameid/714010")
   elif secim == "5":
    print("The Forest açılıyor...")
    os.system("start steam://rungameid/242760")
   elif secim == "6":
    print("CurseForge açılıyor...")
    os.startfile(r"C:\Program Files (x86)\Overwolf\CurseForge\CurseForge.exe")
   else:
    print("Geçersiz giriş. Lütfen 1, 2, 3, 4, 5, 6 veya 7 girin.")








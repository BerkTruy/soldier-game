def intro():
    print("Askeri bir görev üzerindesin ve tehlikeli bir operasyona katılmak üzeresin.")
    print("Kamp alanında bulunan iki farklı yola karar vermen gerekiyor.")
    print("Birinci yol, düşmanın yoğun olduğu bölgeye açılıyor.")
    print("İkinci yol, daha güvenli bir bölgeye çıkıyor.")
    choice = input("Hangi yolu seçeceksin? (yoğun/güvenli): ").strip().lower()
    
    if choice == "yoğun":
        enemy_zone()
    elif choice == "güvenli":
        safe_zone()
    else:
        print("Geçersiz seçim. Lütfen 'yoğun' veya 'güvenli' yazın.")
        intro()

def enemy_zone():
    print("Düşmanın yoğun olduğu bölgeye girdin. Üzerinde dikkatlice ilerliyorsun.")
    print("Bir patika var, diğer tarafta bir köy görünüyor.")
    print("Patikadan ilerlerken bir pusula buluyorsun, köye ulaşmanın iyi bir yol olup olmadığını anlaman gerekiyor.")
    choice = input("Pusulayı kullanarak köy yolunu mu takip edeceksin, yoksa patikadan mı devam edeceksin? (köy/patika): ").strip().lower()
    
    if choice == "köy":
        village()
    elif choice == "patika":
        ambush()
    else:
        print("Geçersiz seçim. Lütfen 'köy' veya 'patika' yazın.")
        enemy_zone()

def safe_zone():
    print("Güvenli bölgeye ulaştın ve burada daha fazla askeri ekipman buluyorsun.")
    print("Burada bir kısıtlı alana girmeden önce bir görev listesi var.")
    print("Bir görev üstlenmen gerek, görevlerin içinden birini seçmen gerekiyor.")
    print("Görevler: 1) Gözetleme 2) Malzeme Teslimatı")
    choice = input("Hangi görevi seçeceksin? (gözetleme/malzeme): ").strip().lower()
    
    if choice == "gözetleme":
        surveillance()
    elif choice == "malzeme":
        supply()
    else:
        print("Geçersiz seçim. Lütfen 'gözetleme' veya 'malzeme' yazın.")
        safe_zone()

def village():
    print("Köye ulaştığında düşmanların bulunduğu bir üs gördün.")
    print("İki seçenek var: Üssü incelemek veya köyde gizlenmek.")
    choice = input("Üssü mi inceleyeceksin, yoksa köyde mi kalacaksın? (üs/köy): ").strip().lower()
    
    if choice == "üs":
        base()
    elif choice == "köy":
        hide()
    else:
        print("Geçersiz seçim. Lütfen 'üs' veya 'köy' yazın.")
        village()

def ambush():
    print("Patikadan devam ederken bir puskuya düştün. Düşman askerleri seni fark etti.")
    print("Bir kaçış yolu var, ama ne yazık ki hızlı düşünmen gerekiyor.")
    choice = input("Hızlıca kaçmak mı yoksa çatışmaya girmek mi istersin? (kaç/çatış): ").strip().lower()
    
    if choice == "kaç":
        escape()
    elif choice == "çatış":
        fight()
    else:
        print("Geçersiz seçim. Lütfen 'kaç' veya 'çatış' yazın.")
        ambush()

def surveillance():
    print("Gözetleme görevini başarıyla tamamladın ve önemli bilgileri topladın.")
    print("Bu bilgileri komutanına iletmen gerekiyor. Başarıyla görevini tamamladın.")
    print("Oyun bitti. Amk ibnesi kolay yolu neden seçtin?")

def supply():
    print("Malzeme teslimatını yaptın, ancak düşman tarafından saldırıya uğradın.")
    print("Yaralandın ve yardıma ihtiyaç duyuyorsun.")
    print("Oyun bitti. Bu görevde başarılı olamadın.")

def base():
    print("Üssü inceledikten sonra önemli bir plan buldun.")
    print("Bu planı komutanına iletmen gerekiyor.")
    print("Görevde başarılı oldun ve büyük bir başarı sağladın!")

def hide():
    print("Köyde gizlendin ve düşmanların gözünden kaçmayı başardın.")
    print("Güvenli bir şekilde bölgeden ayrıldın.")
    print("Oyun bitti. Gizlenme görevini başarılı bir şekilde tamamladın.")

def escape():
    print("Hızla kaçmayı başardın ve güvenli bir bölgeye ulaştın.")
    print("Düşmanları atlattın ve oyunda başarılı oldun!")

def fight():
    print("Düşmanlarla çatışmaya girdin, ancak yaralandın.")
    print("Yaralı olarak kaçmayı başaramadın ve oyunu kaybettin.")

# Oyunu başlat
intro()

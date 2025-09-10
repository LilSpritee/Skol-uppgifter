import bowlingData as bd
while True:
    val1 = input("Välkommen till bokningssystemet för idrottshallen!\nAnge val\n1. Boka bana\n2. Avboka\n3. Se bokningar\n4. Avsluta\n")
    if val1 == "1":
        sport = input("Vilken sport vill du boka?\n1. Bowling\n2. Badminton\n3. Tennis\n")
        tid = input("Vilken tid vill du boka? (9-21)\n")
        if sport == "1":
            bana = int(input("Vilken bana vill du boka? (1-3)\n"))
            if bd.bowling[bana][tid]:
                print("Tyvärr är denna tid redan bokad.")
            else:
                bd.bowling[bana][tid] = True
                print("Bokningen är genomförd\nBana:", bana, "\nTid:", tid, "\nSport: Bowling\n")
        elif sport == "2":
            bana = int(input("Vilken bana vill du boka? (1-5)"))
            if bd.badminton[bana][tid]:
                print("Tyvärr är denna tid redan bokad.")
            else:
                bd.badminton[bana][tid] = True
                print("Bokningen är genomförd\nBana:", bana, "\nTid:", tid, "\nSport: Badminton\n")
        elif sport == "3":
            bana = int(input("Vilken bana vill du boka? (1-4)"))
            if bd.tennis[bana][tid]:
                print("Tyvärr är denna tid redan bokad.")
            else:
                bd.tennis[bana][tid] = True
                print("Bokningen är genomförd\nBana:", bana, "\nTid:", tid, "\nSport: Tennis\n")
        else:
            print("Felaktigt val")
            
    elif val1 == "2":
        print("placeholder för avbokning")
    
    elif val1 == "3":
        sport = input("Vilken sport vill du se bokningar för?\n1. Bowling\n2. Badminton\n3. Tennis\n")
        if sport == "1":
            bana = int(input("Vilken bana vill du se bokningar för? (1-3)\n"))
            for tider in bd.bowling[bana]:
                print(f"Klockan {tider} {'Är bokad' if bd.bowling[bana][tider] else 'Är ledig'}")
        elif sport == "2":
            bana = int(input("Vilken bana vill du se bokningar för? (1-5)\n"))
            for tider in bd.badminton[bana]:
                print(f"Klockan {tider} {'Är bokad' if bd.badminton[bana][tider] else 'Är ledig'}")
        elif sport == "3":
            bana = int(input("Vilken bana vill du se bokningar för? (1-4)\n"))
            for tider in bd.tennis[bana]:
                print(f"Klockan {tider} {'Är bokad' if bd.tennis[bana][tider] else 'Är ledig'}")
        else:
            print("Felaktigt val")
            
    elif val1 == "4":
        print("Avslutar bokningssystemet")
        break
    
    else:
        print("Felaktigt val")
    
        
        
        
        

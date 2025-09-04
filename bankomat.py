# Linus Folkjern bankomat uppgift
# Tror inte det går att crasha programmet men du kan försöka haha
# Färdig skapade ett konto för snabbre testning
konton = [
    "Linus"
]
koder = [
    "1337"
]
pengar = [
    67
]
transaktioner = [
    []
]

while True: # Vanlig while loop för att hålla programmet igång
    print("================================") # Dekorativ linje för att separera olika sektioner av programmet
    val = input("Logga in eller registrera (l/r): ").lower()
    if val == "l":
        namn = input("Ange kontonamn: ") # Frågar användaren efter kontonamn
        if namn in konton:
            kod = input("Ange lösenord: ") # Frågar användaren efter lösenord
            print("================================")
            if kod == koder[konton.index(namn)]: # Om koden anget är lika med koden i listan på samma index som kontot
                print("Välkommen tillbaka,", namn)
                print("Du har", pengar[konton.index(namn)], "kronor på ditt konto.")
                print("Vad vill du göra?")
                while True: # Loop för att hålla användaren inloggad tills de väljer att logga ut
                    val2 = input("1. Ta ut pengar\n2. Sätt in pengar\n3. Logga ut\n4. Visa Saldo\n5. Visa transaktioner\nDitt val: ")
                    print("================================")
                    if val2 == "1":
                        summa_ut = int(input("Hur mycket pengar vill du ta ut? "))
                        if summa_ut > pengar[konton.index(namn)]:
                            print("Du är för fattig prova lägre summa")
                        elif summa_ut <= pengar[konton.index(namn)]:
                            pengar[konton.index(namn)] -= summa_ut
                            print("Du har nu tagit ut", summa_ut, "kronor från ditt konto och har", pengar[konton.index(namn)], "kvar.")
                            transaktioner[konton.index(namn)].append("Tog ut "+str(summa_ut)+"kronor") # Lägger till transaktionen i listan på samma index som kontot
                        
                    elif val2 == "2":
                        try: # Try except för att stoppa använder från att skriva nått annat än integer
                            summa_in = int(input("Hur mycket pengar vill du sätta in? "))
                            pengar[konton.index(namn)] += summa_in
                            print("Du har nu satt in", summa_in, "kronor på ditt konto. Saldo är", pengar[konton.index(namn)])
                            transaktioner[konton.index(namn)].append("Satt in "+str(summa_in)+"kronor") # Lika som ovan fast för insättning
                        except: # Om inte integer så prova igen
                            print("Ange en giltig summa.")
                    
                    elif val2 == "3":
                        print("Utloggad välkommen åter", namn)
                        break # Bryter loopen och loggar ut användaren
                    
                    elif val2 == "4":
                        print("Ditt saldo är", pengar[konton.index(namn)], "kronor.") # Visar saldot på samma index som kontot
                    
                    elif val2 == "5":
                        print("Dina transaktioner:")
                        print("================================")
                        for adrian in transaktioner[konton.index(namn)]: # Loop för att skriva ut transaktioner utan att visa listformatet
                            print(adrian) # Adrian förklarar sin friendgroup
                        
                    else:
                        print("Ange 1, 2 eller 3 och försök igen.")
                    
                    print("================================")
            
            else: # Om fel lösenord så säg åt användaren att prova igen
                print("Fel lösenord, prova igen.")
                    
        else:
            print("Kontot finns inte, prova igen eller registrera för attt skapa ett nytt konto.")
            
    elif val == "r":
        skapa_konto = input("Ange namn på ditt nya konto: ")
        if skapa_konto in konton: # Om kontot redan finns säg åt användaren att prova ett annat namn
            print("Kontot finns redan, prova ett annat namn.")
        else: # Annars skapa kontot
            skapa_kod = input("Ange ett lösenord för ditt konto: ")
            print("================================")
            konton.append(skapa_konto)
            koder.append(skapa_kod)
            pengar.append(0) # Nya konton börjar med 0 kronor
            transaktioner.append([]) # Nya konton börjar med en tom transaktionslista
            print("Du har nu skapat ett konto med namnet", skapa_konto, "med koden", skapa_kod,"\nlogga in för att sätta in pengar.")
    
    else:
        print("Ogiltigt val, ange l eller r och försök igen.") # Om använder inte läser instruktioner
        
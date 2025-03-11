import random 
def wuerfeln():
    return random.randint(1, 6)
def spiel_start(): 
    # Anzahl der Spieler abfragen
    while True:
        try: 
            anzahl_spieler = int(input("Gib die Anzahl der Spieler ein: "))
            if anzahl_spieler > 1:
                break
            else: print("Es müssen mindestens 2 Spieler sein!")
        except ValueError:
            print("Bitte eine gültige Zahl eingeben!")

    # Spieler initialisieren
    spieler = {f"Spieler {i+1}": 3 for i in range(anzahl_spieler)}

    # Spiel starten
    while all(l > 0 for l in spieler.values()):
        aktuelle_summe = 0
        print("\nNeue Runde beginnt!")
        
        while True:
            for name in list(spieler.keys()):
                if spieler[name] <= 0:
                    continue # Spieler mit 0 Leben überspringen

                input(f"{name} ist dran. Drücke Enter zum Würfeln... ")
                wurf = wuerfeln()
                aktuelle_summe += wurf

                print(f"{name} hat eine {wurf} gewürfelt. Gesamt: {aktuelle_summe}")

                if aktuelle_summe > 15:
                    spieler[name] -=1
                    print(f"{name} hat die 15 überschritten und verliert ein Leben! Verbleibende Leben: {spieler[name]}")
                    break # Runde neu starten

            if aktuelle_summe > 15:
                break # Runde neu starten

     # Verlierer bestimmen
    verlierer = [name for name, leben in spieler.items()if leben == 0][0]
    print(f"\nSpiel beendet!{verlierer} hat verloren!")

# Spiel starten
if __name__ == "__main__":
    spiel_start()



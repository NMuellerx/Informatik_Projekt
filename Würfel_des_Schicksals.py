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
    
    #Spielregeln definieren
    print("\nSpielregeln:\nJeder Spieler hat 3 Leben. Die Spieler würfeln abwechselnd,\nwobei die Augenzahl zusammenaddiert wird. Kommt ein Spieler durch würfeln über die Zahl 15,\nverliert er ein Leben und es beginnt eine neue Runde.")
    print("\nZusatzregeln: Eine gewürfelte 3 wird als O gewertet.\n")

    # Spieler initialisieren
    spieler = {f"Spieler {i+1}": 3 for i in range(anzahl_spieler)}
    
    # Spiel starten
    while sum(leben > 0 for leben in spieler.values()) > 1: # Spiel läuft solange mehr als ein Spieler Leben hat
        aktuelle_summe = 0
        print("\nNeue Runde beginnt!")

        while True:
            for name in list(spieler.keys()):
                if spieler[name] <= 0:
                    continue # Spieler mit 0 Leben überspringen
                
                input(f"{name} ist dran. Drücke Enter zum Würfeln... ")
                wurf = wuerfeln()
                while wurf == 6: # Wenn 6 gewürfelt wird, darf der Spieler nocheinmal würfeln
                    print(f"{name} hat eine 6 gewürfelt er darf noch einmal")
                    input(f"{name} ist dran. Drücke Enter zum Würfeln... ")
                    wurf = wuerfeln()
                    if wurf == 6:
                        continue
                    else:
                        break
                if wurf == 3: # Wenn 3 gewürfelt wird, zählt diese mit der Wertigkeit 0
                    wurf = 0
                    aktuelle_summe += wurf # Aufaddieren der Würfe
                    print(f"{name} hat eine 3 gewürfelt. Gesamt: {aktuelle_summe}")
                else:
                    aktuelle_summe += wurf # Aufaddieren der Würfe
                    print(f"{name} hat eine {wurf} gewürfelt. Gesamt: {aktuelle_summe}")
                if aktuelle_summe > 15:    
                    if spieler[name] == 1: # Bei letztem Leben gibt es eine last Chance
                        print(f"Gnadenbrot. {name} hat eine letzte Chance im Spiel zu bleiben")
                        input(f"Drücke Enter zum Würfeln... ")
                        wurf = wuerfeln()
                        if wurf == 6: # Wenn 6 gewürfelt wird, bleibt Spieler im Spiel
                            print(f"{name} hat eine 6 gewürfelt. Er bleibt mit einem Leben im Spiel")
                        else:
                            spieler[name] -= 1 # Wenn 1-5 gewürfelt wird, scheidet Spieler aus
                            if sum(leben > 0 for leben in spieler.values()) < 2:
                                print(f"\n{name} hat {wurf} gewürfelt er ist ausgeschieden.")
                            else:
                                print(f"\n{name} hat {wurf} gewürfelt er ist ausgeschieden. Das Spiel wird ohne ihn fortgesetzt")
                    else:
                        while True:
                            print(f"\n{name}, willst du...\n" ###
                                "1 - Ein Leben verlieren?\n"  ### Abfrage ob man Leben verlieren will oder stattdessen ein Strafe in Kauf nimmt.
                                "2 - bestraft werden?\n"      ### Geht nur wenn der Spieler noch mehr als 1 Leben hat
                                "Deine Wahl (1 oder 2): ")    ###
                            entscheidung = input()
                            if entscheidung == "2":
                                print(f"{name} muss ein CenterShock essen. Das Spiel geht weiter")
                                break
                            elif entscheidung == "1":
                                spieler[name] -= 1
                                print(f"{name} verliert ein Leben. Verbleibende Leben: {spieler[name]}")
                                break
                            else:
                                print("Bitte 1 oder 2 eingeben.") # Aufforderung zur korrekten Eingabe nach falscher Eingabe
                    break # Runde neu starten
                
            if aktuelle_summe > 15:
                break # Runde neu starten

    # Gewinner bestimmen
    gewinner = [name for name, leben in spieler.items() if leben > 0][0]
    print(f"\nSpiel beendet! {gewinner} hat gewonnen!") 

# Spiel starten
if __name__ == "__main__":
    spiel_start()
import random 

# Farben für die Ausgabe
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   ITALICS = '\033[3m'
   END = '\033[0m'

# Würfelfunktion
def wuerfeln():
    return random.randint(1, 6)

# definieren der Zufallsbestrafungen
def zufallsbestrafung():
    strafen = ["ein Centershock essen", "einen albernen Tanz aufführen", "für den Rest des Spiels Sätze mit einem Grunzen beenden", "einen Zitronenschnitz essen"]
    return random.choice(strafen)

# Spielstart
def spiel_start(): 
    print(color.CYAN +"╔══════════════════════════════╗")
    print("║" + color.BOLD + "  DIE WÜRFEL DES SCHICKSALS   " + color.END + color.CYAN + "║")
    print("║"+ color.END +"        by [Patrick Boßlet]   " + color.CYAN +"║")
    print("║"+ color.END +"        and [Niclas Müller]   " + color.CYAN +"║")
    print("╚══════════════════════════════╝\n" + color.END)
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
    print("\nSpielregeln:\nJeder Spieler hat 3 Leben. Die Spieler würfeln abwechselnd,\nwobei die Augenzahl zusammenaddiert wird. Kommt ein Spieler durch würfeln über die Zahl 15,\nverliert er ein Leben oder erhält eine Bestrafung - es folgt eine neue Runde.")
    print("\nZusatzregeln:\n- Eine gewürfelte 3 wird als O gewertet.\n- Bei einer 6 wird nochmal gewürfelt\n- Sollte der Spieler im Begriff sein, sein letztes Leben zu verlieren,\n  hat er durch ein Gnadenbrot die Chance im Spiel zu bleiben. Hierfür muss er eine 6 würfeln")

    # Spieler initialisieren
    spieler = {f"Spieler {i+1}": 3 for i in range(anzahl_spieler)}
    
    # Spiel starten
    while sum(leben > 0 for leben in spieler.values()) > 1: # Spiel läuft, solange mehr als ein Spieler Leben hat
        aktuelle_summe = 0
        print("\nNeue Runde beginnt!\n")

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
                                print(f"\n{name} hat eine {wurf} gewürfelt er ist ausgeschieden.")
                            else:
                                print(f"\n{name} hat eine {wurf} gewürfelt er ist ausgeschieden. Das Spiel wird ohne ihn fortgesetzt")

                    else:
                        while True:
                            print(f"\n{name}, willst du...\n" ###
                                + color.RED + "1" + color.END + " - Ein Leben verlieren?\n"  ### Abfrage ob man Leben verlieren will oder stattdessen ein Strafe in Kauf nimmt.
                                + color.BLUE + "2" + color.END + "- bestraft werden?\n"      ### Geht nur wenn der Spieler noch mehr als 1 Leben hat
                                "Deine Wahl (" + color.RED + "1" + color.END + " oder " + color.BLUE + "2" + color.END+"): ")    ###
                            entscheidung = input()
                            if entscheidung == "2":
                                print(f"{name} muss ", end="")
                                print(zufallsbestrafung())
                                break
                            elif entscheidung == "1":
                                spieler[name] -= 1
                                print(f"{name} verliert ein Leben. " + color.ITALICS + "Verbleibende Leben: ", end="")
                                print(color.GREEN + f"{spieler[name]}" + color.END)
                                break
                            else:
                                print("Bitte 1 oder 2 eingeben.") # Aufforderung zur korrekten Eingabe nach falscher Eingabe
                    break # Runde neu starten
                
            if aktuelle_summe > 15:
                break # Runde neu starten

    # Gewinner bestimmen
    gewinner = [name for name, leben in spieler.items() if leben > 0][0]
    print("\nSpiel beendet! ", end="")
    print(color.YELLOW + f"{gewinner} hat gewonnen!" + color.END) 

# Spiel starten
if __name__ == "__main__":
    spiel_start()
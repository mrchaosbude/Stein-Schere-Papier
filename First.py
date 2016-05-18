import random
import pickle

x = "None!" # normales spiel oder spiel extra
highscore = {"win": 0, "lose": 0, "draw": 0, "geWin": 0, "geLose": 0, "geDraw": 0}

#highscore wird geladen!
def loadhighscore():
    global highscore
    try:
        highscore = pickle.load( open("save.p", "rb"))
    except (OSError, IOError) as e:
        highscore = {"win": 0, "lose": 0, "draw": 0, "geWin": 0, "geLose": 0, "geDraw": 0}
        pickle.dump(highscore, open("save.p", "wb"))


#Stein Schere Papier random generator
def kiRandom(normaloderextra):
    ai = ("Stein", "Schere", "Papier", "Echse", "Spock")
    auswahl = ai[random.randint(0,normaloderextra)]
    return (auswahl)

#Das Haubtmenue
def menue():
    loadhighscore()
    print("""
     ___ _       _          ___     _                    ___           _
    / __| |_ ___(_)_ _     / __| __| |_  ___ _ _ ___    | _ \__ _ _ __(_)___ _ _
    \__ \  _/ -_) | ' \ _  \__ \/ _| ' \/ -_) '_/ -_)_  |  _/ _` | '_ \ / -_) '_|
    |___/\__\___|_|_||_( ) |___/\__|_||_\___|_| \___( ) |_| \__,_| .__/_\___|_|
                       |/                           |/           |_|
                       """)
    ans = True
    while ans:
        print("""
        1. Spiel starten
        2. Spiel Extra
        3. High­score
        4. Credits
        0. Exit/Quit
        """)
        ans = input("Triff deine Wahl :")
        if ans == "1":
            game_engine()
        elif ans == "2":
            game_engine_extra()
        elif ans == "3":
            highscorem()
        elif ans == "4":
            print("\n NOCH NICHT!!!")
        elif ans == "0":
            print("\n Goodbye")
            ans = None
            quit()
        else:
            print("\n oh da ist wohl etwas schiefgelaufen, versuche es doch noch einmal!")

#Das normale spiel
def game_engine():
    global x
    x = 1
    ki = kiRandom(2)
    choice = None
    wahl = None
    ans = True
    while ans:
        print("""
            1. Stein
            2. Schere
            3. Papier
            """)
        ans = input("Triff deine Wahl :")
        if ans == "1":
            choice = {"Stein" : 3, "Schere" : 1, "Papier" : 0}
            wahl = "Stein"
            ans = None
        elif ans == "2":
            choice = {"Stein": 0, "Schere": 3, "Papier": 1}
            wahl = "Schere"
            ans = None
        elif ans == "3":
            choice = {"Stein": 1, "Schere": 0, "Papier": 3}
            wahl = "Papier"
            ans = None
        else:
            print("\n Bitte wähle eine Zahl zwischen 1-3")

    comparison (choice, ki, wahl)

#Mit echse und spook
def game_engine_extra():
    global x
    x = 2
    ki = kiRandom(4)
    choice = None
    ans = True
    while ans:
        print("""
            1. Stein
            2. Schere
            3. Papier
            4. Echse
            5. Spock
            """)
        ans = input("Triff deine Wahl :")
        if ans == "1":
            choice = {"Stein" : 3, "Schere" : 1, "Papier" : 0, "Echse" : 1, "Spock" : 0}
            wahl = "Stein"
            ans = False
        elif ans == "2":
            choice = {"Stein": 0, "Schere": 3, "Papier": 1, "Echse" : 1, "Spock" : 0}
            wahl = "Schere"
            ans = False
        elif ans == "3":
            choice = {"Stein": 1, "Schere": 0, "Papier": 3, "Echse" : 0, "Spock" : 1}
            wahl = "Papier"
            ans = False
        elif ans == "4":
            choice = {"Stein": 0, "Schere": 0, "Papier": 1, "Echse" : 3, "Spock" : 1}
            wahl = "Echse"
            ans = False
        elif ans == "5":
            choice = {"Stein": 1, "Schere": 1, "Papier": 0, "Echse" : 0, "Spock" : 3}
            wahl = "Spock"
            ans = False
        else:
            print("\n Bitte wähle eine Zahl zwischen 1-5")

    comparison (choice, ki, wahl)

#gewonnen oder verloren
def comparison (player1 , player2, chois):
    global highscore
    ai = int(player1[player2])
    if ai == 1:
        print("""
 (
 )\ )      (   (  (                         (
(()/(     ))\  )\))(    (    (      (      ))\  (
 /(_))_  /((_)((_)()\   )\   )\ )   )\ )  /((_) )\ )
(_)) __|(_))  _(()((_) ((_) _(_/(  _(_/( (_))  _(_/(
  | (_ |/ -_) \ V  V // _ \| ' \))| ' \))/ -_)| ' \))
   \___|\___|  \_/\_/ \___/|_||_| |_||_| \___||_||_|

 """ )#Gewonnen
        print("Du hast",chois, "gäwahlt, und dein Gegner hatte", player2 ,"!")
        if x == 1:
            highscore["win"] = highscore["win"] + 1
        elif x == 2:
            highscore["geWin"] = highscore["geWin"] + 1

    elif ai == 0:
        print("""
                  _______  _______  _        _______  _______  _______  _
        |\     /|(  ____ \(  ____ )( \      (  ___  )(  ____ )(  ____ \( (    /|
        | )   ( || (    \/| (    )|| (      | (   ) || (    )|| (    \/|  \  ( |
        | |   | || (__    | (____)|| |      | |   | || (____)|| (__    |   \ | |
        ( (   ) )|  __)   |     __)| |      | |   | ||     __)|  __)   | (\ \) |
         \ \_/ / | (      | (\ (   | |      | |   | || (\ (   | (      | | \   |
          \   /  | (____/\| ) \ \__| (____/\| (___) || ) \ \__| (____/\| )  \  |
           \_/   (_______/|/   \__/(_______/(_______)|/   \__/(_______/|/    )_)
                """)#Verloren
        print("du hast ", chois, "gäwahlt, und dein Gegner hatte", player2 ,"!" )
        if x == 1:
            highscore["lose"] = highscore["lose"] + 1
        elif x == 2:
            highscore["geLose"] = highscore["geLose"] + 1

    elif ai == 3:
        print("""
  __   _  ____   _  ______  ____   _    __   ______  ______  __   _  ____  ______  _____   ______  ____   _  ___
 |  | | ||    \ | ||   ___||    \ | | _|  |_|   ___||   ___||  |_| ||    ||   ___||     \ |   ___||    \ | ||   |
 |  |_| ||     \| ||   ___||     \| ||_    _|`-.`-. |   |__ |   _  ||    ||   ___||      \|   ___||     \| ||___|
 |______||__/\____||______||__/\____|  |__| |______||______||__| |_||____||______||______/|______||__/\____||___|

""")#unentschieden
        print("Du hast ", chois, "gäwahlt, und dein Gegner hatte", player2)
        if x == 1:
            highscore["draw"] = highscore["draw"] + 1
        elif x == 2:
            highscore["geDraw"] = highscore["geDraw"] + 1
    else:
        print("Dies sollte man nicht sehen")

    pickle.dump(highscore, open("save.p", "wb"))
    repeat()

#das spiel wiederholen
def repeat():
    ans = True
    while ans:
        print("Möchtest du noch eine Runde spielen? (J/N)")
        ans = input(">>")
        if ans == "j" or ans == "J":
            if x == 1:
                game_engine()
            elif x == 2:
                game_engine_extra()
        elif ans == "n" or ans == "N":
            menue()
        else:
            print("\n Die Eingabe war nicht die Richtige!")

# Highscore!
def highscorem():
            # print("\033c");
            #os.system('cls||clear')
            global highscore
            print("""
              _  _                              _                ___          _         _
             | \| |  ___   _ _   _ __    __ _  | |  ___   ___   / __|  _ __  (_)  ___  | |
             | .` | / _ \ | '_| | '  \  / _` | | | / -_) (_-<   \__ \ | '_ \ | | / -_) | |
             |_|\_| \___/ |_|   |_|_|_| \__,_| |_| \___| /__/   |___/ | .__/ |_| \___| |_|
                                                                      |_|
                                                                      """)
            print("Du hast", highscore["win"], "Gewonnen", highscore["lose"], "mal verloren und", highscore["draw"],
                  "Unendschieden Gespielt!")

            print("""
              ___         _                    ___          _         _
             | __| __ __ | |_   _ _   __ _    / __|  _ __  (_)  ___  | |
             | _|  \ \ / |  _| | '_| / _` |   \__ \ | '_ \ | | / -_) | |
             |___| /_\_\  \__| |_|   \__,_|   |___/ | .__/ |_| \___| |_|
                """)
            print("Du hast", highscore["geWin"], "Gewonnen", highscore["geLose"], "mal verloren und",
                  highscore["geDraw"], "Unendschieden Gespielt!")

            ans = True
            while ans:
                print("""
                        1. Normales Spiel highscore Resetten
                        2. Extra Spiel highscore Resetten
                        3. Alle Resetten
                        4. Zurück zum Hauptmenue
                        """)
                ans = input("Triff deine Wahl :")
                if ans == "1":
                    highscore["win"] = 0
                    highscore["lose"] = 0
                    highscore["draw"] = 0
                    ans = None
                elif ans == "2":
                    highscore["geWin"] = 0
                    highscore["geLose"] = 0
                    highscore["geDraw"] = 0
                    ans = None
                elif ans == "3":
                    highscore = {"win": 0, "lose": 0, "draw": 0, "geWin": 0, "geLose": 0, "geDraw": 0}
                    ans = None
                elif ans == "4":
                    menue()
                    ans = None
                elif ans == "99":
                    highscore = {"win": 99, "lose": 99, "draw": 99, "geWin": 99, "geLose": 99, "geDraw": 99}
                    ans = None
                else:
                    print("\n Bitte wähle eine Zahl zwischen 1-4")
            pickle.dump(highscore, open("save.p", "wb"))


#der erste aufruf
menue()
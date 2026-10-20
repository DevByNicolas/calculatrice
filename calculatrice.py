def calculatrice ():
    while True:
        print("Bienvenue dans la calculatrice interactive ")
        print("1.Addition: (+)")
        print("2.Soustraction: (-)")
        print("3.Multiplication: (*)")
        print("4.Division: (/)")
        print("5.Quitter")

        choix= input("choisissez un nombre entre 1 et 5 : ")

        if choix == "5" :
           print("Au revoir")
           break

        elif choix in ("1", "2", "3", "4"):
         try:
           nombre1=int(input("Entrez un nombre "))
           nombre2=int(input("entrez le deuxième nombre "))
         except ValueError:
                print("Erreur : Veuillez entrer des nombres valides.")
                continue

        if choix =="1":
             resultat= nombre1 + nombre2
             print(f"la somme de {nombre1} + {nombre2} est {resultat } ")

        elif choix =="2":
            resultat= nombre1 - nombre2
            print(f"la soustration de {nombre1} - {nombre2} est {resultat}")

        elif choix =="3":
            resultat= nombre1 * nombre2
            print(f"la Multiplication de {nombre1} * {nombre2} est {resultat}")

        elif choix =="4":
            if nombre2 == 0:
                print("Erreur : Division par zéro impossible.")
            else:
                resultat= nombre1 / nombre2
                print(f"la Division de {nombre1} / {nombre2} est {resultat}")
        else :
            print("Erreur : veuillez choisir un nombre entre 1 et 5")    


calculatrice()
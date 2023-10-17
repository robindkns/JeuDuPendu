victoire = 0                                # J'initie mes variables ici car ainsi elles seront globales et fonctionneront dans ma fonction, ainsi qu'en dehors, sinon elles se réinitialiseront à chaque partie
défaite = 0
partie_jouée = 0

utilisateur = input("Quel sera votre nom d'utilisateur ? ")


def pendu(play,user):

    global victoire                                                                             # Déclare mes valeurs globales dans ma fonction afin de faire un récapitulatif des parties
    global défaite
    global partie_jouée

    utilisateur = user

    dico_jouées = {utilisateur : partie_jouée}
    dico_victoires = {utilisateur : victoire}
    dico_défaites = {utilisateur : défaite}

    

    if play == "oui":
        
        import random

        liste_mots = ["voiture","maison","tartine","boite","ordinateur","coding","molengeek","molenbeek","batiment","fenetre","trottinette","papier","ambidextre"]

        mot = random.choice(liste_mots)                                                             # Choisi un mot au hasard dans ma liste de mots

        mot_caché = list(mot)

        for i in range(len(mot_caché)):                                                             # Donne le mot caché avec des -
            mot_caché[i] = "-"


        mot_caché_affiché = "".join(mot_caché)                                                      # Permet de passer d'une liste à un string

        print(" ")
        print(" ")
        print("Bienvenue sur ce tout nouveau jeu totalement EXCLUSIF à MOLENGEEK, le jeu du PENDU !")
        print("Vous allez devoir deviner le mot qui se cache derrière ces tirets !")
        print(mot_caché_affiché)
        print("Comme vous pouvez le voir, ce mot fait ",len(mot_caché)," lettres.")
        print("Vous aurez 7 essais pour y arriver.")
        print(" ")
        print(" ")


        essai = 7                                                           
        faux = 0                                                                                    # Initie les variables qui vont permettre de manipuler les bons et mauvais essais
        vrai = 0

        while essai != 0 and mot_caché_affiché != mot:                                              # Ne sortira pas de la boucle tant qu'il n'a pas gagné (mot caché = mot de base) ou perdu (essai = 0)
            
            print(mot_caché_affiché)
            lettre = input("Donnez moi maintenant une lettre qui, pour vous, se trouve dans le mot qui se cache derrière ces tirets : ")
            print(" ")
            print(" ")
            
            if len(lettre) == 1 or lettre == int() :                                                # Laisse jouer si la personne introduit bien strictement une lettre (pas une chaine de caractère ni chiffre)
                for i in range(len(mot)):                                                           # Boucle for qui va vérifier chaque caractère un à un
                    if lettre == mot[i] or lettre == mot[i].upper():                                # Si la lettre (minuscule OU majuscule) encodée est bien dans le mot
                        vrai = vrai + 1                                                             
                        for i2 in range(len(mot_caché)):
                            mot_caché[i] = str(lettre)                                              # Remplace le - par la lettre
                    else :                                                                          # Si la lettre encodée n'est pas dans le mot
                        faux = faux + 1
            
                if faux > 0 and vrai == 0:                                                          # Si mon compteur faux a été ajouté de 1 et que mon compteur vrai est resté à 0
                    print("La lettre ",lettre," n'est pas dans le mot :'(")
                    essai = essai - 1
                    faux = 0                                                                        # Réinitialise mes compteurs vrais faux pour le prochain tour de boucle
                    vrai = 0
                else :
                    vrai = 0
                    faux = 0

            
                mot_caché_affiché = "".join(mot_caché)                                              # Retransforme le mot caché que je manipulais sous forme d'une liste en string
                

            else :
                print("ERROR 404 - Veuillez introduire strictement une lettre")

            # print(mot_caché_affiché)
            print("Nombre d'essais restants : ", essai)
            

        partie_jouée = int(partie_jouée) + 1 

        verif_in_dico = utilisateur in dico_jouées                                                  # Pour savoir si l'utilisateur est déjà entré dans le dico

        if essai > 0:                                                                               # S'il reste des essais, c'est gagné
            print("BRAVO ",user,"TU AS GAGNE !!!!")
            victoire = int(victoire) + 1
            if verif_in_dico == False :                                                             # Est sensé ajouté un nouvel utilisateur s'il n'est pas encore dans le dictionnaire mais ça efface toute les données déjà présentes
                dico_jouées.update({str(utilisateur) : int(partie_jouée)})                          # SEUL PROBLEME DU CODE
                dico_victoires.update({str(utilisateur) : int(victoire)})
                # dico_jouées = {utilisateur : partie_jouée}
                # dico_victoires = {utilisateur : victoire}
            else :
                dico_jouées[utilisateur] = dico_jouées[utilisateur] + 1
                dico_victoires[utilisateur] = dico_victoires[utilisateur] + 1

        else :
            print("TU AS PERDU" , user,"HAHAHA LOOSER !!!!")
            défaite = int(défaite) + 1
            if verif_in_dico == False :                                                             # COMME AU-DESSUS
                dico_jouées.update({utilisateur : partie_jouée})                                    # SEUL PROBLEME DU CODE
                dico_défaites.update({utilisateur : défaite})
                # dico_jouées = {utilisateur : partie_jouée}
                # dico_défaites = {utilisateur : défaite}
            else :
                dico_jouées[utilisateur] = dico_jouées[utilisateur] + 1
                dico_défaites[utilisateur] = dico_défaites[utilisateur] +1
        
        
        print("Vous avez ",victoire," victoire(s) et ",défaite," défaite(s) en ",partie_jouée," partie(s) jouée(s) !")

        consulter = input("Veux-tu consulter les scores des différents utilisateurs ? (oui / non)")

        if consulter == "oui" :
            print("Nombre de parties jouées : ",dico_jouées)
            print("Nombre de victoires      : ",dico_victoires)
            print("Nombre de défaites       : ",dico_défaites)

        rejouer = input("Souhaitez-vous rejouer une partie ? (oui / non) ")

        if rejouer == "oui" :
            user_change = input("Voulez-vous changer d'utilisateur ? (oui / non) ")

            if user_change == "oui":
                utilisateur = input("Quel sera votre nom d'utilisateur ? ")
                partie_jouée = 0                                                            # Réinitialise si on change d'utilisateur 
                victoire = 0
                défaite = 0
            else :
                pendu(rejouer,utilisateur)                                                  # Je rappelle ma fonction afin de rejouer

        # pendu(rejouer,utilisateur)                            




pendu(input("Souhaitez-vous jouer une partie ? (oui / non)"),utilisateur)
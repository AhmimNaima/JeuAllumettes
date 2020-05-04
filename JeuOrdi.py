######################################################################### #
# nom : jeu_ordi #
# valeurs entree : nb_allum et prise_max, nombre d'allumette en jeu etnombre d'allumette que l'on peut prendre au plus.
# valeurs sortie : prise, nombre d'allumettes prises.
# fonction : retourne la meilleure prise à faire
# #########################################################################
def jeu_ordi(nb_allum, prise_max):
    global prise
    s = prise_max + 1
    t = (nb_allum - s) % (prise_max + 1)
    while(t != 0):
        s -= 1
        t = (nb_allum - s) % (prise_max + 1)
        prise = s - 1
    if ( prise == 0):
        prise = 1
    print("l'ordi en prend : ", prise)
    return prise

prise=0
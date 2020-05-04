######################################################################### #
# nom : main
# fonction : initialiser le jeu et l'organiser.
# #########################################################################
from Allumette import afficher_allumettes
from JeuOrdi import jeu_ordi


def main():
        #initialisation des variables.
        nb_max_d=0
        #nbre d'allumettes maxi au départ
        nb_allu_max=0
        #nbre d'allumettes maxi que l'on peut tirer au maxi
        nb_allu_rest=0;
        #nbre d'allumettes restantes
        prise=0
        #nbre d'allumettes prises par le joueur
        qui = -1 #qui joue? 0=User --- 1=PC


        # verification pour l'initialisation.
        while( nb_max_d < 10 or nb_max_d > 60):
           try:
               nb_max_d = int(input("Entrez un nombre max d'allumette au depart entre 10 et 60."))
           except:
               print("saisie incorrecte")

        # mise a jour du nombre d'allumette en jeu.
        nb_allu_rest = nb_max_d
        afficher_allumettes(nb_allu_rest)
        nb_allu_max = int(input("Entrez Le nombre maximal d'allumettes que l'on peut retirer "))
        qui=int(input("Qui commence? 0:joueur  1:Ordi "))
        if (qui==0):
         while(nb_allu_rest>=1):

          print("Il y a %i allumettes et vous avez droit d'en retirer de 1 à %i" % (nb_allu_rest, nb_allu_max))
          prise = int(input("Combien d'allumettes vous voulez retirer ?"))

          nb_allu_rest-=prise
          afficher_allumettes(nb_allu_rest)
          if(nb_allu_rest>0):
            print(nb_allu_rest)
            prise = jeu_ordi(nb_allu_rest, nb_allu_max)
            nb_allu_rest-=prise
            print(nb_allu_rest)
            afficher_allumettes(nb_allu_rest)
            if(nb_allu_rest<=0):
             print('vous avez gangé!')
          else:
            print("L'ordinateur gangé!")

        else:
          while (nb_allu_rest >= 1):
            prise = jeu_ordi(nb_allu_rest, nb_allu_max)
            nb_allu_rest -= prise
            print(nb_allu_rest)
            afficher_allumettes(nb_allu_rest)
            if(nb_allu_rest>0):
                print("Il y a %i allumettes et vous avez droit d'en retirer de 1 à %i" % (nb_allu_rest, nb_allu_max))
                prise = int(input("Combien d'allumettes vous voulez retirer ?"))
                nb_allu_rest -= prise
                afficher_allumettes(nb_allu_rest)
                if(nb_allu_rest<=0):
                    print("L'ordi à gangé!")
            else:
                print("vous avez gangé!")











if __name__ == '__main__':
   main()

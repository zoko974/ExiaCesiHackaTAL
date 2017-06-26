												#########################################
												##############  EXIA.CESI  ##############
												#########################################



Fonctionnement de l'ensemble des livrables :

AVANT DE VOUS LANCEZ DANS UNE PARTIE MERCI DE LIRE CETTE DERNIERE COMPLETEMENT SINON LE FONCTIONNEMENT N'EST PAS GARANTI.



												----------------------------------------
												--- PARTIE 1 : RECHERCHE DES DONNEES ---
												----------------------------------------

Les fichiers du répertoire "parAnnee" ont été créés par ce script, vous n'avez donc pas besoin de réaliser ce process, néanmoins nous vous laissons les étapes pour le refaire.

1)	Si vous avez une bonne puissance de calcul et assez de RAM lancez juste le script createCube.py, (si vous avez une erreur lisez la ligne 2 sinon lisez la ligne 3).

2)	Autrement dé-commentez la ligne 13 et commentez la ligne 14, relancez le script autant de fois qu'il y a d'années en modifiant la valeur dans le tableau de la ligne 13.

3)	Afin de récupérer les données veuillez rediriger la sortie du script dans un fichier (./createCube.py > fichier_de_sortie.json).

4)	Une fois ces étapes réalisées vous vous retrouverez, en fonction de la méthode utilisée au-dessus, avec un ou plusieurs fichiers .json comportant(s) toutes les données des brevets.

5)	Dans le cas où vous n'auriez qu'un seul .json, vous n'avez pas besoin de faire l'aglomération de l'ensemble des fichiers grâce au script prepareDataForWords.py (sinon 6).

6)	Dans le cas où vous auriez plusieurs fichiers .json, lancez le script prepareDataForWords.py, il faut savoir que vous pouvez mettre plusieurs mots en paramètre de ce script exemple : prepareDataForWords.py premier_mot deuxieume_mot > nom_du_fichier_de_sortie.json. Afin de fusionner les résultats des mots précédemment rechercher, installer l'utilitaire jq (https://stedolan.github.io/jq/), voici la commande permettant de le faire : ./prepareDataForWords.py premier_mot deuxieme_mot > tmp.json && ./jq -s '.[0] * .[1]' mot_deja_recherche.json tmp.json > tmp2.json && mv tmp2.json mot_deja_recherche.json && rm tmp*



												-----------------------------------------
												--- PARTIE 2 : TRAITEMENT DES DONNEES ---
												-----------------------------------------

1)	Afin d'avoir un visuel sur l'ensemble des données, lancez le script interface.py.

2)	Une fois que la fenêtre est affichée, rentrez le mot dont vous voulez voir les données et choisissez votre type de graphique.

3)	Si vous voulez comparez plusieurs mots en même temps, retourner à l'étape 1 autant de fois que vous aurez de mots à analyser, sans fermez les fenêtres précédemment ouvertes.


Pour plus d'informations, vous pouvez nous contacter aux adresses suivantes :

phalftermeyer@cesi.fr
gabriel.amemoutou@viacesi.fr
christophe.pauly@viacesi.fr
philippe.billard@viacesi.fr
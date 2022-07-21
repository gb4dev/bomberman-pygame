import pygame
from pygame.locals import *
from constantes import *
class Niveau:
    """classe qui contient une fontion qui genere la carte
et une fonction qui l'affiche"""
    def __init__(self,fichier):
        self.structure=0
        self.fichier=fichier

    def generer(self):
        """Methode permettant de generer le niveau en fonction du fichier.
		On cree une liste generale, contenant une liste par ligne afficher"""	
            #On ouvre le fichier
        os.chdir(rep)
        with open(self.fichier, "r") as fichier :
                structure_niveau = []
                #On parcourt les lignes du fichier
                for ligne in fichier:
                        ligne_niveau = []
                        #On parcourt les sprites (lettres) contenus dans le fichier
                        for sprite in ligne:
                                #On ignore les "\n" de fin de ligne
                                if sprite != '\n':
                                        #On ajoute le sprite à la liste de la ligne
                                        ligne_niveau.append(sprite)
                        #On ajoute la ligne à la liste du niveau
                        structure_niveau.append(ligne_niveau)
                #On sauvegarde cette structure
                self.structure = structure_niveau

    def afficher(self, fenetre,mur,kure,bombe,explosion,vtrait,htrait):
            """Methode permettant d'afficher le niveau en fonction
            de la liste de structure renvoyee par generer()"""
            #On parcourt la liste du niveau
            mur=mur
            kure=kure
            bombe = bombe
            explosion = explosion
            vtrait=vtrait
            htrait=htrait
            num_ligne = 0
            for ligne in self.structure:
                    #On parcourt les listes de lignes
                    num_case = 0
                    for sprite in ligne:
                            #On calcule la position reelle en pixels
                            x = num_case * taille_sprite
                            y = num_ligne * taille_sprite
                            if sprite == 'm':		#m = Mur
                                fenetre.blit(mur, (x,y))
                            elif sprite== 'k':          #k = mur cassable
                                fenetre.blit(kure,(x,y))
                            elif sprite == 'b':
                                fenetre.blit(bombe,(x,y))
                            elif sprite == 'e' :
                                fenetre.blit(explosion,(x,y))
                            elif sprite == 'v' :
                                fenetre.blit(vtrait,(x,y))
                            elif sprite == 'h' :
                                fenetre.blit(htrait,(x,y))
                                
                            num_case += 1
                    num_ligne += 1

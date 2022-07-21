import pygame
from pygame.locals import *
from constantes import *
from niveau import *
from perso import *
from bombe import *

pygame.init()

fenetre=pygame.display.set_mode((450,330))


#chargement des images
os.chdir(rep+"\images")
image_mur = pygame.image.load("mur1.png").convert()
image_kure = pygame.image.load("kure.png").convert()
image_fond = pygame.image.load("herbe.jpg").convert()
image_perso = pygame.image.load("perso.png").convert()
image_perso.set_colorkey((255,255,255))
image_bombe = pygame.image.load("bombe.png").convert()
image_bombe.set_colorkey((255,255,255))
image_explosion = pygame.image.load("explosion.png").convert()
image_vtrait = pygame.image.load("vtrait.png").convert()
image_htrait = pygame.image.load("htrait.png").convert()

pygame.display.set_caption("bomberman")
pygame.display.set_icon(image_bombe)


horloge = pygame.time.Clock()

niveau=Niveau(fichier)
niveau.generer()
joueur1 = Perso((30,30),(1,1),image_perso)
joueur2 = Perso((390,270),(14,10),image_perso)
bombe = Bombe()
liste_joueurs=[joueur1,joueur2]
liste_directions=['bas','bas']
liste_bombes=[]

jeu = 1
continuer = 1

while continuer :
    while jeu :
        horloge.tick(30)
        for event in pygame.event.get():
            if event.type == QUIT :
                jeu=0
                continuer=0
            if event.type == KEYDOWN :
                if event.key == K_LEFT :
                    joueur1.bouger('gauche',niveau.structure)
                if event.key == K_RIGHT :
                    joueur1.bouger('droite',niveau.structure)
                if event.key == K_UP :
                    joueur1.bouger('haut',niveau.structure)
                if event.key == K_DOWN :
                    joueur1.bouger('bas',niveau.structure)
                if event.key == K_q :
                    joueur2.bouger('gauche',niveau.structure)
                if event.key == K_d :
                    joueur2.bouger('droite',niveau.structure)
                if event.key == K_z :
                    joueur2.bouger('haut',niveau.structure)
                if event.key == K_s :
                    joueur2.bouger('bas',niveau.structure)
                if event.key == K_SPACE :
                    liste_bombes.append(joueur1.poserbombe())
                if event.key == K_0 :
                    liste_bombes.append(joueur2.poserbombe())

                print(event.key)

                
        bombe.generer(liste_bombes)   
        indicejoueur=0
        for joueur in liste_joueurs:
            joueur.meurt(niveau.structure)
            if joueur.etat==True :
                niveau.structure=bombe.nettoyer(liste_bombes[0][0],liste_bombes[0][1])
                del liste_joueurs[indicejoueur]
                del joueur
            niveau.structure,liste_bombes=bombe.actualiser(niveau.structure)
            indicejoueur+=1
    


        fenetre.blit(image_fond,(0,0))
        niveau.afficher(fenetre,image_mur,image_kure,image_bombe,image_explosion,image_vtrait,image_htrait)
        for joueur in liste_joueurs:
            joueur.afficher(fenetre)
        pygame.display.flip()
                


pygame.quit()

from constantes import *
from pygame.locals import *
import pygame

class Perso() :
    """cree un personnage avec des fontions d'action"""
    def __init__(self,position,case,image_perso):
        self.posx = position[0]
        self.posy = position[1]
        self.casex = case[0]
        self.casey = case[1]
        self.nbombes = 1
        self.liste_bombes=[]
        self.image_perso= image_perso
        self.etat=False


    def afficher(self,fenetre):
        fenetre.blit(self.image_perso,(self.posx,self.posy))

            
    def bouger(self,direction,structure):
        if direction == 'droite' :
            #pour ne pas depasser l'ecran
            if self.casex < (nombre_sprite_ligne - 1):
                #on verifie si la case de destination est libre
                if structure[self.casey][self.casex+1] != 'm' and structure[self.casey][self.casex+1] != 'k' and structure[self.casey][self.casex+1] != 'b' :
                    #deplacement d'une case
                    self.casex += 1
                    #calcul de la position reelle en pixels
                    self.posx = self.casex * taille_sprite

        if direction == 'gauche':
            if self.casex > 0:
                if structure[self.casey][self.casex-1] != 'm' and structure[self.casey][self.casex-1] != 'k' and structure[self.casey][self.casex-1] != 'b' :
                    self.casex -=1
                    self.posx = self.casex * taille_sprite

        if direction == 'haut':
            if self.casey > 0:
                if structure[self.casey-1][self.casex] != 'm' and structure[self.casey-1][self.casex] != 'k' and structure[self.casey-1][self.casex] != 'b' :
                    self.casey -=1
                    self.posy = self.casey * taille_sprite

        if direction == 'bas':
            if self.casey < (nombre_sprite_colone-1):
                if structure[self.casey+1][self.casex] != 'm' and structure[self.casey+1][self.casex] != 'k' and structure[self.casey+1][self.casex] != 'b' :
                    self.casey += 1
                    self.posy = self.casey * taille_sprite

    def poserbombe(self):
        if len(self.liste_bombes) < self.nbombes:
            return [self.casex,self.casey,90,15,0]

    def meurt(self,structure):
        if structure[self.casey][self.casex]=='h' or structure[self.casey][self.casex]=='v' or structure[self.casey][self.casex]=='e':
            self.etat = True

            

        
                

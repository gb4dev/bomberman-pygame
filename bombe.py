from constantes import *
import pygame

class Bombe():

    def __init__(self):
        self.liste_bombes=[]
        self.structure=[]
        
        

    def generer(self,liste_bombes):
        self.liste_bombes=liste_bombes

    def actualiser(self,structure):
        self.structure=structure
        for element in self.liste_bombes :
            if element[4]==0:
                self.structure[element[1]][element[0]] = 'b'
                element[2] -= 1
            if element[2] == 0:
                element[3]-=1
                if element[4]==0:
                    self.structure=self.exploser(element[0],element[1],element[3])
                    element[4] = 1
                if element[3]==0:
                    self.structure=self.nettoyer(element[0],element[1])
                    del self.liste_bombes[0]

        return self.structure,self.liste_bombes

    def exploser(self,bombex,bombey,temps):
        self.structure[bombey][bombex] = 'e'
        #rangee du haut
        for k in range(1,3):
            if self.structure[bombey-k][bombex] == 'm':
                break
            elif self.structure[bombey-k][bombex] == '0':
                self.structure[bombey-k][bombex] = 'v'
            elif self.structure[bombey-k][bombex] == 'k':
                self.structure[bombey-k][bombex] = '0'
                break
            """elif self.structure[bombey-k][bombex] == 'b':
                self.exploser((bombey-k),bombex,15)
                break"""
        #rangee du bas
        for k in range(1,3):
            if self.structure[bombey+k][bombex] == 'm':
                break
            elif self.structure[bombey+k][bombex] == '0':
                self.structure[bombey+k][bombex] = 'v'
            elif self.structure[bombey+k][bombex] == 'k':
                self.structure[bombey+k][bombex] = '0'
                break
            """elif self.structure[bombey+k][bombex] == 'b':
                self.exploser((bombey+k),bombex,15)
                break"""
        #rangee de gauche
        for k in range(1,3):
            if self.structure[bombey][bombex-k] == 'm':
                break
            elif self.structure[bombey][bombex-k] == '0':
                self.structure[bombey][bombex-k] = 'h'
            elif self.structure[bombey][bombex-k] == 'k':
                self.structure[bombey][bombex-k] = '0'
                break
            """elif self.structure[bombey][bombex-k] == 'b':
                self.exploser(bombey,bombex-k,15)
                break"""
        #rangee de droite
        for k in range(1,3):
            if self.structure[bombey][bombex+k] == 'm':
                break
            elif self.structure[bombey][bombex+k] == '0':
                self.structure[bombey][bombex+k] = 'h'
            elif self.structure[bombey][bombex+k] == 'k':
                self.structure[bombey][bombex+k] = '0'
                break
            """elif self.structure[bombey][bombex+k] == 'b':
                self.exploser(bombey,bombex+k,15)
                break"""
        return self.structure
                        
                        
                
    def nettoyer(self,bombex,bombey):
        self.structure[bombey][bombex] = '0'
        #rangee du haut
        for k in range(1,3):
            if self.structure[bombey-k][bombex] == 'v':
                self.structure[bombey-k][bombex] = '0'
            else :
                break
        #rangee du bas
        for k in range(1,3):
            if self.structure[bombey+k][bombex] == 'v':
                self.structure[bombey+k][bombex] = '0'
            else :
                break
        #rangee de gauche
        for k in range(1,3):
            if self.structure[bombey][bombex-k] == 'h':
                self.structure[bombey][bombex-k] = '0'
            else :
                break
        #rangee de droite
        for k in range(1,3):
            if self.structure[bombey][bombex+k] == 'h':
                self.structure[bombey][bombex+k] = '0'
            else :
                break
        return self.structure

            



            
            

        

import pygame as pg
from escenas import Partida, Game_over,Pantalla_inicio  
from pygame import init 

pg.init()

class Game:
    
    def __init__(self, ancho=800, alto=600):
        pantalla = pg.display.set_mode((ancho, alto))
        pg.display.set_caption('The quest')
        pg.mixer.init()
        partida = Partida(pantalla)  #instancio clase Partida
        game_over = Game_over(pantalla) #instancio clase Game_over 
        pantalla_inicio = Pantalla_inicio(pantalla)  #instancio clase Pantalla_inicio
        
        self.escenas = [pantalla_inicio, partida, game_over]

    def lanzarpantalla(self):
        
        escena_activa = 0   #indice primero de la lista escenas, pantalla de inicio
        
        game_active = True
        
        while game_active:
           
            print(self.escenas[escena_activa])
            
            game_active = self.escenas[escena_activa].bucle_ppal()
            print(game_active)
            escena_activa += 1
           
            if escena_activa == len(self.escenas):
                escena_activa = 0
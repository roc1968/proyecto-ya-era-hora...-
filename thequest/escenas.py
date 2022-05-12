
import random
import pygame as pg

from thequest import niveles, HEIGHT, WIDTH, RED, GREEN, BLUE, WHITE, BLACK, FPS 
from entities import Fondo, niveles, Nave, Meteorito, Asteroide, Planeta, Explosion
import os, sys

pg.init()

fuente0 = pg.font.SysFont("Calibri", 20, False, False)
fuente1 = pg.font.SysFont("Arial black", 20, True, True)
fuente2 = pg.font.SysFont("Segoe print", 24, False, True)

FPS = 60

def draw_text(surface, texto, size, x, y):  
    
    font = pg.font.SysFont("serif", size)
    texto_surface = font.render(texto, True, WHITE)
    text_rect = texto_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(texto_surface, text_rect)   #llevas a la pantallala superficie creada que incluye el texto renderizado

def cargar_datos_baseSQL(self):
        
        with open("C:/Users/Rafael/Programar_desde_cero_KeepCoding/Proyecto_final/venv/thequest/jugadores.txt",'r') as f:
              
            try:
                self.puntos = int(f.read())       
            except:
                self.puntos = 0      #solo puntos enteros, porque son ok con el sistema de puntuación, que no admite decimales 


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.clock = pg.time.Clock()
            
    def bucle_ppal(self):
        pass

  
class Pantalla_inicio(Escena):    
    
    def __init__(self, pantalla):
        pg.Rect
        #self.pantalla = pantalla
        super().__init__(pantalla)
        
               
    def bucle_ppal(self):
            
        inicio = True        
        
        #estamos dentro del juego
        
        while inicio:  

            for event in pg.event.get():

                if event.type == pg.QUIT:
                    inicio = False
                    ejecutando = False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_z:
                        inicio = False
                        ejecutando = True      #entro en la partida con la tecla z
            
            self.pantalla.fill(BLUE)
            
            historia_instrucciones = [
  "THE QUEST" ,

            "La Tierra se muere... ",
            "La raza humana debe buscar otro planeta... ",
            "Tendrá que salvar, en su camino, meteoritos y asteroides... ",
            "¿Eres capaz de encontrar ese 'planeta deseado'?. ",
            
            "Pulsa 'tecla z' para empezar..., 'teclas w y s' para mover arriba y abajo tu nave' ",
            "Avanza en el juego aterrizando en un planeta nuevo.. "
            ]
            
            y = 100     # es fija, parto e una determinada altura de la pantalla
           
            for frase in historia_instrucciones:
                
                draw_text(self.pantalla, frase, 25, 400, y)                           
                y += 60

            pg.display.flip()
        
        return ejecutando                  #me ha funcionado....                
        #si false cruz pantalla, salida juego, si True debe enlazar con la escena principal del juego, la partida...


class Partida(Escena): 

    def __init__(self, pantalla):
        pg.Rect
        super().__init__(pantalla)    
        
        pg.display.set_caption("The Quest")
        	
        self.nave = Nave ()        
        
        
        self.load_data()
        
        
          
        #self.planeta = Planeta()        
        self.sprites = pg.sprite.Group()
        
        self.sprites.add(self.nave)
        #self.sprites.add(self.planeta)
        
        self.lista_asteroides= pg.sprite.Group()
        self.lista_meteoritos= pg.sprite.Group()    
        self.explosiones=pg.sprite.Group()
        
        self.fondo = Fondo()
        #self.fondo = pg.image.load(f"./resources/images/fondo_vertical.png")
        #intenté que se moviera y cree una clase............           
        
        self.reset()     
        
        pg.mixer.init()      
        self.musica_ambiente = pg.mixer.Sound(f"./resources/images/musica_juego.ogg")
        self.musica_ambiente.play()
        pg.mixer.music.set_volume(0.2)
        
        
        self.sonidos= [pg.mixer.Sound(f"./resources/images/Explosion+2.wav"), 
                                pg.mixer.Sound(f"./resources/images/Explosion+7.wav"),
                                pg.mixer.Sound(f"./resources/images/Explosion+8.wav"),
                                pg.mixer.Sound (f"./resources/images/Explosion+9.wav")]     
       
        
        
        self.tamaño = random.randrange (1,5)   
        #quiero un tamaño de la explosion aleatorio, entre cuatro posibles.
        
        self.expl_anim = {'t1':[], 't2':[], 't3':[], 't4':[]}  #diccionario con 4 listas de expl de distintos tamaños (el tamaño es la clave del dic.) , de 24 imagenes cada lista, jugando con el tamaño de la imagen original
  
        for i in range(24):    #hay 24 imagenes de cada tipo de explosion: de la 00 a la23
            
            file = "resources/images/expl_01_{:04d}.png".format(i)   #4 digitos 01-0001 y así hasta 01_0023
            imagen = pg.image.load(file).convert_alpha()    #las cargo
            imagen.set_colorkey(BLACK)

            imagen_t1 = pg.transform.scale(imagen, (32, 32))   #las hago más pequeñas que su tamaño original
            self.expl_anim['t1'].append(imagen_t1)
            
            imagen_t2 = pg.transform.scale(imagen, (64, 64))   #las hago algo menos más pequeñas, tamaño 2
            self.expl_anim['t2'].append(imagen_t2)
             
            imagen_t3 = pg.transform.scale(imagen, (128, 128))   #las hago más grandes
            self.expl_anim['t3'].append(imagen_t3)
            
            imagen_t4 = pg.transform.scale(imagen, (256, 256))   #las hago todavia mas grandes
            self.expl_anim['t4'].append(imagen_t4)
            

    def reset(self):                  
        
        self.sprites.empty()
        self.lista_meteoritos.empty()
        self.lista_asteroides.empty()
        self.sprites.add(self.nave)
        self.nave.vidas = 3  
        self.nave.girando == False
        self.nave.viva = True
        
  
    def crea_meteoritos(self, nivel):  #voy a crear meteoritos dependiendo del nivel   
        
        self.lista_meteoritos = []
        delta = 4
        
        for nivel in niveles: 
            
            self.meteoritos = delta * (nivel, nivel * (1+nivel^2))            
            
            self.meteoritos = Meteorito()
            self.lista_meteoritos.append(self.meteoritos) 
        self.sprites.add(self.lista_meteoritos) 
          
    
    def crea_asteroides(self, nivel):       
        
        self.lista_asteroides = []
        delta_uno = 6
        
        for nivel in niveles: 
            
            self.numero_asteroides = delta_uno * (nivel, nivel * (1+nivel^3))   
            
            self.asteroides = Asteroide()
            self.lista_asteroides.append(self.asteroides) 
        self.sprites.add(self.lista_asteroides)    
               
    
    
    
    def bucle_ppal(self):               
        
        tiempo_seg = 0 
        record = 0
        puntosn1 = 0
        puntosn2 = 0
        nivel = 1
        self.reset()
         
        ejecutando = True     #para que enlace con pantalla de inicio, ya que el while de la pantalla de inicio return ejecutando
        game_over = False
        
        while (self.nave.vidas > 0 and nivel <= 2) and (ejecutando ==True and tiempo_seg <= 50):            #hemos pasado de nivel
            
            tiempo_seg = pg.time.get_ticks()//1000    #calculo el tiempo del juego en segundos
	            
            print(tiempo_seg)
            
            puntosn2 += (20 * tiempo_seg)                 
            
            self.crea_meteoritos(nivel)      #hace falta invocarla en cada nivel del juego....
            self.crea_asteroides(nivel)
          
            if tiempo_seg == 50:
                self.planeta = Planeta()
                self.sprites.add(self.planeta)
                self.nave.girando = True
                draw_text("Nave girando/aterrizando", 25, self.pantalla,(700,500))    

            
            while (self.nave.vidas > 0 and tiempo_seg <= 20 and ejecutando == True):     #en microsegundos, por tanto, 20 segundos 
                  
                tiempo_seg = pg.time.get_ticks()//1000    #calculo el tiempo del juego en segundos
	            #tiempo transcurrido desde que se ejecutó pygame.init()
                
                print(tiempo_seg)
                #para calcular los puntos en cada segundo:
                
                puntosn1 += (10 * tiempo_seg) 
              
                self.crea_meteoritos(nivel)
                self.crea_asteroides(nivel)
                   
                for event in pg.event.get():
                   
                    if event.type == pg.QUIT:
                        game_over = True
                            
                    if event.type == pg.KEYDOWN:
                       
                        if event.key == pg.K_p:    #presiono tecla p", quiero que me muestre el fondo
                            self.pantalla.blit(self.fondo,(0, 0))    #lo quiero el fondo, estático
                            draw_text("Nivel 2..¡¡Adelante!!..", self.pantalla, 40, (WIDTH//2, HEIGHT //2)) 
                            self.pantalla.flip()                        
                            #nivel +=1       #no sé si hay que repetir este codigo aqui...
                            #self.sprites.empty()
                            #self.lista_meteoritos.empty()
                            #self.lista_asteroides.empty()
                            #self.sprites.add(self.nave)                             
                            #self.nave.reset()

                if tiempo_seg ==20:    
                    
                    self.nave.girando = True

                    draw_text("Nave girando/aterrizando", 25, self.pantalla,(700,500))
                    draw_text("Pulse tecla 'p' para pasar al siguiente nivel",25,self.pantalla,(700,300))
                    self.planeta = Planeta()   #instancio aqui el planeta, sólo aquí en este momento
                    self.sprites.add(self.planeta)            
                
                self.sprites.update()    
                
                #colisiones:
                
                colisiones_nave_meteoritos= pg.sprite.spritecollide(self.nave, self.lista_meteoritos, True)
            
                if colisiones_nave_meteoritos:
                
                        if self.nave.girando == False:      #solo colisiones si la nave no esta girando	
                            
                            self.explosion = Explosion(self.nave.rect.center,f't{self.tamaño}')    #instancio el objeto explosion en el centro de la nave y con el f string slecciono un tamaño aleatorio (1,2,3,4)de las imagenes de la explosion 
                            self.sonidos[random.randrange(0,4)].play()  #elijo un sonido aleatorio
                            self.sprites.add(self.explosion)   
                            self.nave.vidas -= 1
                            self.nave.viva = False
                            self.nave.reset()
                            
                            if self.nave.vidas <= 0:
                                game_over = True
                        
                            else:    
                                self.nave.viva = True
                                game_over = False

                        else:  #si la nave esta girando, entonces mo hay explosion y la nave está viva...
                            self.nave.viva = True
                
                colisiones_nave_planeta= pg.sprite.spritecolliderect(self.nave, self.planeta, False) 	
                
                if colisiones_nave_planeta:

                    self.nave.viva = True    #no hay explosion de la nave.... 

                colisiones_nave_asteroides= pg.sprite.spritecollide(self.nave, self.lista_asteroides, True)
            
                if colisiones_nave_asteroides:
                
                        if self.nave.girando == False:	
                            
                            self.explosion = Explosion(self.nave.rect.center,f't{self.tamaño}') #elige aleatoriamente el tamaño de la explosion de la nave
                            self.sonidos_aletorios[random.randrange(0,4)].play()
                            self.sprites.add(self.explosion)   
                            self.nave.vidas -= 1
                            self.nave.viva = False
                            self.nave.reset()
                            
                            if self.nave.vidas <= 0:
                                game_over = True
                        
                            else:    
                                self.nave.viva = True
                                game_over = False    
                        else:
                            self.nave.viva = True
        
            #podria haber hecho una funcion entre col nave/meteoritos----nave/asteroides   
               
                 
                colisiones_asteroides_meteoritos= pg.sprite.groupcollide(self.lista_asteroides, self.lista_meteoritos, True, True)
                
                if colisiones_asteroides_meteoritos:
                    
                    self.explosion = Explosion(self.meteoritos.rect.center,f't{self.tamaño}') #elige aleatoriamente el tamaño de la explosion de la nave
                    self.sonidos_aletorios[random.randrange(0,4)].play()
                    self.sprites.add(self.explosion)   
                    self.sprites.remove(self.lista_asteroides)
                    self.sprites.remove(self.lista_meteoritos)
             
                self.fondo.update()
                self.fondo.pintar()
                
                self.sprites.draw(self.pantalla)
                       
                texto1 = "Nivel: " + str(nivel)
                texto2 = "Vidas: " + str(self.nave.vidas)
                
                texto3 = "Score: " + str(puntosn1 + puntosn2)
                texto4 = "High Score: " + str(record)
                
                draw_text(texto1, 20, self.pantalla, 750, 5)
                draw_text(texto2, 20, self.pantalla, 750, 15)
                draw_text(texto3, 20, self.pantalla, 5, 1)    #en la esquina superior izquierda   
                draw_text(texto4, 20, self.pantalla,750 ,25)    
                       
                
                pg.display.flip()
                                 
            nivel +=1
            self.sprites.empty()
            self.lista_meteoritos.empty()
            self.lista_asteroides.empty()
            self.sprites.add(self.nave)   
            self.nave.reset()
            
        return game_over                          #para enlazar con la siguiente pantalla



class Game_over(Escena):

    def __init__(self, pantalla):
        pg.Rect
        self.pantalla = pantalla
        super().__init__(pantalla)
        
        self.fuente = pg.font.SysFont("calibri", 25)

    def bucle_ppal(self):
          
        game_over = True     #enlazo escena principal y game over
         
        while game_over:    
                
            for event in pg.event.get():
                
                if event.type == pg.QUIT:
                    game_over = True
                    inicio = False                   
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_N:
                        game_over = True
                        inicio = False                         
                   
                    if event.key == pg.K_S:
                        game_over = True
                        inicio = True
                        
        
            if (self.puntosn1+self.puntosn2) > record:   #en este caso la puntuacion obtenida, por fuerza, es mayor de las cinco almacenadas

                record = (self.puntosn1+self.puntosn2)   #el nuevo marcador sustituye al record
                draw_text("NUEVO RECORD!!!", 25, self.pantalla, WIDTH // 2, HEIGHT // 2 )

                self.pantalla.fill(RED)    
                draw_text()
            
            
            
                with open("C:/Users/Rafael/Programar_desde_cero_KeepCoding/Proyecto_final/venv/thequest/jugadores.txt" 'w') as f:
                    f.write(str(self.puntosn1+self.puntosn2))    #ACTUALIZAMOS LOS RECORDS CON EL NUEVO RECORD
            
            else:
                draw_text("High Score: " + str(record), 20, WIDTH / 2, HEIGHT / 2 )
                                
            historia_perder = [
            
            "GAMEOVER " ,
            
            "No has conseguido llegar a un planeta compatible con la vida humana. ",
            "Los meteoritos/asteroides te han impedido lograrlo. ",
            "No te quedes con las ganas.......  ",
            "¿Quieres volverlo a intentar? ",
            
            "Pulsa 'S' para volverlo a intentar ",
            "Pulsa 'N' para salir del juego ",                 
            ]

            historia_ganar = [

            "¡¡¡¡ FELICIDADES MASTER DEL UNIVERSO !!!. ",

            "Has conseguido llegar a un planeta compatible con la Tierra. ",
            "Los asteroides / meteoritos no te han destruido. ",
            "Te has convertido en un héroe de la especie humana. ",
            
            "¿Quieres embarcarte en una nueva misión? ",
                
            "Pulsa 'S' para volver a jugar ",
            "Pulsa 'N' para salir del juego "
            ]
          
            ganar = True
            
            if self.nave.vidas == 0:
                ganar = False    
                
           
            elif len(niveles)>2:
                ganar = True
                
           
            if ganar:   
                relato = historia_ganar
            else:
                relato = historia_perder

            y = 40
            
            for frase in relato:
                
                draw_text(self.pantalla, frase, 20, 100, y)  
                
                y += 40
                        
            pg.display.update() 
            
        return inicio                #para enlazar con la pantalla de inicio


pg.quit()


#He llegado hasta aqui, no funciona como cabía esperar, he ido probando alguna cosa aislada, pero no me ha sido posible dedicar el tiempo necesario.    
#Quedo pendiente, entre otras cosas, hacer un inputbox, para que el jugadgor en caso de que puntuacion sea mayor que las5 de la base de datos, meta sus inciales.
#He mirado mucho por Internet y he visto la forma de hacerlo. 

class TextInputBox(pg.sprite.Sprite):
    # [...]

    def update(self, event_list):
        for event in event_list:
            if event.type == pg.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pg.KEYDOWN and self.active:
                if event.key == pg.K_RETURN:
                    self.active = False
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]  #borra el ultimo caracter que ha introducidoel usuario???
                else:
                    self.text += event.unicode
                
                
                
                self.render_text()


event_list = pygame.event.get()
for event in event_list:
    if event.type == pygame.QUIT:
        run = False
group.update(event_list)

import pygame as pg
from pygame.locals import *
import random
import sys
import os
from thequest import FPS, niveles, RED, GREEN, BLACK, WHITE, BLUE 
#lo que no está iluminado no haria falta porque no se usa



WIDTH= 800
HEIGHT= 600



def draw_text(surface, texto, size, x, y):  
    
    font = pg.font.SysFont("serif", size)
    texto_surface = font.render(texto, True, WHITE)
    text_rect = texto_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(texto_surface, text_rect)   #llevas a la pantalla la superficie creada que incluye el texto renderizado



'''class Viñeta(pg.sprite.Sprite):
    
    def __init__(self, pantalla):
        super().__init__()
        self.pantalla = pantalla
		
	def colisiona (self, otro) -> bool:
        if self.rect.w > otro.rect.w:
            menor_ancho = otro
            mayor_ancho = self
        else:
            menor_ancho = self
            mayor_ancho = otro

        if self.rect.h > otro.rect.h:
            menor_alto = otro
            mayor_alto = self
        else:
            menor_alto = self
            mayor_alto = otro
        return (menor_ancho.rect.left in range(mayor_ancho.rect.left, mayor_ancho.rect.right) or \
                menor_ancho.rect.right in range(mayor_ancho.rect.left, mayor_ancho.rect.right)) and \
               (menor_alto.rect.top in range(mayor_alto.rect.top, mayor_alto.rect.bottom) or \
                menor_alto.rect.bottom in range(mayor_alto.rect.top, mayor_alto.rect.bottom))
'''  
#no la voy a utilizar.... 

abajo = True
arriba = True
derecha = True

class Meteorito(pg.sprite.Sprite):
	
	def __init__(self):    
		super().__init__()
		
		meteoritos_images = []     #lista vacía que tendrá las imágenes de la lista de los meteroitos
		meteoritos_list = [f"./resources/images/meteor_small1.png", f"./resources/images/meteor.png", f"./resources/images/meteoro_diminuto.png", f"./resources/images/meteoro_grande2.png", f"./resources/images/meteoro_big1.png", f"./resources/images/meteoro_big2.png"]
				
		for imagen in meteoritos_list:
			meteoritos_images.append(pg.image.load(imagen).convert()) #añadesa la lista cada imagen cargada 
		
		self.image = random.choice(meteoritos_images)   #de la lista de imagenes, elige aleatoriamente una imagen....
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = (WIDTH - self.rect.width)   #para que se vea entero desde el margen derecho de la pantalla
		self.rect.y = random.randrange(0, HEIGHT-self.rect.y)  #salen en alturas aleatorias   
		self.vy = 0
		self.vx = random.randrange(1, 6)   #velocidad aleatoria de 1 a 4, mov horizontal hacia atras, vx en negativo
		
		
	def update(self):
		
		self.rect.x -= self.vx
		self.rect.y += self.vy       #no le afecta
		
		if self.rect.x < 0:  #se ha esquivado por la nave, desaparece de la pantalla el meteorito
			
			self.rect.x = (WIDTH - self.rect.width)
			self.rect.y = random.randrange(0, HEIGHT-self.rect.y)
			self.vy = 0
			self.vx = random.randrange(2, 11)
		    #que sigan apareciendo pero con una velocidad mas alta....
				
		
class Asteroide(pg.sprite.Sprite):      #muy parecida, solo cambia el numero de imagenes y la velocidad
	
	def __init__(self):
		super().__init__()
		
		asteroides_images = []
		asteroides_list = [f"./resources/images/asteroide4.png", f"./resources/images/asteroide3.png"]

		for imagen in asteroides_list:
			asteroides_images.append(pg.image.load(imagen).convert_alpha())	
		
		self.image = random.choice(asteroides_images)
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = (WIDTH - self.rect.width)
		self.rect.y = random.randrange(0, HEIGHT-self.rect.y)
		self.vy = 0
		self.vx = random.randrange(3, 16)
		

	def update(self):
		self.rect.x -= self.vx
		self.rect.y += self.vy

		if self.rect.x < 0:   #se ha esquivado por la nave
			
			self.rect.x = (WIDTH - self.rect.width)
			self.rect.y = random.randrange(0, HEIGHT-self.rect.y)
			self.vy = 0
			self.vx = random.randrange(4, 18)
		

class Nave(pg.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
			
		self.image = pg.image.load(f"./resources/images/nave1.png").convert_alpha()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		
		self.x = 0
		self.rect.centery = (HEIGHT // 2), #tiene que aparecer siempre al inicio de la partida/nivel en estas coordenadas,según instrucciones	
		
		self.vy = -5   #mov. hacia arriba (sólo vy y negativo), viceversa si baja....
		self.vx = 0    #no desplazam. horizontal 
		
		
		self.vidas = 3
		self.viva = True 
		#inicialmente la nave "esta viva" y no va a girar"
		self.girando = False
		self.paso_giro = 0
		
	
	def update(self):	
		
		if self.girando ==False:      #es decir, como va a estar, salvo al final de cada nivel:
			
			teclas = pg.key.get_pressed()       #se maneja por teclado

			if teclas[pg.K_UP]:    
				self.rect.y += self.vy        #segun lo expuesto
			if teclas[pg.K_DOWN]:
				self.rect.y -= self.vy
			if teclas[pg.K_RIGHT]:               #tecla dcha. no desplaz.
				self.rect.x +=self.vx
			if teclas[pg.K_LEFT]:                #tecla izda no desplaz.
				self.rect.x -= self.vx
			if teclas[pg.K_LSHIFT] and [pg.K_UP] or [pg.K_DOWN]:	#si presiono a la vez la tecla shift izdo y una de las teclas de mov. la nave, va mucho mas deprisa.. 
				self.rect.x += 2 * self.vy

			if teclas[pg.KEYUP]:  
					if teclas in (pg.K_UP, pg.K_DOWN):
						self.vy = 0       #si levanto la tecla de arriba/abajo, la nave se para.

			if self.rect.top < 0:   #evitar que se salga la nave por arriba. 
				self.rect.top = 0
		
			if self.rect.bottom > HEIGHT:	  # evitar que nave se salga la nave por abajo de la pantalla
				self.rect.bottom = HEIGHT
			
		else:	#la nave esta girando..:primero traslacion y luego giro	
			
			draw_text(self.pantalla, "Nave aterrizando", 20, (500, 150))   #en esa posicion, texto color blanco por la funcion invocada y prev. definida...
		
			if abajo == True:
				if self.rect.centery < (HEIGHT // 2):
					self.vy = 2
					self.rect.centery += self.vy
				else:
					abajo = False
		
			if arriba == True:	
				if self.rect.centery > (HEIGHT // 2): 
					self.vy = -2
					self.rect.centery += self.vy
				else:			
					arriba = False		

			if derecha ==True:
						#if self.rect.centery==HEIGHT//2, mov. traslacion de la nave L, mejor no dejando el centroy fijo, más bonito....	
				
				if self.x < 500:       			
					self.vx = 2			
					self.x += self.vx	
					self.vy = 0
				else:					
					derecha == False
		
			draw_text(self.pantalla,"Nave tras mov. traslacion ,empieza a girar y aterriza", 20, (600, 400))								
		
		
			if self.paso_giro == 0:    #no ha empezado a girar
			
				self.centro = self.image.get_rect().center   #obtenemos el centrox, centro y de la imagen de la nave a rotar
	
			elif self.paso_giro <=60:
		
				self.imagen_rotada = pg.transform.rotate(self.image, 3* self.paso_giro)
				self.rect = self.imagen_rotada.get_rect(center = self.centro)			
		
			else:     
				self.imagen_rotada = self.image    #la imagen no rotada  	
				self.paso_giro = -1
			self.paso_giro += 1 

	
	def reset(self):       #al inio de partida, situación y atributos de la nave		
		self.x = 0                             #pos. inicial
		self.rect.centery = (HEIGHT // 2)	
		self.vy = -5
		self.vx = 0
		self.vidas = 3                              
		self.girando = False
		self.paso_giro = 0


class Explosion(pg.sprite.Sprite):

	def __init__(self, center, tamaño): #centrada la explosion en el centro de la nave, tengo varios tamaños de explosiones hechos con 24 imagenes de una explosion 
		super().__init__()
		
		self.tamaño = tamaño
		self.image = self.expl_anim[self.tamaño][0]   #primera imagen de expls con el tamaño solicitado
		self.rect = self.image.get_rect()
		self.rect.center = center

		self.imagen_activa = 0     #la primera imagen cargada en la lista
		self.frec_cambio_imagen_activa = 30     #por ejemplo, regula la velocidad de cambio de imagen 
		self.ultima_actualizacion = pg.time.get_ticks()     #en milisegundos....
	   
	
	def update(self):
	    
		now = pg.time.get_ticks()
		
		if now - self.ultima_actualizacion > self.frec_cambio_imagen_activa:
			
			self.actualizacion = now
			
			self.imagen_activa += 1   #logico, pasa siguiente imagen de la lista
			
			if self.imagen_activa == len(self.expl_anim[self.tamaño]):
				self.kill()     #adios a la explosion, logico se han acabado las imagenes....
			
			else:
				center = self.rect.center    #la centra la explosion, sino ha acabado la secuencia de 24 imagenes
				self.image = self.expl_anim[self.tamaño][self.imagen_activa]
				self.rect = self.image.get_rect()
				self.rect.center = center
      


class Planeta(pg.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		
		self.image = pg.image.load(f"./resources/images/planeta1.jpg").convert()
		self.image.set_colorkey(BLACK)   #queda muy mal, pero????
		self.imagen_scale = pg.transform.scale(self.image, (80, 80))   #reduzco algo el tamaño de la foto
		self.rect = self.image.get_rect()   
		
			
		self.rect.center = (1000, HEIGHT //2)
	
		self.vy = 0
		self.vx = -0.1     #


	def update(self):       #movimiento del planeta
		
		if self.rect.centerx > (WIDTH - self.rect.x//3) and (self.rect.centery == HEIGHT //2):	
		
			self.rect.x += self.vx
			self.rect.centery += self.vy
		
		else:
			pass   
			

		       #mi idea es que el planeta se situe con su centro en la coordenada (600,300)   	

class Fondo():    #con dos iagenes de fondo voy a ver si puedo hacer como si se mueve el fondo del juego...
	def __init__(self, pantalla):
		self.pantalla = pantalla
		self.fondoimage = pg.image.load(f"./resources/images/fondo_vertical.png")	
		self.rectfondoimage = self.fondoimage.get_rect()   #la surface
		
		self.x1 = 0    
		self.y1 = 0      #primer fondo
	
		self.x2= 0
		self.y2= -self.rectfondoimage.height   #el fondo 2 esta encima precediendo a la imagen inicial del fondo, que esta en (cero, cero) 

		self.velocidad = 30   #pixeles/seg. 
	
	def update(self):    #desplazo los dos fondos de pantalla hacia abajo 30 pixeles/segundo, por eso la x esta fija 
		
		self.y1 += self.velocidad
		self.y2 += self.velocidad       #bajan las dos imagenes a una tasa constante
		
		
		if self.y1 > self.rectfondoimage.height:    
   			self.y1 = -self.rectfondoimage.height                           
		if self.y2 > self.rectfondoimage.height:              #????? no se me quita el error de identación...		
			self.y2 = -self.rectfondoimage.height

	
	def pintar(self):		
		self.pantalla.blit(self.rectfondoimage,(self.x1, self.y1))

		self.pantalla.blit(self.rectfondoimage(self.x2, self.y2))       

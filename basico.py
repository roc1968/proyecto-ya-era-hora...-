import pygame as pg


WIDTH = 600
HEIGHT = 800
size = (600,600)
pantalla= pg.display.set_mode(size)
running = True
fondo = pg.image.load(f"./resources/images/fondo_vertical.png")
image = pg.image.load(f"./resources/images/nave1.png").convert_alpha()
rect = image.get_rect()
corx=100
cory=50
vy=2
abajo = True
arriba = True
derecha = True
paso_giro=0
girando = False



while running:
    for event in pg.event.get():
        print(event)
        if event.type == pg.QUIT:
            running = False    
    
       
       
    if abajo == True:
        if cory < 300:
            vy = 2
            vx=0
            cory += vy
    else:
        abajo = False

    if arriba == True:
        if cory >300:
            vy = -2
            vx=0
            cory += vy
            
        else:
            arriba = False        
    
    #if cory==300:
    if derecha == True:
        if corx < 400:
            vx= 2
            corx+=vx
            vy=0
        else:
            derecha = False
     
     
    if girando ==True:    
            
        if paso_giro == 0:
            
            centro = image.get_rect().center   #obtenemos el centrox, centro y de la imagen de la nave a rotar
            print(centro)
        
        elif paso_giro <= 60:
            
            imagen_rotada = pg.transform.rotate(image,3 * paso_giro)
            rect_img_rot = imagen_rotada.get_rect(center=centro)			
    
        else:
            girando = False		
            imagen_rotada = image    	
            paso_giro = -1
        paso_giro += 1 
	
    else:
        teclas = pg.key.get_pressed()
        if teclas[pg.K_UP]:    
            rect.y += vy 
        if teclas[pg.K_DOWN]:
            rect.y -= vy
        if teclas[pg.K_RIGHT]:
            rect.x +=vx
        if teclas[pg.K_LEFT]:
            rect.x -= vx
        if teclas[pg.K_LSHIFT] and [pg.K_UP] or [pg.K_DOWN]:	
            rect.x += 2 * vy

        tecla_lev = pg.KEYUP
        if teclas in (pg.K_UP, pg.K_DOWN):
            vy = 0

        if rect.top < 0:   #evitar que se salga la nave por arriba 
            rect.top = 0
        
        if rect.bottom > HEIGHT:	  # que se salga por abajo
            rect.bottom = HEIGHT

    





    
    
    
    pantalla.blit(fondo, (0,0))
    pantalla.blit(image,(corx, cory))
    
    
    
    pg.display.flip()
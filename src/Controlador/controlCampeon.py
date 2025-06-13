import pygame

CELDA_ANCHO = 80
CELDA_ALTO =  80

class controlCampeon:

    def __init__(self, vista_campeon):
        self.vista = vista_campeon
        self.x = vista_campeon.x
        self.y = vista_campeon.y
        self.rect = vista_campeon.rect
    

    def movimiento(self, direccion, cantidad):
        "Mueve el personaje en la dirección indicada por las casillas"
        if(direccion == "up"):
            self.y -= cantidad * CELDA_ALTO
        if(direccion == "down"):
            self.y += cantidad * CELDA_ALTO
        if(direccion == "left"):
            self.x -= cantidad * CELDA_ANCHO
        if(direccion == "right"):
            self.x += cantidad * CELDA_ANCHO
            
        self.rect.topleft = (self.x, self.y)
    
    def colision(self, another_champion, proximo_x, proximo_y):
        "Verifica que los campeones no se superpongan"
        temp_rect = self.rect.copy()
        temp_rect.topleft = (proximo_x, proximo_y)
        return temp_rect.colliderect(another_champion.rect)
    
    def mover(self, direccion, cantidad, otro_campeon, max_x, max_y):
        prox_x = self.x
        prox_y = self.y
        if direccion == "up":
            prox_y -= cantidad * CELDA_ALTO
        elif direccion == "down":
            prox_y += cantidad * CELDA_ALTO
        elif direccion == "left":
            prox_x -= cantidad * CELDA_ANCHO
        elif direccion == "right":
            prox_x += cantidad * CELDA_ANCHO
        
        if not (0 <= prox_x < max_x * CELDA_ANCHO and 0 <= prox_y < max_y * CELDA_ALTO):
            return False
        
        if self.colision(otro_campeon, prox_x, prox_y):
            return False
        
        self.x = prox_x
        self.y = prox_y
        self.rect.topleft = (self.x, self.y)
        self.vista.x = self.x
        self.vista.y = self.y
        self.vista.rect.topleft = (self.x, self.y)
        return True
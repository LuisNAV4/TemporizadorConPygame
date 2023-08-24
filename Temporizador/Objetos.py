import pygame

class Label:
    def __init__(self, x, y, Texto, TamañoFuente):
        self.Posicion = (x,y)
        self.Text = Texto
        self.font = pygame.font.SysFont("arial",TamañoFuente)
    
    def Dibujar(self, screen):
        TextoRender = self.font.render(self.Text,True,(255,255,255))
        screen.blit(TextoRender, self.Posicion)

class Botones:
    def __init__(self, x, y, width, height, Texto):
        self.rect = pygame.Rect(x,y,width, height)
        self.texto = Texto
        self.color_normal = (100,100,100)
        self.color_presionado = (200,200,200)
        self.font = pygame.font.SysFont("arial",20)
        self.presionado = False
        self.visible = True
        
    def Dibujar(self, screen):
        color = self.color_presionado if self.presionado else self.color_normal
        pygame.draw.rect(screen,color,self.rect)
        
        Texto_render = self.font.render(self.texto,True,(255,255,255))
        Texto_rect = Texto_render.get_rect(center= self.rect.center)
        screen.blit(Texto_render,Texto_rect)
        
    def verificar_clic(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.presionado = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.presionado = False   
            
class AsignarTiempo:
    def __init__(self,x,y,width,height,Tiempo):
        self.rect = pygame.Rect(x,y,width,height)
        self.Texto = Tiempo
        self.color = (200,200,200)
        self.font = pygame.font.SysFont("arial",60)
        self.colorText = (0,0,0)
    
    def Dibujar(self, screen):
        colorText = self.colorText
        ColorMarco = self.color
        pygame.draw.rect(screen,ColorMarco,self.rect)
        TextoRender = self.font.render(self.Texto,True,colorText)
        TextoRect = TextoRender.get_rect(center = self.rect.center)
        screen.blit(TextoRender,TextoRect)
           
class Ventanas:
    Visible = None
        
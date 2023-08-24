import pygame
import datetime
import os
from Objetos import *

def ActualizarHora():
    HoraActual = datetime.datetime.now()
    if (HoraActual.hour < 10):
        Hora = f"0{HoraActual.hour}"
    else:
        Hora = HoraActual.hour
    if (HoraActual.minute < 10):
        Minuto = f"0{HoraActual.minute}"
    else: 
        Minuto = HoraActual.minute
    if (HoraActual.second < 10):
        Segundo = f"0{HoraActual.second}"
    else: 
        Segundo = HoraActual.second
    return Hora,Minuto,Segundo

def SonidoAlarma():
    pygame.mixer.music.load("Sonidos/Morning Flower - Tono de Alarma Samsung.mp3")
    pygame.mixer.music.play(loops=1)

    
def CalculoTemporizador(Hora,Minuto,Segundo, Finalizado, SegundoReal,Comparacion,Alarma):
        if Segundo < 0:
            Segundo = 59
        if Hora == 0 and Minuto == 0 and Segundo == 0:
            Finalizado = False
            Alarma = True
        else:
            if SegundoReal != Comparacion:
                Segundo -= 1
                
                if Segundo <= 0 and Minuto != 0:
                    Minuto -= 1
                    Segundo = 59
                if Minuto <= 0 and Hora != 0:
                    Hora -=1
                    Minuto = 59
                Comparacion = SegundoReal
         
        return Hora,Minuto,Segundo, Finalizado,Comparacion, Alarma
            
def CalculoParaBotonesUP(Tiempo):
    TiempoTexto = "00" 
    Tiempo += 1
    if Tiempo < 10:
        TiempoTexto = f"0{Tiempo}"
    else: 
        TiempoTexto = Tiempo
    if Tiempo >= 60:
        Tiempo = 0
        TiempoTexto = f"0{Tiempo}"
        
    return Tiempo, TiempoTexto
        
def CalculoParaBotonesDOWN(Tiempo):
    TiempoTexto = "00" 
    if Tiempo > 0:
        Tiempo -= 1
        if Tiempo < 10:
            TiempoTexto = f"0{Tiempo}"
        else: 
            TiempoTexto = Tiempo
    else:
        Tiempo = 59
        TiempoTexto = Tiempo

    return Tiempo,TiempoTexto
    
        

    
def AparecerTemporizador():
    HoraSistema.Dibujar(screen)
      
    HoraBox.Dibujar(screen)
    HoraText.Dibujar(screen)
    
    MinutoBox.Dibujar(screen)
    MinutoText.Dibujar(screen)
    
    SegundoBox.Dibujar(screen)
    SegundoText.Dibujar(screen)
    
    
def AparecerBotones():
    BotonHoraDown.Dibujar(screen)
    BotonHoraUP.Dibujar(screen)

    BotonMinutoUP.Dibujar(screen)
    BotonMinutoDown.Dibujar(screen)

    BotonSegundoUP.Dibujar(screen)
    BotonSegundoDown.Dibujar(screen)
  
    BotonEmpezar.Dibujar(screen)

    
    
def AccionBotones():
    BotonHoraDown.verificar_clic(event)
    BotonHoraUP.verificar_clic(event)
    
    BotonMinutoUP.verificar_clic(event)
    BotonMinutoDown.verificar_clic(event)
    
    BotonSegundoUP.verificar_clic(event)
    BotonSegundoDown.verificar_clic(event)
    
    BotonEmpezar.verificar_clic(event)
#Inicio Pygame
pygame.init()

#Especificaciones de la Ventana
width, height = 600, 400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Temporizador")
icon = pygame.image.load("Icon/icon.png")
pygame.display.set_icon(icon)
os.system('CLS')

#Objeto Fuente Para Hora
fuenteHora = pygame.font.SysFont("arial",23)
TextoHora = "La Hora actual es: 00:00:00"
#DISEÑO DE BOTONES
BotonHoraUP = Botones(15,100,160,30, "+") 
BotonHoraDown = Botones(15,260,160,30, "-") 

BotonMinutoUP = Botones(215,100,160,30, "+") 
BotonMinutoDown = Botones(215,260,160,30, "-")

BotonSegundoUP = Botones(415,100,160,30, "+") 
BotonSegundoDown = Botones(415,260,160,30, "-")

BotonEmpezar = Botones(215,340,160,30,"Empezar")

BotonDetener = Botones(380,340,160,30,"Stop")
BotonPausar = Botones(215,340,160,30, "Pausar")

BotonAlarma = Botones(500,20,80,30,"Alarma")


#DISEÑO NUMEROS
HoraBox = AsignarTiempo(15,130,160,130, "00")
MinutoBox = AsignarTiempo(215,130,160,130, "00")
SegundoBox = AsignarTiempo(415,130,160,130, "00")
HoraTemp = 0
MinutoTemp = 0
SegundoTemp = 0
TiempoHora = "00"
TiempoMinuto = "00"
TiempoSegundo = "00"

#DISEÑO LABELS
HoraSistema = Label(190,5, "",23)
HoraText = Label(68,60,"Horas",26)
MinutoText = Label(252,60,"Minutos",26)
SegundoText = Label(441,60,"Segundos",26)

clock = pygame.time.Clock()
FPS = 20

Temporizador = False
BanderaPausa = True
ComparadorSeg = datetime.datetime.now().second
Alarma = False

running = True
while running:
    screen.fill((0,0,0))
    Hora,Minuto,Segundo = ActualizarHora()
    HoraSistema.Text = (f"Hora Actual: {Hora}:{Minuto}:{Segundo}")
    AparecerTemporizador()
    if Temporizador:
        HoraTemp,MinutoTemp,SegundoTemp,Temporizador,ComparadorSeg,Alarma = CalculoTemporizador(HoraTemp,MinutoTemp,SegundoTemp,Temporizador,Segundo,ComparadorSeg,Alarma)
        if HoraTemp < 10:
            TiempoHora = f"0{HoraTemp}"
        else:
            TiempoHora = HoraTemp
        if MinutoTemp < 10:
            TiempoMinuto = f"0{MinutoTemp}"
        else:
            TiempoMinuto = MinutoTemp
        
        if SegundoTemp < 10:
            TiempoSegundo = f"0{SegundoTemp}"
        else:
            TiempoSegundo = SegundoTemp
            
    else:
        BotonEmpezar.visible = True 

    if Alarma:
        SonidoAlarma()
        Alarma = False
        
    
    if BotonEmpezar.visible:
            AparecerBotones()
    else:
        BotonDetener.Dibujar(screen)
        BotonPausar.Dibujar(screen)

        ##EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if BotonEmpezar.visible:
            AccionBotones()
        #HORA
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BotonHoraUP.presionado:
                    HoraTemp,TiempoHora = CalculoParaBotonesUP(HoraTemp)
                    
                elif BotonHoraDown.presionado:
                    HoraTemp,TiempoHora = CalculoParaBotonesDOWN(HoraTemp)
          
        #MINUTOS
                if BotonMinutoUP.presionado:
                    MinutoTemp,TiempoMinuto= CalculoParaBotonesUP(MinutoTemp)
                    
                elif BotonMinutoDown.presionado:
                    MinutoTemp,TiempoMinuto = CalculoParaBotonesDOWN(MinutoTemp)
                
        #SEGUNDOS
                if BotonSegundoUP.presionado:
                    SegundoTemp, TiempoSegundo = CalculoParaBotonesUP(SegundoTemp)
                elif BotonSegundoDown.presionado:
                    SegundoTemp, TiempoSegundo = CalculoParaBotonesDOWN(SegundoTemp)
        
            if BotonEmpezar.visible:

                if BotonEmpezar.presionado:
                    pygame.mixer.music.stop()
                    if HoraTemp == 0 and MinutoTemp == 0 and SegundoTemp == 0:

                        break
                    
                    Temporizador = True
                    BotonEmpezar.visible = False
                    BotonEmpezar.presionado = False
        
        else:
            BotonDetener.verificar_clic(event)
            BotonPausar.verificar_clic(event) 
            
            if event.type == pygame.MOUSEBUTTONDOWN:

                if BotonDetener.presionado:
                    Temporizador = False
                    HoraTemp = 0
                    MinutoTemp = 0
                    SegundoTemp = 0
                    TiempoHora = "00"
                    TiempoMinuto = "00"
                    TiempoSegundo = "00"
                    BotonDetener.presionado = False
                
                if BotonPausar.presionado:
                   
                    Temporizador = False
                    
            
    HoraBox.Texto = str(TiempoHora)
    MinutoBox.Texto = str(TiempoMinuto)
    SegundoBox.Texto = str(TiempoSegundo)
                    
    pygame.display.flip()
        
    clock.tick(FPS)
    
    
    
pygame.quit()

    


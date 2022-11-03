import pygame,sys
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
pygame.init()

#dimenciones pantalla
WIDTH=1000
HEIGTH=600
size= (WIDTH,HEIGTH)
#controla el ciclo
isRunnig=True
#crear Ventana
screen = pygame.display.set_mode(size)
#controlar FPS
clock=pygame.time.Clock()

BLACK =(0,0,0)
WHITE =(255,255,255)
GREEN =(0,255,0)
BLUE =(255,0,0)
RED =(0,0,255)
YELLOW =(216,255,0)
ORANGE =(255,131,0)
BROWN=(86,44,0)

cord_x=70
cord_y=70
radio=45
line_x=100
line_y=240


ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
while True:
    try:
        num = int(simpledialog.askstring(title="Test",prompt="nodos a insertar:"))
        if num>15:
            messagebox.showinfo(message="la pantalla no permite más\nde quince nodos", title="Insert")
            
        else:
            break
    except:
        messagebox.showinfo(message="ingrese un dato valido",title="exception")

while isRunnig:
    #me captura el evento de cierra
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isRunnig=False
    #me pinta la ventana de blanco        
    screen.fill(WHITE) 
    #se recorre el for depende del numero de nodos por el usuario
    for i in range (int(num)):
        pygame.draw.circle(screen,
                        BLUE,
                        (cord_x,cord_y),
                        radio,
                        5)
        #conecta los nodos guardando la distancia de su radio
        if(i!=int(num)-1 and cord_x< WIDTH-200):
            pygame.draw.line(screen,
                            ORANGE,
                            [cord_x+radio,cord_y],
                            [cord_x+200-radio,cord_y],
                            5)
        #incrementa los espacios en x en 200
        cord_x+=200
        #conecta los nodos next renglon
        if(cord_x>WIDTH and cord_y <HEIGTH-150 and num>5):
            pygame.draw.line(screen,
                            ORANGE,
                            [cord_x-200,cord_y+42],
                            [line_x,line_y],
                            5)
            #coordenadas de las lineas
            line_y+=200
            cord_y+=200
            cord_x=70
        
    #carga de nuevo las posiciones iniciales
    cord_x=70  
    cord_y=70
    line_x=100
    line_y=240
    #actualizar la ventana
    pygame.display.flip()
    #maneja los FPS
    clock.tick(60)
    



    

    
    
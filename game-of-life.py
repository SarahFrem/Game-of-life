# -*- coding: utf-8 -*-

"""
The game of life

@author: sarahFremond
"""


import time

# function of the game, table modification   

def modif_tabl():
    global ok
    global tps1
    import scipy

    x={}
    x[0]=height/u
    x[1]=width/u 


    # exterior cells test
    # cell top left: (0,0)

    compt_a=0
    if tabl[0,1]==1:
        compt_a+=1

    if tabl[1,1]==1:
        compt_a+=1

    if tabl[1,0]==1:
        compt_a+=1

    # cell top right: (0,x[1]-1)

    compt_b=0
    if tabl[0,x[1]-2]==1:
        compt_b+=1

    if tabl[1,x[1]-2]==1:
        compt_b+=1

    if tabl[1,x[1]-1]==1:
        compt_b+=1

    # cell bottom left: (x[0]-1,0)

    compt_c=0
    if tabl[x[0]-2,0]==1:
        compt_c+=1

    if tabl[x[0]-2,1]==1:
        compt_c+=1

    if tabl[x[0]-1,1]==1:
        compt_c+=1

    # cell bottom right: (x[0]-1,x[1]-1)

    compt_d=0
    if tabl[x[0]-1,x[1]-2]==1:
        compt_d+=1

    if tabl[x[0]-2,x[1]-2]==1:
        compt_d+=1

    if tabl[x[0]-2,x[1]-1]==1:
        compt_d+=1

        

    # cells middle ext top & bottom 

    compt_f=scipy.zeros((x[1]-2, 1))
    compt_e=scipy.zeros((x[1]-2, 1))

    for k in range(1,x[1]-1):
        # top         
        if tabl[0,k-1]==1:
            compt_e[k-1]+=1
        if tabl[1,k-1]==1:
            compt_e[k-1]+=1
        if tabl[1,k]==1:
            compt_e[k-1]+=1
        if tabl[1,k+1]==1:
            compt_e[k-1]+=1
        if tabl[0,k+1]==1:
            compt_e[k-1]+=1          

        # bottom      
        if tabl[x[0]-1,k-1]==1:
            compt_f[k-1]+=1
        if tabl[x[0]-2,k-1]==1:
            compt_f[k-1]+=1
        if tabl[x[0]-2,k]==1:
            compt_f[k-1]+=1
        if tabl[x[0]-2,k+1]==1:
            compt_f[k-1]+=1
        if tabl[x[0]-1,k+1]==1:
            compt_f[k-1]+=1

    # cells middle ext left & right            

    compt_g=scipy.zeros((x[0]-2, 1))
    compt_h=scipy.zeros((x[0]-2, 1))

    for v in range(1,x[0]-1):
        # left         

        if tabl[v-1,0]==1:
            compt_g[v-1]+=1
        if tabl[v-1,1]==1:
            compt_g[v-1]+=1
        if tabl[v,1]==1:
            compt_g[v-1]+=1
        if tabl[v+1,1]==1:
            compt_g[v-1]+=1
        if tabl[v+1,0]==1:
            compt_g[v-1]+=1

        # right        

        if tabl[v-1,x[1]-1]==1:
            compt_h[v-1]+=1
        if tabl[v-1,x[1]-2]==1:
            compt_h[v-1]+=1
        if tabl[v,x[1]-2]==1:
            compt_h[v-1]+=1
        if tabl[v+1,x[1]-2]==1:
            compt_h[v-1]+=1
        if tabl[v+1,x[1]-1]==1:
            compt_h[v-1]+=1
           

    # int cells test

    compt=scipy.zeros((x[0]-2, x[1]-2))

    for i in range(1,x[0]-1):
        for j in range(1,x[1]-1):
            if tabl[i,j-1]==1:
                compt[i-1][j-1]+=1
            if tabl[i-1,j-1]==1:
                compt[i-1][j-1]+=1
            if tabl[i-1,j]==1:
                compt[i-1][j-1]+=1
            if tabl[i-1,j+1]==1:
                compt[i-1][j-1]+=1
            if tabl[i,j+1]==1:
                compt[i-1][j-1]+=1
            if tabl[i+1,j+1]==1:
                compt[i-1][j-1]+=1
            if tabl[i+1,j]==1:
                compt[i-1][j-1]+=1
            if tabl[i+1,j-1]==1:
                compt[i-1][j-1]+=1

    # state changes

    # int cells

    y=1

    for i in range(1,x[0]-1):
        for j in range(1,x[1]-1):
            if tabl[i,j]==0 and compt[i-1][j-1]==3:
                tabl[i,j]=1
                y=0

            if tabl[i,j]==1 and not compt[i-1][j-1]==2 and not compt[i-1][j-1]==3:
                tabl[i,j]=0
                y=0

    # corner top left           

    if tabl[0,0]==0 and compt_a==3:
        tabl[0,0]=1   
        y=0

    if tabl[0,0]==1 and not compt_a==2 and not compt_a==3:
        tabl[0,0]=0
        y=0

    # corner top right

    if tabl[0,x[1]-1]==0 and compt_b==3:
        tabl[0,x[1]-1]=1
        y=0        

    if tabl[0,x[1]-1]==1 and not compt_b==2 and not compt_b==3:
        tabl[0,x[1]-1]=0 
        y=0

    # corner bottom left            

    if tabl[x[0]-1,0]==0 and compt_c==3:
        tabl[x[0]-1,0]=1
        y=0

    if tabl[x[0]-1,0]==1 and not compt_c==2 and not compt_c==3:
        tabl[x[0]-1,0]=0
        y=0

    # corner bottom right           

    if tabl[x[0]-1,x[1]-1]==0 and compt_d==3:
        tabl[x[0]-1,x[1]-1]=1
        y=0

    if tabl[x[0]-1,x[1]-1]==1 and not compt_d==2 and not compt_d==3:
        tabl[x[0]-1,x[1]-1]=0
        y=0

    # cells middle ext top & bottom

    for k in range(1,x[1]-1):
        if tabl[0,k]==0 and compt_e[k-1]==3:
            tabl[0,k]=1
            y=0

        if tabl[0,k]==1 and not compt_e[k-1]==2 and not compt_e[k-1]==3:
            tabl[0,k]=0
            y=0        

        if tabl[x[0]-1,k]==0 and compt_f[k-1]==3:
            tabl[x[0]-1,k]=1
            y=0

        if tabl[x[0]-1,k]==1 and not compt_f[k-1]==2 and not compt_f[k-1]==3:
            tabl[x[0]-1,k]=0
            y=0

    # cells middle ext left & right

    for v in range(1,x[0]-1):       

        if tabl[v,0]==0 and compt_g[v-1]==3:
            tabl[v,0]=1
            y=0

        if tabl[v,0]==1 and not compt_g[v-1]==2 and not compt_g[v-1]==3:
            tabl[v,0]=0
            y=0

        if tabl[v,x[1]-1]==0 and compt_h[v-1]==3:
            tabl[v,x[1]-1]=1
            y=0

        if tabl[v,x[1]-1]==1 and not compt_h[v-1]==2 and not compt_h[v-1]==3:
            tabl[v,x[1]-1]=0
            y=0

    
    # printing the new table

    table_display()

    #conditions

    if y!=0:
        ok = 0

    # reload case if table is resolved

    if ok == 1:
        fenetre.after(speed,modif_tabl)


    # display resolution time (stop button or resolved table)

    elif ok == 0:
        tps2 = time.time()
        label1 = Tkinter.Label(fenetre, text="Temps de résolution de la grille : %f secondes." %(tps2-tps1))  
        label1.pack(side=Tkinter.LEFT,padx=5,pady=5)

        
# function table_display

def table_display():

    h=0

    while h <= (height/u)-1:
        l=0
        while l <= (width/u)-1:
            y=h*u
            x=l*u

            if tabl[h,l]==1:
                canvas.create_rectangle(x, y, x+u, y+u, fill='white')
            elif tabl[h,l]==0:
                canvas.create_rectangle(x, y, x+u, y+u, fill='black')

            l+=1
        h+=1


# button start

def start():

    global ok
    ok = 1
    global tps1
    tps1= time.time()
    modif_tabl()


# button stop

def stop():
    global ok
    ok =0


# parameters
height = 600
width = 1000
u = 50 # u is the unit
speed = 500
a = 0
b = 0
ok = 0
tps1 = 0


# table creation

tabl = {}
import random

for i in range(0,height/u):
    for j in range(0,width/u):
        tabl[i,j]=random.randint(0,1) # game rule : 0 is a dead cell, 1 alive 

# graphic interface creation

import Tkinter 
fenetre = Tkinter.Tk()
fenetre.title('Game of life')
canvas = Tkinter.Canvas(fenetre, width =width, height =height, background ='black')

while a != width:
    canvas.create_line(a,0,a,height,width=1,fill='white')
    a+=u

while b != height:
    canvas.create_line(0,b,width,b,width=1,fill='white')
    b+=u

canvas.pack()


# buttons creation

button_start = Tkinter.Button(fenetre,text="Start",command=start)
button_stop = Tkinter.Button(fenetre,text="Stop",command=stop)

button_start.pack(side=Tkinter.LEFT,padx=5,pady=5)
button_stop.pack(side=Tkinter.LEFT,padx=5,pady=5)


# display graphic interface window

fenetre.mainloop()
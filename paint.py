from tkinter import *
from math import *
import csv 

window = Tk()
canvas = Canvas(window,width = 800, height = 800)
window.title('Plagia paint')

content = [
           ]

color = ["red","green","blue","orange","pink","violet","cyan","yellow","white","black"]
kolor = ["black","white","yellow","cyan","violet","pink","orange","blue","green","red"]
taille = [1,2,3,4,8]
gaille = [1,2,3,4,5]

onDrag = False

canvas.pack()

startx = 0
starty = 0
endx = 0
endy = 0
width = 0
choice=1
record = 0

csv_file = "value.csv"

bg = 0
fg = 0
g = 0



def drawAll():
    global r, bg
    canvas.delete("all")
    for c in content:
        create_circle(c["x"],c["y"], c["r"], c["c"], c["w"],c["f"],c["g"])
    if onDrag:
        dx = endx - startx
        dy = endy - starty
        r = sqrt(dx*dx+dy*dy)
        create_circle(startx,starty,r,bg,width,fg,choice)
    drawTools()
    
def drawTools():
    v1 = 0
    v2 = 30
    t1=0
    t2=10
    for c in color :
        canvas.create_rectangle(v1,0,v2,30,fill=c)
        v1 = v1 +30
        v2 = v2 + 30
    canvas.create_rectangle(30*bg,0,30*bg+30,30,fill="", outline="turquoise", width=4)
    canvas.create_rectangle(30*(record+len(color)+2.12),0,30*(record+len(color)+2.12)+30-2,30,fill="darkgrey", outline="black", width=2)
    x = len(color)*30+5
    for i in taille:
        canvas.create_line(x+t1,0,x+t2,30, width=i, fill="black")
        t1 = t1 +10
        t2 = t2 + 10

    for v in kolor :
        canvas.create_rectangle(0,v1,30,v2,fill=v)
        v1 = v1 -30
        v2 = v2 - 30
    canvas.create_rectangle(0,30*fg+30,30,30*fg+60,fill="", outline="lime", width=4)

    canvas.create_rectangle(x+60,5,x+85,30,outline="black")
    canvas.create_oval(x+90,5,x+115,30,outline="black")
    canvas.create_arc(x+120,5,x+150,30,outline="black")
    canvas.create_line(x+150,5,x+175,30)
    canvas.create_oval(x+180,10,x+210,20,outline="black")
    canvas.create_text(550,10, text='Save')
    canvas.create_text(650,10, text='Reset Save')
    canvas.create_text(720,15, text='<-')


def create_circle(x,y,r,c,w,f,g):
    global width, choice
    if(gaille[g]==2):
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color[c], width=taille[w], outline=color[f])
    elif(gaille[g]==1):
        canvas.create_rectangle(x-r,y-r,x+r,y+r,fill=color[c], width=taille[w], outline=color[f])
    elif(gaille[g]==3):
        canvas.create_arc(x-r,y-r,x+r,y+r,fill=color[c], width=taille[w], outline=color[f])
    elif(gaille[g]==4):
        canvas.create_line(x-r,y-r,x+r,y+r,fill=color[c], width=taille[w])
    elif(gaille[g]==5):
        canvas.create_oval(x-r*2,y-r*3,x+r*4,y+r*2,fill=color[c], width=taille[w], outline=color[f])
    
def OnMousePress(event):
    global startx, starty, bg, endx, endy, onDrag, width, fg, choice, record, g
    if(event.y <30 and event.x<30*len(color)):
        bg = event.x//30
    elif(event.x <30 and event.y<60*len(color)):
        fg = event.y//30
        fg=fg-1
    elif(event.y <30 and event.x<300+10*len(taille)):
        x = event.x - 30*len(color)
        width = x//10
        #print(width)
    elif(event.y <30 and event.x<350+35*len(gaille)):
        g = event.x - 30*len(color)-30
        choice = g//30
        choice=choice-1
        if(choice!=-1):
            record=choice
            #print(record)
        else:
            choice=record
        #print(choice)
    elif(event.y < 30 and event.x < 550 + 35):
        Save()
        print("Saving Success")
    elif(event.y < 30 and event.x < 650 + 35):
        ResetSave()
    elif(event.y < 30 and event.x < 720 + 10):
        BackTime()

    else:
        onDrag = True
        endx = startx = event.x
        endy = starty = event.y
        
    drawAll()

def OnMouseDrag(event):
    global endx, endy
    endx = event.x
    endy = event.y
    drawAll()
   
def OnMouseRelease(event):
        global endx, endy, startx, starty, onDrag
        if onDrag:
                
            endx = event.x
            endy = event.y
            dx = endx-startx
            dy = endy - starty
            r = sqrt(dx*dx+dy*dy)
            content.append({"x":startx,
                            "y":starty,
                            "r":r,
                            "c":bg,
                            "w":width,
                            "f":fg,
                            "g":choice
                            })
            startx = starty = endx = endy = 0
            onDrag = False    
        drawAll()
    
def Save():
    csv_columns = ['x','y','r','c','w','f','g']
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in content:
            writer.writerow(data)

def ReadSave():
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print(row['x'], row['y'], row['r'], row['c'], row['w'], row['g'], row['f'])
            content.append({"x":int(row['x']),
                            "y":int(row['y']),
                            "r":float(row['r']),
                            "c":int(row['c']),
                            "w":int(row['w']),
                            "f":int(row['f']),
                            "g":int(row['g'])
                            })
        print("Project Loaded")

def ResetSave():
    content.clear()
    Save()
    print('Save Clear')

def BackTime():
    number = len(content)
    #print(number)
    if(number > 0): content.pop()


window.bind("<ButtonPress-1>", OnMousePress)
window.bind("<ButtonRelease-1>", OnMouseRelease)
window.bind("<B1-Motion>", OnMouseDrag)
ReadSave()
drawAll()

window.mainloop()


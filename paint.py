from tkinter import *
from math import *
window = Tk()
canvas = Canvas(window,width = 800, height = 800)
window.title('Plagia Paint')

content = [
           ]

color = ["red","green","blue","orange","pink","violet","cyan","yellow","white","black"]

onDrag = False

canvas.pack()

startx = 0
starty = 0
endx = 0
endy = 0
width = 0

bg = 0
fg = 0
tx = 0

def drawAll():
    global r, bg
    canvas.delete("all")
    for c in content:
        create_circle(c["x"],c["y"], c["r"], c["c"], c["width"], c["f"])
    if onDrag:
        dx = endx - startx
        dy = endy - starty
        r = sqrt(dx*dx+dy*dy)
        create_circle(startx,starty,r,bg,width, fg)
    drawTools()
    
def drawTools():
    v1 = 0
    v2 = 30
    for c in color :
        canvas.create_rectangle(v1,0,v2,30,fill=c)
        v1 = v1 +30
        v2 = v2 + 30
    canvas.create_rectangle(30*bg,0,30*bg+30,30, outline="red", width=2)
    canvas.create_rectangle(30*tx-2,0,30*tx+30-2,30,fill="darkgrey", outline="black", width=2)
    x = len(color)*30+5
    for i in range(1,5):
        if(i == width-1):
            canvas.create_line(x+(10*i),0,x+(10*i),30, width=2*i, fill=color[fg])
        else:
            canvas.create_line(x+(10*i),0,x+(10*i),30, width=2*i)
    
    x = x+10*8
    canvas.create_rectangle(x+5,0+4,x+30,30-5)
    canvas.create_oval(x+35,2,x+60,25)
    canvas.create_oval(x+65,5,x+90,25)
    canvas.create_line(x+93,0,x+123,30)


def create_circle(x,y,r,c,w,f):
    canvas.create_oval(x-r,y-r,x+r,y+r,fill=color[c], width=w, outline=color[f])
    
def OnMousePress(event):
    global startx, starty, bg, endx, endy, onDrag, width, fg, tx
    if(event.y <30 and event.x<30*len(color)):
        bg = event.x//30
    elif(event.y <30 and event.x<80+30*len(color)):
        x = event.x - 30*len(color)
        width = x//10
        for i in range(1,5):
            strock = event.x//10
        #print("strock" + str(strock))
    elif(event.y <30 and event.x<200+30*len(color)):
        tx = event.x // 30
        for i in range(1,5):
            tools = event.x//10
        print(tools)
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
                            "width":width,
                            "f":fg
                            })
            startx = starty = endx = endy = 0
            onDrag = False    
        drawAll()
            

window.bind("<ButtonPress-1>", OnMousePress)
window.bind("<ButtonRelease-1>", OnMouseRelease)
window.bind("<B1-Motion>", OnMouseDrag)

drawAll()

window.mainloop()


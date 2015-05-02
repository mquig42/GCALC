#!/usr/bin/python

from Tkinter import *
from math import *

root=Tk()
root.title("Gcalc")
formula=Text(root, height=1)
cmdGraph=Button(root,text="Graph")
canvas=Canvas(root,bg="black",width=640,height=480)
lbl1=Label(root,text="y=")

#virtual coordinates of graph canvas
xmin=-10.0
xmax=10.0
ymin=-10.0
ymax=10.0

#Functions
def translate(x,y):
	global xmin,xmax,ymin,ymax
	tc=[0,0]
	x_add=0-xmin
	y_add=0-ymin
	x_mul=int(canvas["width"])/(xmax-xmin)
	y_mul=-1*(int(canvas["height"])/(ymax-ymin))
	x=(x+x_add)*x_mul
	y=(y+y_add)*y_mul+int(canvas["height"])
	tc[0]=x
	tc[1]=y
	return tc
	
def drawline(xfrom,yfrom,xto,yto,colour):
	fromcoords=translate(xfrom,yfrom)
	tocoords=translate(xto,yto)
	canvas.create_line(fromcoords[0],fromcoords[1],tocoords[0],tocoords[1],fill=colour)

def drawgrid():
	for x in range(int(xmin),int(xmax)):
		drawline(x,ymin,x,ymax,"darkgreen")
	for y in range(int(ymin),int(ymax)):
		drawline(xmin,y,xmax,y,"darkgreen")
	drawline(xmin,0,xmax,0,"green")
	drawline(0,ymin,0,ymax,"green")
	
def drawgraph(event):
	global xmin,xmax,ymin,ymax
	canvas.delete("all")
	drawgrid()
	yprev=0.0
	x=xmin
	eqn=formula.get("1.0","1.end")
	while(x<=xmax):
		y=eval(eqn)
		drawline(x-0.25,yprev,x,y,"green")
		yprev=y
		x=x+0.25


#Bind event handlers
cmdGraph.bind('<Button-1>',drawgraph)

#Display graphical elements
lbl1.grid(column=0,row=0)
formula.grid(column=1,row=0)
cmdGraph.grid(column=2,row=0)
canvas.grid(columnspan=3)

drawgrid()
root.mainloop()

from tkinter import *
from tkinter import ttk
import random
 
colors1 = {'black': '0',
			'brown' : '1',
			'red' : '2',
			'orange' : '3',
			'yellow' : '4',
			'green' : '5',
			'blue' : '6',
			'violet' : '7',
			'grey' : '8', 
			'white' : '9'}

colors2 = {'black': '0',
			'brown' : '1',
			'red' : '2',
			'orange' : '3',
			'yellow' : '4',
			'green' : '5',
			'blue' : '6',
			'violet' : '7',
			'grey' : '8', 
			'white' : '9'}

colors3 = {'black': '1',
			'brown' : '10',
			'red' : '100',
			'orange' : '1000',
			'yellow' : '10000',
			'green' : '100000',
			'blue' : '1000000',
			'violet' : '10000000',
			'grey' : '100000000', 
			'white' : '1000000000',
			'gold' : '0.1',
			'silver' : '0.01'}

colors4 = {'brown' : '±1%',
			'red' : '±2%',
			'orange' : '±3%',
			'yellow' : '±4%',
			'green' : '±0.5%',
			'blue' : '±0.25%',
			'violet' : '±0.1%',
			'grey' : '±0.05%', 
			'gold' : '±5%',
			'silver' : '±10%'}

def CheckColor(b1,b2,b3,b4 = 'gold'):
	print('Band 1: {} digit : {}'.format(b1,colors1[b1]))
	print('Band 2: {} digit : {}'.format(b2,colors2[b2]))
	print('Band 3: {} multiplier : {}'.format(b3,colors3[b3]))
	print('Band 4: {} torerance: {}'.format(b4,colors4[b4]))
	cal = int(colors1[b1]+colors2[b2]) * int(colors3[b3])
	if cal >= 1000000000 :
		prefix = 'G'
		if str(cal)[-8] != '0':
			res = str(cal)[:-9] + prefix + str(cal)[-9]
		else :
			res = str(cal)[:-9] + prefix
	elif cal >= 1000000 :
		prefix = 'M'
		if str(cal)[-6] != '0':
			res = str(cal)[:-6] + prefix + str(cal)[-6]
		else :
			res = str(cal)[:-6] + prefix
	elif cal >= 1000 :
		prefix = 'k'
		if str(cal)[-3] != '0':
			res = str(cal)[:-3] + prefix + str(cal)[-3]
		else :
			res = str(cal)[:-3] + prefix
	else :
		res = ''

	print('ตัวต้านตัวนี้มีค่า: {:,d} โอห์ม ( {}Ω )'.format(cal,res))
	print('----------')
	return '{:,d} โอห์ม ( {}Ω )'.format(cal,res)

GUI = Tk()
GUI.title('Resistor GUI')
GUI.geometry('800x600')
FONT = ('Angsana New',20)
L1 = Label(GUI,text='ค่าความต้านทาน',font=FONT).pack()

resistor = StringVar()
E1 = Entry(GUI,textvariable=resistor,font=FONT)
E1.place(x=100,y=50,width=500)

ohm = Label(GUI,text='Ω',font=FONT)
ohm.place(x=620,y=50)

canvas = Canvas(GUI,width=500,height=100)
canvas.place(x=200,y=250)

box1 = canvas.create_rectangle(0,0,50,50,fill='red')
box2 = canvas.create_rectangle(100,0,150,50,fill='green')
box3 = canvas.create_rectangle(200,0,250,50,fill='blue')
box4 = canvas.create_rectangle(300,0,350,50,fill='yellow')

F1 = Frame(GUI)
F1.place(x=50,y=350)

allbutton = []
v_c1 = StringVar()
v_c2 = StringVar()
v_c3 = StringVar()
v_c4 = StringVar()


def Change(bcl,b,v):
	if b == 1:
		v_c1.set(bcl)
		cvalue = resistor.get() + v
		resistor.set(cvalue)
		B2.configure(state='disabled')
	elif b == 2:
		v_c2.set(bcl)
		cvalue = resistor.get() + v
		resistor.set(cvalue)
		B3.configure(state='disabled')
	elif b == 3:
		v_c3.set(bcl)
		resistor.set(CheckColor(v_c1.get(),v_c2.get(),v_c3.get()))
		B4.configure(state='disabled')
	else :
		v_c4.set(v)
		cvalue = resistor.get() + ' ' + v 
		resistor.set(cvalue)
		B5.configure(state='disabled')

	
	global allbutton
	bcolor = {1:box1,2:box2,3:box3,4:box4}
	canvas.itemconfig(bcolor[b],fill=bcl)
	for ab in allbutton:
		ab.destroy()
	allbutton = []

def c1():
	for i,(bc,bv) in enumerate(colors1.items()):
		B = Button(F1,width=6,bg=bc,command=lambda x=bc,y=bv: Change(x,1,y))
		B.grid(row = 0 ,column = i,padx = 10)
		allbutton.append(B)

def c2():
	for i,(bc,bv) in enumerate(colors2.items()):
		B = Button(F1,text=bc,bg=bc,command=lambda x=bc,y=bv: Change(x,2,y))
		B.grid(row = 0 ,column = i,padx = 10)
		allbutton.append(B)

def c3():
	for i,(bc,bv) in enumerate(colors3.items()):
		B = Button(F1,text=bc,bg=bc,command=lambda x=bc,y=bv: Change(x,3,y))
		B.grid(row = 0 ,column = i,padx = 10)
		allbutton.append(B)

def c4():
	for i,(bc,bv) in enumerate(colors4.items()):
		B = Button(F1,text=bc,bg=bc,command=lambda x=bc,y=bv: Change(x,4,y))
		B.grid(row = 0 ,column = i,padx = 10)
		allbutton.append(B)

B2 = ttk.Button(GUI,text='Color 1',command = c1)
B2.place(x=200,y=390)
B3 = ttk.Button(GUI,text='Color 2',command = c2)
B3.place(x=300,y=390)
B4 = ttk.Button(GUI,text='Color 3',command = c3)
B4.place(x=400,y=390)
B5 = ttk.Button(GUI,text='Color 4',command = c4)
B5.place(x=500,y=390)

def Reset():
	resistor.set('')
	v_c1.set('')
	v_c2.set('')
	v_c3.set('')
	v_c4.set('')
	B2.configure(state='enabled')
	B3.configure(state='enabled')
	B4.configure(state='enabled')
	B5.configure(state='enabled')



BR = ttk.Button(GUI,text='Reset',command=Reset)
BR.place(x=600,y=390,width=90)

GUI.mainloop()
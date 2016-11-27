from tkinter import *
import os

def create_code_blocks(file_name):
	emptlist = []
	joined_list = []
	handle = open(file_name, 'r')
	for i in handle:
		i = i.rstrip()
		if i != "":
			emptlist.append(i)
		else:
			joined = "\n".join(emptlist)
			joined_list.append(joined)
			emptlist = []
			continue
	return joined_list
    
code_blocks = create_code_blocks('jd_calc.py')
dialog_blocks = create_code_blocks('jd_calc_doc.txt')
               
counter = -1

class Code_Professor(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid(columnspan=4)
		self.code_disp = ""
		self.dialog_disp = ""
		self.createWidgets()
		self.createLabels()
        
	def read_lines(self):
		global counter
		counter += 1
		try:
			self.code_disp.set(code_blocks[counter])
			self.dialog_disp.set(dialog_blocks[counter])
		except:
			return
        
	def back_space(self):
		global counter
		if counter != 0:
			counter -= 1
			try:
			    self.code_disp.set(code_blocks[counter])
			    self.dialog_disp.set(dialog_blocks[counter])
			except:
			    return
		else:
			return
        
	def clear_lines(self):
		self.code_disp.set("")
		self.dialog_disp.set("")
        
	def reload(self):
		global counter
		counter = 0
		self.code_disp.set(code_blocks[counter])
		self.dialog_disp.set(dialog_blocks[counter])
        

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["command"] =  exit
		self.QUIT.grid(row = 4, column = 1, columnspan = 4)
        
		self.Launch = Button(self)
		self.Launch["text"] = "CALCULATOR"
		self.Launch["command"] = self.quit
		self.Launch.grid(row = 3, column = 1, columnspan = 4)
        
		self.clear = Button(self)
		self.clear["text"] = "Clear"
		self.clear["command"] = self.clear_lines
		self.clear.grid(row=2, column = 4)
        
		self.home = Button(self)
		self.home["text"] = "Home"
		self.home["command"] = self.reload
		self.home.grid(row = 2, column = 1)
        
		self.next = Button(self)
		self.next["text"] = "Next",
		self.next["command"] = self.read_lines
		self.next.grid(row= 2 , column = 2)
        
		self.back = Button(self)
		self.back["text"] = "Back",
		self.back["command"] = self.back_space
		self.back.grid(row= 2 , column = 3)
        
        
	def createLabels(self):
		self.code_disp = StringVar()
		Label(master=None, anchor = N, font = "Courier 10 bold", bg='green', relief=SUNKEN,width=90,height=38, justify = LEFT, textvariable = self.code_disp ).grid(row=0)
		self.code_disp.set("")
        
		self.dialog_disp = StringVar()
		Label(master=None, anchor = N, font = "Courier 10 bold", fg = "green", bg='black', relief=RIDGE, width=90,height=38, justify = LEFT, textvariable = self.dialog_disp ).grid(row=0, column = 1)
		self.dialog_disp.set("")
        
root = Tk()
body = Frame(root)
root.resizable(0,0)
body.grid()
app = Code_Professor(master=root)
app.mainloop()
root.destroy()

import jd_calc
#

#

#

#

#

from tkinter import *

class JamesCalculator():
    def __init__(self):
        self.equa = "" 
        self.post_op = "" 
        self.op_list = [False, False, False] 

    def push_num(self,num):
        if self.equa == "":
            self.equa = self.equa + num
            equation.set(self.equa)
        elif self.equa[0] == "0": 
            if "." not in self.equa:
                if num != "0":
                    self.equa = num
                    equation.set(self.equa)
            else:
                self.equa = self.equa + num	
                equation.set(self.equa)
        else:
            self.equa = self.equa + num
            equation.set(self.equa)
		
    def push_operator(self,operator):
        if self.equa != "":
            if self.op_list[0] == False:
                self.op_list[0] = self.equa
                self.op_list[1] = operator
                crnt_op.set(self.op_list[1])
                equation.set(self.op_list[0])
                self.equa = ""
            elif self.op_list[0] != False:
                if self.equa == "":
                    self.op_list[1] = operator
                    crnt_op.set(self.op_list[1])
                else:
                    self.op_list[2] = self.equa
                    self.equa = ""
                    joiner = "".join(self.op_list) 
                    joinedval = eval(joiner)
                    joinedval = str(joinedval)
                    self.post_op = joinedval
                    self.op_list = [self.post_op, operator, False]
                    crnt_op.set(operator)
                    equation.set(self.op_list[0])
        else:
            if self.post_op != "":
                self.op_list[1] = operator
                crnt_op.set(operator)
            else:
                return
                          
    def num_logic(self,num): 
        if self.post_op != "":
            equation.set(self.equa)
            self.post_op = ""
            self.push_num(num)
        else:
            self.push_num(num)
              
    def dot_push(self):
        if "." in self.equa:
            return
        else:
            if self.equa == "":
                self.equa = "0"+"."
                equation.set(self.equa)
            else:
                self.equa = self.equa + "."
                equation.set(self.equa)
			
    def sign_change(self): 
        if self.equa != "":        
            if "." in self.equa:
                self.equa = -(float(self.equa))
                self.equa = str(self.equa)
                equation.set(self.equa)
            else:
                self.equa = -(int(self.equa))
                self.equa = str(self.equa)
                equation.set(self.equa)
        else:
            if "." in self.post_op:
                self.post_op = -(float(self.post_op))
                self.post_op = str(self.post_op)
                self.op_list[0] = self.post_op
                equation.set(self.post_op)
            else:
                self.post_op = -(int(self.post_op))
                self.post_op = str(self.post_op)
                self.op_list[0] = self.post_op
                equation.set(self.post_op)
           
    def clear_entry(self):
        self.equa = ""
        equation.set(self.equa)
	    
    def clear_all(self):
        self.op_list = [False, False, False]
        self.equa = ""
        crnt_op.set("")
        equation.set(self.equa)
	    
    def equals(self):
        if self.op_list[0] == False:
            return
        elif self.equa == "":
        	return
        else:
            self.op_list[2] = self.equa
            joiner = "".join(self.op_list)
            joinedval = eval(joiner)
            joinedval = str(joinedval)
            self.equa = joinedval
            self.post_op = joinedval
            crnt_op.set("")
            self.op_list = [False, False, False]
            equation.set(self.equa)
          
jc = JamesCalculator()
root = Tk()
root.resizable(0, 0)
root.geometry("170x275")

calc = Frame(root, background = "grey")
calc.grid()
root.title("James_Calculator")

equation = StringVar()
labelholder = ""
equation.set(labelholder)
calculation = Label(calc, wraplength=100,height=2, justify=RIGHT, anchor=E, 
                     relief=SUNKEN, textvariable = equation)
calculation.grid(row = 0, column=1, columnspan=3, pady = 5, sticky=W+E+N+S)  
calculation.grid_rowconfigure(0, minsize=370)
	
crnt_op = StringVar()
sign_holder = ""
crnt_op.set(sign_holder)
op_display = Label(calc, justify=LEFT, anchor=E, relief=SUNKEN, textvariable = crnt_op)
op_display.grid(row = 0, column=0, pady = 5, sticky=W+E+N+S)  
op_display.grid_rowconfigure(0, minsize=5)

numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(Button(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k, pady = 5)
        bttn[i]["command"] = lambda x = numbers[i]: jc.num_logic(x)
        i += 1

division = Button(calc, text = chr(247))
division["command"] = lambda: jc.push_operator("/")
division.grid(row = 1, column = 3, pady = 5)

multiplication = Button(calc, text = "x")
multiplication["command"] = lambda: jc.push_operator("*")
multiplication.grid(row = 2, column = 3, pady = 5)

subtraction = Button(calc, text = "-")
subtraction["command"] = lambda: jc.push_operator("-")
subtraction.grid(row = 3, column = 3, pady = 5)

dot = Button(calc, text = ".")
dot["command"] = lambda: jc.dot_push()
dot.grid(row = 4, column = 0, pady = 5)

addition = Button(calc, text = "+")
addition["command"] = lambda: jc.push_operator("+")
addition.grid(row = 4, column = 3, pady = 5)

negative = Button(calc, text = "+/-")
negative["command"] = lambda: jc.sign_change()
negative.grid(row = 5, column = 0, pady = 5)

clear_last = Button(calc, text = "C")
clear_last["command"] = lambda: jc.clear_entry()
clear_last.grid(row = 5, column = 1, pady = 5)

clear_all = Button(calc, text = "AC")
clear_all["command"] = lambda: jc.clear_all()
clear_all.grid(row = 5, column = 2, pady = 5)

equal = Button(calc, text = "=")
equal["command"] = lambda: jc.equals()
equal.grid(row = 5, column = 3, pady = 5)

zero = Button(calc, text = "0")
zero["command"] = lambda: jc.num_logic("0")
zero.grid(row = 4, column = 1, pady = 5)

quit = Button(calc, text = "QUIT")
quit["command"] = exit
quit.grid(row = 6, column= 0, columnspan = 5, pady = 5)

root.mainloop()

#
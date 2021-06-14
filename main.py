from tkinter import *
import threading
import tkinter

class calculator:
    arithmetic = ''
    first_digit = 0
    second_digit = 0
    result = 0
    
    def __init__(self, master): 

        self.master = master
       
        #frame 1 boundary for display section
        frame1 = Frame(master,padx=0, pady=20)
        frame1.grid(row=0)
        #frame 2 boundary for the buttons and arithmetic logic
        frame2 = Frame(master)
        frame2.grid(row=1)
        #label
        self.text = Entry(frame1, width=58)


        #buttons
        self.zero = Button(frame2,text=0, width=14, height=4, command=lambda: self.button_click(0))
        self.first = Button(frame2,text=1, width=14, height=4, command=lambda: self.button_click(1))
        self.second = Button(frame2,text=2, width=14, height=4, command=lambda: self.button_click(2))
        self.third = Button(frame2,text=3, width=14, height=4, command=lambda: self.button_click(3))
        self.fourth = Button(frame2,text=4, width=14, height=4, command=lambda: self.button_click(4))
        self.fifth = Button(frame2,text=5, width=14, height=4, command=lambda: self.button_click(5))
        self.sixth = Button(frame2,text=6, width=14, height=4, command=lambda: self.button_click(6))
        self.seventh = Button(frame2,text=7, width=14, height=4, command=lambda: self.button_click(7))
        self.eighth = Button(frame2,text=8, width=14, height=4, command=lambda: self.button_click(8))
        self.nineth = Button(frame2,text=9, width=14, height=4, command=lambda: self.button_click(9))

        #arithmetic buttons
        self.addition = Button(frame2,text='+', width=14, height=4, command=self.add)
        self.multiplication = Button(frame2,text='X', width=14, height=4, command=self.multiplication)
        self.division = Button(frame2,text='/', width=14, height=4, command=self.division)
        self.difference = Button(frame2,text='-', width=14, height=4,command=self.difference)
        self.equals = Button(frame2,text='=', width=14, height=4,command=self.equals )
        self.clear = Button(frame2,text='Clear', width=14, height=4,command=self.clear)
        self.rand = Button(frame2,text='rand', width=14, height=4)
        self.square = Button(frame2,text='Square', width=14, height=4)

        #grid / position on workspace
        self.zero.grid(column=1,row=5)
        self.first.grid(column=0,row=4)
        self.second.grid(column=1,row=4)
        self.third.grid(column=2,row=4)
        self.fourth.grid(column=0,row=3)
        self.fifth.grid(column=1,row=3)
        self.sixth.grid(column=2,row=3)
        self.seventh.grid(column=0,row=2)
        self.eighth.grid(column=1,row=2)
        self.nineth.grid(column=2,row=2)

        self.addition.grid(column=4, row=4, )
        self.multiplication.grid(column=4, row=3, )
        self.division.grid(column=4, row=2, )
        self.difference.grid(column=4, row=1,)
        self.equals.grid(column=4, row=5, )
        self.clear.grid(column=2, row=1, )
        self.rand.grid(column=1, row=1, )
        self.square.grid(column=0, row=1,)

        self.text.grid(column=0, row=0, columnspan=4)
        self.text.config( )
        # bg='black',fg='white'
    
    def button_click(self,number):
        store = self.text.get()
        self.text.delete(0,END)
        self.text.insert(0,int(store + str(number)))
        self.first_digit = self.text.get()

        return self.first_digit

    def add(self):
        self.text.delete(0,END) #clear screen
        self.f_num = self.first_digit
        self.arithmetic = '+'
    def multiplication(self):
        self.text.delete(0,END) #clear screen
        self.f_num = self.first_digit
        self.arithmetic = '*'
    def division(self):
        self.text.delete(0,END) #clear screen
        self.f_num = self.first_digit
        self.arithmetic = '/'
    def difference(self):
        self.text.delete(0,END) #clear screen
        self.f_num = self.first_digit
        self.arithmetic = '-'

        return self.result
    def equals(self):
        self.second_digit = self.text.get() #store second value in a variable
       
        if self.arithmetic == '+':
            self.result =  int(self.f_num) + int(self.second_digit)  #arithmetic
            self.text.delete(0,END)
            self.text.insert(0,self.result)
           

        elif self.arithmetic == '-':
            if self.second_digit > self.first_digit:

                self.result =  int(self.second_digit) - int(self.f_num)  #arithmetic
            else:
                self.result =  int(self.f_num) - int(self.second_digit)  #arithmetic
            self.text.delete(0,END)
            self.text.insert(0,self.result)
        elif self.arithmetic == '*':
            self.result =  int(self.f_num) * int(self.second_digit)  #arithmetic
            self.text.delete(0,END)
            self.text.insert(0,self.result)
        elif self.arithmetic == '/':
            self.result =  int(self.f_num) / int(self.second_digit)  #arithmetic
            self.text.delete(0,END)
            self.text.insert(0,self.result)

    def clear(self):
        self.text.delete(0,END) #clear screen


        #customization

def main():
    window = Tk()
    # make window or applicatin not resisable
    window.resizable(0,0)
    # window.geometry('700x450')
    new = calculator(window)
    window.mainloop()

if __name__ == '__main__':
    main()

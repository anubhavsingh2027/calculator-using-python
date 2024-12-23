from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry('450x588')
root.resizable(0,0)
root.config(bg='black')

r=Label(root, text='', bg='black', fg='white', anchor='e',height=2)
r.grid(row=0, column=0, columnspan=1500, pady=10, padx=5, sticky='we') 
r.config(font=('verdana', 25, 'bold'))

import math as m

def get_digit(digit):
    current=r['text']
    new=current+digit
    r.config(text=new)

def clear():
    r.config(text='')
def oclear(operator):
    if operator=='X':
        l=r['text']
        res = l[:-1]
        r.config(text=res)


def operations(operator):
    global n1,opr,total
    n1=r['text']
    
    opr=operator
    total=n1+opr
    r.config(text=total)


def sqm(value):
    global n1
    n1=r['text']
    if(value=='sqrt'):
        r.config(text=m.sqrt(int(n1)))
    elif(value=='sin'):
        r.config(text=m.sin(m.radians(int(n1))))
    elif(value=='cos'):
        r.config(text=m.cos(m.radians(int(n1))))
    elif(value=='fact'):
        r.config(text=m.factorial(int(n1)))
    else:
        r.config(text=m.tan(m.radians(int(n1))))
def equals(operator):
    global n2,n1
    n3=r['text']
    n2=''.join(n3[i] for i in range(len(total), len(n3)))
    n1, n2 = float(n1), float(n2)

    if opr=='*':
     r.config(text=n1*n2)
    elif opr=='+':
         r.config(text=n1+n2)
    elif opr=='-':
         r.config(text=n1-n2)
    elif opr=='%':
        try:
          if n2 != 0:  
            result = n1%n2
            r.config(text=str(result)) 
          else:
              r.config(text="0")  
        except ValueError:
            r.config(text="Error") 

 
    
    elif opr == '/':
        try:
          if n2 != 0:  
            result = n1/n2
            r.config(text=str(result)) 
          else:
              r.config(text="Not defined")  
        except ValueError:
            r.config(text="Error") 

    else:
            result = "Error"
            r.config(text=str(result))

     
        
              
ac=Button(root,text='AC',bg='grey',fg='black',height=3,width=6,command=lambda:clear())
ac.grid(row=1,column=0,padx=1,pady=1)
ac.config(font=('verdana',15,'italic'))
per=Button(root,text='%',bg='grey',fg='black',height=3,width=6,command=lambda:operations('%'))
per.grid(row=1,column=1,padx=1,pady=1)
per.config(font=('verdana',15,'italic'))
de=Button(root,text='DEL',bg='grey',fg='black',height=3,width=6,command=lambda:oclear('X'))
de.grid(row=1,column=2,padx=1,pady=1)
de.config(font=('verdana',15,'italic'))
div=Button(root,text='/',bg='grey',fg='black',height=3,width=6,command=lambda:operations('/'))
div.grid(row=1,column=3,padx=1,pady=1)
sq=Button(root,text='sqr',bg='lightblue',fg='black',height=3,width=6,command=lambda:sqm('sqrt'))
sq.grid(row=1,column=4,padx=1,pady=1)
sq.config(font=('verdana',15,'italic'))
div.config(font=('verdana',15,'italic'))
b7=Button(root,text='7',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('7'));
b7.grid(row=2,column=0,padx=1,pady=1)
b7.config(font=('verdana',15,'italic'))
b8=Button(root,text='8',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('8'))
b8.grid(row=2,column=1,padx=1,pady=1)
b8.config(font=('verdana',15,'italic'))
b9=Button(root,text='9',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('9'))
b9.grid(row=2,column=2,padx=1,pady=1)
b9.config(font=('verdana',15,'italic'))
mul=Button(root,text='*',bg='grey',fg='black',height=3,width=6,command=lambda:operations('*'))
mul.grid(row=2,column=3,padx=1,pady=1)
mul.config(font=('verdana',15,'italic'))
sin=Button(root,text='sinx',bg='lightblue',fg='black',height=3,width=6,command=lambda:sqm('sin'))
sin.grid(row=2,column=4,padx=1,pady=1)
sin.config(font=('verdana',15,'italic'))
b4=Button(root,text='4',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('4'))
b4.grid(row=3,column=0,padx=1,pady=1)
b4.config(font=('verdana',15,'italic'))
b5=Button(root,text='5',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('5'))
b5.grid(row=3,column=1,padx=1,pady=1)
b5.config(font=('verdana',15,'italic'))
b6=Button(root,text='6',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('6'))
b6.grid(row=3,column=2,padx=1,pady=1)
b6.config(font=('verdana',15,'italic'))
sub=Button(root,text='-',bg='grey',fg='black',height=3,width=6,command=lambda:operations('-'))
sub.grid(row=3,column=3,padx=1,pady=1)
sub.config(font=('verdana',15,'italic'))
cos=Button(root,text='cosx',bg='lightblue',fg='black',height=3,width=6,command=lambda:sqm('cos'))
cos.grid(row=3,column=4,padx=1,pady=1)
cos.config(font=('verdana',15,'italic'))
b1=Button(root,text='1',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('1'))
b1.grid(row=4,column=0,padx=1,pady=1)
b1.config(font=('verdana',15,'italic'))
b2=Button(root,text='2',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('2'))
b2.grid(row=4,column=1,padx=1,pady=1)
b2.config(font=('verdana',15,'italic'))
b3=Button(root,text='3',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('3'))
b3.grid(row=4,column=2,padx=1,pady=1)
b3.config(font=('verdana',15,'italic'))
add=Button(root,text='+',bg='grey',fg='black',height=3,width=6,command=lambda:operations('+'))
add.grid(row=4,column=3,padx=1,pady=1)
add.config(font=('verdana',15,'italic'))
tan=Button(root,text='tanx',bg='lightblue',fg='black',height=3,width=6,command=lambda:sqm('tan'))
tan.grid(row=4,column=4,padx=1,pady=1)
tan.config(font=('verdana',15,'italic'))
zerozero=Button(root,text='00',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('00'))
zerozero.grid(row=5,column=0,padx=1,pady=1)
zerozero.config(font=('verdana',15,'italic'))
zero=Button(root,text='0',bg='white',fg='black',height=3,width=6,command=lambda:get_digit('0'))
zero.grid(row=5,column=1,padx=1,pady=1)
zero.config(font=('verdana',15,'italic'))
dec=Button(root,text='.',bg='white',fg='black',height=3,width=5,command=lambda:get_digit('.'))
dec.grid(row=5,column=2,padx=1,pady=1)
dec.config(font=('verdana',16,'bold'))
equal=Button(root,text='=',bg='lightblue',fg='black',height=3,width=6,command=lambda:equals('='))
equal.grid(row=5,column=3,padx=1,pady=1)
equal.config(font=('verdana',15,'italic'))
fact=Button(root,text='fact',bg='lightblue',fg='black',height=3,width=6,command=lambda:sqm('fact'))
fact.grid(row=5,column=4,padx=1,pady=1)
fact.config(font=('verdana',15,'italic'))
root.mainloop()



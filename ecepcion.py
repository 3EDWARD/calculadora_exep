#Codigo creado por varios metodos visto y aprendidos 
#Se busco hacer el codigo lo mas simple podible
#Creado por "3DWARD"

from tkinter import *
def Suma():
          sum=int(int(entry.get())+int(entrada2.get())) #en esta parte sale error
          Label(root,text=sum).pack()

def divi():
          divi=int(int(entry.get())/int(entrada2.get())) 
          Label(root,text=divi).pack()

def multi():
          multi=int(int(entry.get())*int(entrada2.get())) 
          Label(root,text=multi).pack()


def resta():
          res=int(int(entry.get())-int(entrada2.get())) 
          Label(root,text=res).pack()

def validate(char, entry_value):
          if char in '1234567890.':     #esto es para validar solo numeros escritos aqui
              return True
          else:
              print('invalid: {s}'.format(s = char))
              return False

def validate2(char, entry_value):
          if char in '1234567890.':
               return True
          else:
              print('invalid: {s}'.format(s = char))
              return False

root = Tk()
vcmd = (root.register(validate), '%S', '%P')
entry = Entry(root, validate = 'key', validatecommand = vcmd)
entry.pack()
vcmd1 = (root.register(validate2), '%S', '%P')
entrada2 = Entry(root, validate='key',validatecommand =vcmd1)
entrada2.pack()

boton = Button(root,text="+",command= Suma).pack()

boton = Button(root,text="-",command= resta).pack()

boton = Button(root,text="/",command= divi).pack()

boton = Button(root,text="*",command= multi).pack()

root.mainloop()

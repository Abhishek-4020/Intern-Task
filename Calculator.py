from tkinter import *

def click(key):
    if key == '=':
        try:
            result.set(eval(result.get()))
        except:
            result.set('Error')
    elif key == 'C':
        result.set('')
    else:
        result.set(result.get() + key)

root = Tk()
root.title("Calculator")
result = StringVar()
Entry(root, textvariable=result, justify='right').grid(row=0, columnspan=4)

keys = ['7','8','9','/', '4','5','6','*', '1','2','3','-', 'C','0','=','+']
for i, key in enumerate(keys):
    Button(root, text=key, width=5, command=lambda k=key: click(k)).grid(row=1+i//4, column=i%4)

root.mainloop()
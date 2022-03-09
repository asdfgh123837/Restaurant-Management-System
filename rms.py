from tkinter import *

root = Tk()
root.geometry("930x400")
root['bg'] = 'yellow'
root.title("Restaurant Mangement Systems")

head_text = Label(font = ('times new roman', 50 , 'bold'), text = "Restaurant Mangement Systems", fg = "white", bg = "black").grid(row = 0, column = 0, columnspan = 5)

#entry goods
goods_1 = Label(font = ('times new roman', 12 , 'bold'), text = "Goods: 1", fg = "white", bg = "black").grid(row = 1, column = 0)
goods_2 = Label(font = ('times new roman', 12 , 'bold'), text = "Goods: 2", fg = "white", bg = "black").grid(row = 2, column = 0)
goods_3 = Label(font = ('times new roman', 12 , 'bold'), text = "Goods: 3", fg = "white", bg = "black").grid(row = 3, column = 0)

#entry function

entry_1 = Entry(root, justify = "right", borderwidth = 3)
entry_1.grid(row = 1, column = 1)

entry_2 = Entry(root, justify = "right", borderwidth = 3)
entry_2.grid(row = 2, column = 1)

entry_3 = Entry(root, justify = "right", borderwidth = 3)
entry_3.grid(row = 3, column = 1)

#insert total cost

entry_4 = Entry(root, justify = "right", borderwidth = 3)
entry_4.grid(row = 4, column = 1)


#goods cost
cost_1 = Label(font = ('times new roman', 12 , 'bold'), text = "2$", bg = 'yellow').grid(row = 1, column = 2)
cost_2 = Label(font = ('times new roman', 12 , 'bold'), text = "2$", bg = 'yellow').grid(row = 2, column = 2)
cost_3 = Label(font = ('times new roman', 12 , 'bold'), text = "2$", bg = 'yellow').grid(row = 3, column = 2)

#calculating

def btn_ttl():
    a = entry_1.get()
    a_1 = entry_1.get()
    a_2 = entry_1.get()
        
    sum = int(a) + int(a_1) + int(a_2)
    entry_4.insert(0, sum)

def btn_clr():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)

btn_ttl = Button(root, text = "Total", font = ('times new roman', 12 , 'bold'), fg = "white", bg = "black", command = btn_ttl).grid(row = 4, column = 0)

btn_clr = Button(root, text = "Clear", font = ('times new roman', 12 , 'bold'), fg = "white", bg = "black", command = btn_clr).grid(row = 5, column = 0)

#cancel
cancel = Button(root, text = "OK", font = ('times new roman', 12 , 'bold'), fg = "white", bg = "black", command = root.destroy).grid(row = 5, column = 3)


root.mainloop()

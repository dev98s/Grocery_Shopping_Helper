from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Grocery Shopping Helper")
root.geometry("400x430")
root.resizable(width=False, height=False)
root.configure(bg='grey')

label = Label(root, text="Choose Your Items-", font=('Helvetica', 25, 'bold', 'underline'), fg="snow")
label.grid(columnspan=2, sticky='e')
label.configure(bg="grey")

v = IntVar()

res = IntVar()

a = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

items = ['Bananas', 'Apples', 'Grapes', 'Strawberrys', 'Mangos', 'Cherrys']
price = [4, 6, 10, 12, 14, 18]


def loop(arr):
    new = ''
    for i in arr:
        new = new + i + "\n"
    return new


def cal_price():
    value = int(v.get())
    global a, c1, c2, c3, c4, c5, c6
    b = 0
    if value == 0:
        res.set(int(entry.get()) * price[0])
        b = int(entry.get()) * price[0]
        c1 += int(entry.get())
    elif value == 1:
        res.set(int(entry.get()) * price[1])
        b = int(entry.get()) * price[1]
        c2 += int(entry.get())
    elif value == 2:
        res.set(int(entry.get()) * price[2])
        b = int(entry.get()) * price[2]
        c3 += int(entry.get())
    elif value == 3:
        res.set(int(entry.get()) * price[3])
        b = int(entry.get()) * price[3]
        c4 += int(entry.get())
    elif value == 4:
        res.set(int(entry.get()) * price[4])
        b = int(entry.get()) * price[4]
        c5 += int(entry.get())
    elif value == 5:
        res.set(int(entry.get()) * price[5])
        b = int(entry.get()) * price[5]
        c6 += int(entry.get())
    a = a + b
    label5.config(text=a)
    amount.config(text=str(c1) + "\n" + str(c2) + "\n" + str(c3) + "\n" + str(c4) + "\n" + str(c5) + "\n" + str(c6))


def clr():
    global a, c1, c2, c3, c4, c5, c6
    label5.config(text=0)
    res.set(0)
    amount.config(text='0\n0\n0\n0\n0\n0')
    a = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0


r_btn = Radiobutton(root, text=items[0] + " (" + str(price[0]) + " rs/item)", variable=v, value=0,
                    font=('Helvetica', 10, 'bold'))
r_btn.grid(row=1, column=1, sticky="w")
r_btn.configure(bg="grey", fg='yellow')

r_btn1 = Radiobutton(root, text=items[1] + " (" + str(price[1]) + " rs/item)", variable=v, value=1,
                     font=('Helvetica', 10, 'bold'))
r_btn1.grid(row=2, column=1, sticky="w")
r_btn1.configure(bg="grey", fg='darkred')

r_btn2 = Radiobutton(root, text=items[2] + " (" + str(price[2]) + " rs/item)", variable=v, value=2,
                     font=('Helvetica', 10, 'bold'))
r_btn2.grid(row=3, column=1, sticky="w")
r_btn2.configure(bg="grey", fg='purple')

r_btn3 = Radiobutton(root, text=items[3] + " (" + str(price[3]) + " rs/item)", variable=v, value=3,
                     font=('Helvetica', 10, 'bold'))
r_btn3.grid(row=4, column=1, sticky="w")
r_btn3.configure(bg="grey", fg='pink')

r_btn4 = Radiobutton(root, text=items[4] + " (" + str(price[4]) + " rs/item)", variable=v, value=4,
                     font=('Helvetica', 10, 'bold'))
r_btn4.grid(row=5, column=1, sticky="w")
r_btn4.configure(bg="grey", fg='orange')

r_btn5 = Radiobutton(root, text=items[5] + " (" + str(price[5]) + " rs/item)", variable=v, value=5,
                     font=('Helvetica', 10, 'bold'))
r_btn5.grid(row=6, column=1, sticky="w")
r_btn5.configure(bg="grey", fg='violet')

label1 = Label(root, text="Price of selected items: ", font=('Helvetica', 10, 'bold'), fg='gold2')
label1.grid(row=10, column=0)
label1.configure(bg="grey")

label2 = Label(root, textvariable=res, font=('Helvetica', 10, 'bold'), fg='cyan')
label2.grid(row=10, column=1, sticky='w')
label2.configure(bg="grey")

label3 = Label(root, text="Enter Number of items->:", font=('Helvetica', 10, 'bold'))
label3.grid(row=8, column=0)
label3.configure(bg="grey")

entry = Entry(root, width=25)
entry.grid(row=8, column=1, sticky='e')

btn = Button(root, text="ADD ITEMS", width=15, command=lambda: cal_price(), fg='goldenrod4', bg='spring green')
btn.configure(font=('Helvetica', 10, 'bold'))
btn.grid(row=9, rowspan=2, column=1, sticky='e')

btn2 = Button(root, text="CLEAR", width=10, command=lambda: clr(), fg='ivory2', bg='purple3')
btn2.configure(font=('Helvetica', 10, 'bold'))
btn2.grid(row=9, column=0)

label4 = Label(root, text="Total Cost:", font=('Helvetica', 10, 'bold'))
label4.grid(row=11, column=0)
label4.configure(bg="grey", fg='maroon')

label5 = Label(root, text=a, font=('Helvetica', 10, 'bold'), fg='cyan')
label5.grid(row=11, column=1, sticky='w')
label5.configure(bg="grey")

label6 = Label(root, text="Items in your cart:", font=('Helvetica', 10, 'bold'), bg="grey")
label6.grid(row=12, columnspan=2, sticky='w')

lists = Label(root, text=loop(items), font=('Helvetica', 10, 'bold'), bg='grey', fg='darkblue')
lists.grid(row=13, column=0)

amount = Label(root, text='0\n0\n0\n0\n0\n0', font=('Helvetica', 10, 'bold'), bg='grey', fg='cyan')
amount.grid(row=13, column=1, sticky='nw')

img = Image.open('fruits.png')
img = img.resize((100, 120))

ph_img = ImageTk.PhotoImage(img)

pic_lab = Label(root, image=ph_img)
pic_lab.grid(row=1, rowspan=6, column=0)

names = Label(root, text='Project by-\nSuraj Malik', bg='grey', fg='yellow2',
              font=('Helvetica', 8, 'bold'))
names.grid(row=13, column=1, sticky='e')

root.mainloop()

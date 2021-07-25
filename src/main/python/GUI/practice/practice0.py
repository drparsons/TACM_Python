import tkinter as tk

window = tk.Tk()

#image can't exsist by itself so is contained in label
python_image = tk.PhotoImage(file='D:\\Pictures\\Python.png')
tk.Label(image=python_image, text="photo of me").pack()

greeting = tk.Label(
    text="Hello, World!",
    foreground="white",
    background="black",
    width=10,
    height=10)

button = tk.Button(
    text="click me!"
)

button2 = tk.Button(
    text="Click me too!",
    width=25,
    height=5,
    bg = "blue",
    fg = "#34A2FE"
)

entry = tk.Entry(
    fg = "yellow",
    bg = "blue",
    width=50
)
#passwd = tk.Entry(parent, textvariable=password, show="*")
#entry.get()
#entry.delete(0) #entry.delete(0, tk.END)
#entry.insert(0, "Python")

text_box = tk.Text()
#text_box.get("1.0", tk.END) #get all from row 1 word 0 to end


greeting.pack()
button.pack()
button2.pack()
entry.pack()
text_box.pack()

window.mainloop()
#window.destroy()
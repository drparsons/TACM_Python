"""
# Check box
measureSystem = StringVar()
check = ttk.Checkbutton(parent, text='Use Metric', 
	    command=metricChanged, variable=measureSystem,
	    onvalue='metric', offvalue='imperial')

# Radio Button
phone = StringVar()
home = ttk.Radiobutton(parent, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(parent, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(parent, text='Mobile', variable=phone, value='cell')

# Combo Box
countryvar = StringVar()
country = ttk.Combobox(parent, textvariable=countryvar)
country.bind('<<ComboboxSelected>>', function)
country['values'] = ('USA', 'Canada', 'Australia')
#readonly
country.state(["readonly"])

# List Box
l = Listbox(parent, height=10)
choices = ["apple", "orange", "banana"]
choicesvar = StringVar(value=choices)
l = Listbox(parent, listvariable=choicesvar)
...
choices.append("peach")
choicesvar.set(choices)

curselection
if lbox.selection_includes(2): ...

lbox.selection_set(idx)
lbox.see(idx)

# Scroll Bar
s = ttk.Scrollbar( parent, orient=VERTICAL, command=listbox.yview)
listbox.configure(yscrollcommand=s.set)
#--
l = Listbox(root, height=5)
l.grid(column=0, row=0, sticky=(N,W,E,S))
s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
s.grid(column=1, row=0, sticky=(N,S))
l['yscrollcommand'] = s.set
ttk.Label(root, text="Status message here", anchor=(W)).grid(column=0, columnspan=2, row=1, sticky=(W,E))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
for i in range(1,101):
    l.insert('end', 'Line %d of 100' % i)
root.mainloop()

# Scale 
s = ttk.Scale(parent, orient=HORIZONTAL, length=200, from_=1.0, to=100.0)

# spin Box
spinval = StringVar()
s = ttk.Spinbox(parent, from_=1.0, to=100.0, textvariable=spinval)

# Progress Bar
p = ttk.Progressbar(parent, orient=HORIZONTAL, length=200, mode='determinate')
"""
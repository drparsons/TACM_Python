import tkinter as tk

window = tk.Tk()

#output goes to console
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)
button.pack()
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

window.mainloop()

"""
#tkinter's mainloop() acts like a event machine like:

events_list = []

# Create an event handler
def handle_keypress(event):
    #Print the character associated to the key pressed
    print(event.char)

while True:
    if events_list == []:
        continue
    event = events_list[0]

    # If event is a keypress event object
    if event.type == "keypress":
        # Call the keypress event handler
        handle_keypress(event)

"""
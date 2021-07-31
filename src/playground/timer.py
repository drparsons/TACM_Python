
import tkinter as tk
import webbrowser
import time

# Create a window object
window = tk.Tk()

# Create Entry Object
entry = tk.Entry()

# Create an event handler
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

def handle_click(event):
    #Make separate thread to prevent window freezing
    start = time.time()
    x = entry.get()
    total = int(x)
    print("The button was clicked!")
    end = time.time()
    counter = 0

    while ((end-start) < total):
        time.sleep(1)
        end = time.time()
        counter += 1
        if counter == 5:
            #output to label
            print("Time left: {:.2f}".format((total - (end-start))))
            counter = 0
    #have label handle status
    print("done")
 
button = tk.Button(text="start")

entry.pack()
 
button.bind("<Button-1>", handle_click)
button.pack()

 
# Run the event loop
window.mainloop()
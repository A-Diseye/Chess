import tkinter as tk # Import the library, typically aliased as tk

# 1. Create the main application window
window = tk.Tk()
window.title("Chess") # Set the window title
window.geometry("400x200") # Set the window size (width x height)

# 2. Add widgets
label = tk.Label(window, text="Hello World!", font=("Arial", 16)) # Create a text label
label.pack(pady=20) # Arrange the label in the window using the pack() geometry manager

# A function to be called when the button is clicked
def on_button_click():
    label.config(text="Button Clicked!") # Update the label text

button = tk.Button(window, text="Click Me", command=on_button_click) # Create a button widget
button.pack(pady=10) # Arrange the button below the label

# 3. Enter the main event loop
window.mainloop() # Keeps the window running and interactive

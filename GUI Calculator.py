import tkinter as tk
from tkinter import ttk

# Define a CalculatorApp class to encapsulate the calculator logic and GUI
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        # Set the window title to "Calculator"
        self.root.title("Calculator")
        # Set the window size to 300x400 pixels
        self.root.geometry("300x400")
        # Allow the window to be resizable in both directions
        self.root.resizable(True, True)

        # Holds the mathematical expression entered by the user OR Initialize an empty string to store the current expression
        self.expression = '' 

        # Create a string variable to display the text
        self.display_text = tk.StringVar()

        # Create a frame to hold the display label (where numbers/results show up)
        display_frame = ttk.Frame(self.root)
        # Make the frame fill the available space and expand with resizing
        display_frame.pack(fill=tk.BOTH, expand=True)

        # Create the display label widget to serve as the calculator screen
        display_label = ttk.Label(
            display_frame,
            # Bind/link the label's text to the display_text variable
            textvariable=self.display_text,
            # Set font to Arial, size 24 for readability
            font=('Arial', 24),
            # Align text to the right (east) side of the label
            anchor='e',
            # Set background color to white
            background='white',
            # Set text color to black
            foreground='black',
            # Add padding of 6 pixels around the text
            padding=6
        )
        # Make the label fill the frame and expand with resizing
        display_label.pack(fill=tk.BOTH, expand=True)

        # Create a frame to hold all calculator buttons
        button_frame = tk.Frame(self.root)
        # Make the button frame fill the available space and expand with resizing
        button_frame.pack(fill=tk.BOTH, expand=True)

        # Call the method/function to create and arrange buttons
        self.create_buttons(button_frame) 

    def create_buttons(self, frame):
        # Define a list of tuples containing button text and their grid positions (row, column)
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]
        # Iterate through the buttons list to create and place each button
        for (text, row, col) in buttons:
            # Create a button with the specified text and link its click to on_button_click
            button = ttk.Button(
                frame,
                text=text,
                # Use lambda to pass the button's text to the click handler
                command=lambda t=text: self.on_button_click(t)
            )
            # Place the button in the grid at the specified row and column, making it resize with the grid
            button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

        # Configure rows and columns weight for resizing
        for i in range(6):
            # Set weight to 1 for each row to make them resize proportionally
            frame.rowconfigure(i, weight=1)
        for i in range(4):
            # Set weight to 1 for each column to make them resize proportionally
            frame.columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        # Handle the "C" button to clear the expression
        if button_text == 'C':
            self.expression = ''
        # Handle the "=" button to evaluate the expression
        elif button_text == '=':
            try:
                # Evaluate the expression and convert the result to a string
                self.expression = str(eval(self.expression))
            except Exception as e:
                # Display "Error" if evaluation fails (e.g., invalid expression)
                self.expression = 'Error'
        else:
            # Append the button's text (number or operator) to the current expression
            self.expression += button_text
        # Update the display with the current expression
        self.display_text.set(self.expression)

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    # Instantiate the CalculatorApp with the main window
    app = CalculatorApp(root)
    # Start the Tkinter event loop to run the application
    root.mainloop()



import functions
import PySimpleGUI as sg

# Ta metoda tworzy text instances/label instances
label = sg.Text('Type in a to-do:')

# Ta metoda tworzy input space
input_box = sg.InputText('Enter a todo')

# Ta metoda tworzy przyciski
add_button = sg.Button('Add')

# Layout -> Every single list element is a seperate rown, so if I wanted to put one row below another it would be like this: [[label][input_box]]
window = sg.Window('My To-Do App', [[label], [input_box, add_button]])

# Method read() displays a window on the screen.
window.read()
window.close()

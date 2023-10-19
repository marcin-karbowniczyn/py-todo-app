import functions
import PySimpleGUI as sg

label = sg.Text('Type in a to-do:')
input_box = sg.InputText('Enter a todo')
add_button = sg.Button('Add')

# Layout -> Every single list element is a seperate rown, so if I wanted to put one row below another it would be like this: [[label][input_box]]
window = sg.Window('My To-Do App', [[label], [input_box, add_button]])

# Method read() displays a window on the screen.
window.read()
window.close()

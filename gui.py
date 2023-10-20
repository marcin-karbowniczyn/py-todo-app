import functions
import PySimpleGUI as sg

# Ta metoda tworzy text instances/label instances
label = sg.Text('Type in a to-do:')

# Ta metoda tworzy input space
input_box = sg.InputText(tooltip='Enter a todo', key='todo')

# Ta metoda tworzy przyciski
add_button = sg.Button('Add')

# Layout -> Every single list element is a seperate rown, so if I wanted to put one row below another it would be like this: [[label][input_box]]. The third argument is a font and its size.
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]], font=('Helvetica', 15))

# Method read() displays a window on the screen. It also produces the event object, which contains the name of a button that was clicked, and also contents of input fields.
while True:
    event, values = window.read()
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo'] + '\n')
            functions.write_todos(todos)
            continue
        case sg.WIN_CLOSED:
            break

window.close()

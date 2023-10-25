import functions
import PySimpleGUI as sg

# Ta metoda tworzy text instances/label instances
label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip='Enter a todo', key='todo_input_box')
add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

list_box = sg.Listbox(
    values=functions.get_todos(),
    key='todosList',
    enable_events=True,
    size=(45, 10))

# Layout -> Every single list element is a seperate rown, so if I wanted to put one row below another it would be like this: [[label][input_box]]. The third argument is a font and its size.
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

# Method read() displays a window on the screen. It also produces the event object, which contains the name of a button that was clicked, and also contents of input fields.
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            todos.append(values['todo_input_box'] + '\n')
            functions.write_todos(todos)

            window['todosList'].update(values=todos)
            window['todo_input_box'].update(value='')

        case 'todosList':
            window['todo_input_box'].update(value=values['todosList'][0].replace('\n', ''))

        case 'Edit':
            todo_to_edit = values['todosList'][0]
            new_todo = values['todo_input_box'] + '\n'
            todos = functions.get_todos()
            todo_to_edit_index = todos.index(todo_to_edit)
            todos[todo_to_edit_index] = new_todo
            functions.write_todos(todos)

            # Wszystkie elementy są zapisane na obiekcie window i w taki sposób mamy do nich dostęp
            window['todosList'].update(values=todos)
            window['todo_input_box'].update(value='')

        case 'Complete':
            todo_to_complete = values['todosList'][0]
            todos = functions.get_todos()

            # Dwa sposoby na usunięcie elementu z listy
            # todos.pop(todos.index(todo_to_complete))
            todos.remove(todo_to_complete)

            functions.write_todos(todos)

            window['todosList'].update(values=todos)
            window['todo_input_box'].update(value='')

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

print('Bye')
window.close()

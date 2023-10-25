import time
import os
import functions
import PySimpleGUI as sg

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        # Możemy używać keyworda "pass" kiedy mamy kod w którym linijka musi być zapisana, ale nie potrzebujemy nic zapisywać. Lub jako placeholder
        pass

sg.theme('DarkGreen2')
# Ta metoda tworzy text instances/label instances
label_clock = sg.Text('', key='label_clock')
label = sg.Text('Type in a to-do:')
input_box = sg.InputText(tooltip='Enter a todo', key='todo_input_box')
add_button = sg.Button('Add', size=9)
edit_button = sg.Button('Edit', size=9)
complete_button = sg.Button('Complete', size=9)
exit_button = sg.Button('Exit', size=9)
btn_column = sg.Column([[edit_button], [complete_button]])

list_box = sg.Listbox(
    values=functions.get_todos(),
    key='todosList',
    enable_events=True,
    size=(45, 10))

# Layout -> Every single list element is a seperate rown, so if I wanted to put one row below another it would be like this: [[label][input_box]]. The third argument is a font and its size.
window = sg.Window('My To-Do App',
                   layout=[[label_clock],
                           [label],
                           [input_box, add_button],
                           [list_box, btn_column],
                           [exit_button]],
                   font=('Helvetica', 15))

# Method read() displays a window on the screen. It also produces the event object, which contains the name of a button that was clicked, and also contents of input fields.
while True:
    event, values = window.read(timeout=200)
    window['label_clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    # print(event, values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo_input_box'] + '\n'

            # Check if a new todoo isn't an empty string
            if len(new_todo.replace(' ', '')) < 3:
                sg.popup('A todo must be at least 3 characters long.', title='Error')
                window['todo_input_box'].update(value='')
                continue

            todos.append(new_todo)
            functions.write_todos(todos)

            window['todosList'].update(values=todos)
            window['todo_input_box'].update(value='')

        case 'todosList':
            window['todo_input_box'].update(value=values['todosList'][0].replace('\n', ''))

        case 'Edit':
            try:
                todo_to_edit = values['todosList'][0]
                new_todo = values['todo_input_box'] + '\n'

                # Check if a new todoo isn't an empty string
                if len(new_todo.replace(' ', '')) < 3:
                    sg.popup('A todo must be at least 3 characters long.', title='Error')
                    window['todo_input_box'].update(value='')
                    continue

                todos = functions.get_todos()
                todo_to_edit_index = todos.index(todo_to_edit)
                todos[todo_to_edit_index] = new_todo
                functions.write_todos(todos)

                # Wszystkie elementy są zapisane na obiekcie window i w taki sposób mamy do nich dostęp
                window['todosList'].update(values=todos)
                window['todo_input_box'].update(value='')

            except IndexError:
                sg.popup('Please select an item first.', title='Error', font=('Helvetica', 12))

        case 'Complete':
            try:
                todo_to_complete = values['todosList'][0]
                todos = functions.get_todos()

                # Dwa sposoby na usunięcie elementu z listy
                # todos.pop(todos.index(todo_to_complete))
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todosList'].update(values=todos)
                window['todo_input_box'].update(value='')

            except IndexError:
                sg.popup('Please select an item first.', title='Error', font=('Helvetica', 12))

        case 'Exit':
            break

        case sg.WIN_CLOSED:
            break

print('Bye')
window.close()

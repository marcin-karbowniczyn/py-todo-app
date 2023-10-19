# W TYM PLIKU USUNĄŁEM SPORO KOMENTARZY I NIE MA W NIM KODU Z LEKCJI SPRZED IF/ELSE BLOCS. TEN KOD JEST W main-match-case-before-if.py !!

# from functions import get_todos, write_todos
# from modules import functions -> gdyby plik functions był w folderze modules
import functions  # Skrypt functions.py jest wykonywany w momencie importu
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f"It is {now}")
wrong_command_msg = 'Your command is not valid.'
while True:
    user_action = input("Type add, edit, complete, show or exit show: ")
    user_action = user_action.strip()  # Get user input and strip space chars from it

    # 'in' i 'or' operators, || === or, && === and, not in === !==
    # if 'add' in user_action or 'new' in user_action:

    if user_action.startswith('add'):
        # list slicing, wycinamy string od 4 znaku, indexowane oczywiście od 0, może też być [4:11] czyli start i koniec wycięcia.
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:]) - 1
            edited_todo = input('Enter a new todo: ')

            todos = functions.get_todos()

            todos[number] = f"{edited_todo}\n"

            functions.write_todos(todos)

            print('Todo has been edited.')
        # W pythonie trzeba sprecyzować jaki error ma nastąpić, żeby wykonać kod z bloku except.
        except ValueError:
            print(wrong_command_msg)
            continue  # Działa tak samo jak w JS, od razu przechodzi do kolejnej iteracji

    elif user_action.startswith('complete'):
        try:
            number_of_todo = int(user_action[9:])

            todos = functions.get_todos()

            index = number_of_todo - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo '{todo_to_remove.title()}' has been removed.")

        except IndexError:
            print(f"Wrong number, please insert a number from 1 to {len(todos)}")
            continue

        except ValueError:
            print(wrong_command_msg)
            continue

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        # # List comprehension -> Iterator przechodzi przez każdy item w liście todos, i zwraca w jego miejsce wynik działania item.strip('\n')
        # todos_without_backslash = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            # FSTRING, CZYLI COŚ JAK TEMPLATE LITERALS W JS, GDZIE MOŻEMY DODAĆ ZMIENNE DO STRINGS !!!!!!!!
            item = item.strip('\n')
            print(f"{index + 1}. {item.capitalize()}")
        print(f"This TODO list has {len(todos)} elements.")

    elif user_action.startswith('exit'):
        break

    else:
        print('Wrong command, please type add, show or exit: ')

print('Bye!')

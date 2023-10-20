FILEPATH = 'todos.txt'  # Tak zapisujemy zmienne w modułach, można je później przejrzeć za pompcą funkcji dir(), np. dir(functions)


# Filepath w definicji to parameter, a przy wywoływaniu funkcji to argument.
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    # 'With context menager' zastępujemy nim zapis powyżej, nie musimy używać file.close(). Używamy go głównie dlatego, że jak wysypie się program, i iterator nie dotrze do file.close()
    # to możemy zostać z niezamkniętym plikiem w systemie i to może stwarzać problemy. Dlategho lepiej korzystać z with cotnext menager. W drugim pliku pokazana stara wersja zapisu kodu.
    """ Write the to-do items list into the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# W taki sposób ukrywamy ten print() w main.py
if __name__ == "__main__":
    print(get_todos())

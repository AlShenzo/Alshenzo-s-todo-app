FILEPATH = 'todos.txt' # this is a constant to store things like a variable


def get_todos(filepath=FILEPATH):
    """read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the next file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


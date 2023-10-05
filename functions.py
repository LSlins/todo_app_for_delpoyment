def get_todos(filepath='todos.txt'):
    """ Read the text file and return the list of to-do item. """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(tasks, filepath='todos.txt'):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as file:
        todos = file.writelines(tasks)


if __name__ == '__main__':
    print('I study so that I can run away the life I don\'t like.')
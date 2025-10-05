FILEPATH = "todos.txt"  # better to use .txt instead of .text

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of todo items."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the todo items list into the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    todos = get_todos()
    print("Current todos.txt contents:")
    for line in todos:
        print(line.strip())
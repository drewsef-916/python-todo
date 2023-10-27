import time
from functions import get_todos, write_todos

while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number - 1] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            idx = number - 1
            todo_to_remove = todos[idx].strip("\n")
            todos.pop(idx)

            write_todos(todos)

            print(f"{todo_to_remove} complete!")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("You entered an unknown command")

print("Bye!")
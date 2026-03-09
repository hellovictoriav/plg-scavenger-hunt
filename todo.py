tasks = []


def main():
    print("Welcome to Todo App")
    while True:
        command = input("> ").strip()
        if command == "quit":
            break
        elif command == "list":
            if not tasks:
                print("No tasks.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif command.startswith("add "):
            task = command[4:].strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("Commands: add [task], list, quit")
        else:
            print("Commands: add [task], list, quit")


if __name__ == "__main__":
    main()

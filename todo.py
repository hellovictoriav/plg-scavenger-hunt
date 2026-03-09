tasks = []
completed = set()


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
                    mark = "✓ " if i in completed else "  "
                    print(f"{i}. {mark}{task}")
        elif command.startswith("add "):
            task = command[4:].strip()
            if task:
                tasks.append(task)
                print(f"Added: {task}")
            else:
                print("Usage: add [task]")
        elif command.startswith("done "):
            arg = command[5:].strip()
            if arg.isdigit() and 1 <= int(arg) <= len(tasks):
                n = int(arg)
                completed.add(n)
                print(f"Marked done: {tasks[n - 1]}")
            else:
                print(f"Invalid task number: '{arg}'. Use 'list' to see available tasks.")
        else:
            print("Unknown command. Commands: add [task], list, done [number], quit")


if __name__ == "__main__":
    main()

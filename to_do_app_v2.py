import readchar

menu = [
    "1. Check All Tasks",
    "2. Add New Task",
    "3. Update Task",
    "4. Delete Task",
    "5. Exit",
]
to_do_list = []


def main():
    selected = 0
    while True:
        print("\033c", end="")
        print("\n=== TO DO APP ===")
        show_menu(selected)
        key = readchar.readkey()

        if key == readchar.key.UP:
            selected = (selected - 1) % len(menu)
        elif key == readchar.key.DOWN:
            selected = (selected + 1) % len(menu)
        elif key == readchar.key.ENTER:
            print("\033c", end="")
            print("\n=== TO DO APP ===")
            if selected == 0:
                list_task()
            elif selected == 1:
                add_new_task()
            elif selected == 2:
                update_task()
            elif selected == 3:
                delete_task()
            elif selected == 4:
                print("Exiting the program. See you later!👋 ")
                break
            input("\nPress ENTER to return to the menu...")


def show_menu(selected):
    print("Use ↑ ↓ keys to navigate, ENTER to select\n")
    for i, item in enumerate(menu):
        if i == selected:
            print(f"> {item} <")
        else:
            print(f"  {item}")


def list_task():
    print("\n📋 To Do List:")
    if not to_do_list:
        print("🛑 Nothing To Do.")
    else:
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")


def add_new_task():
    task = input("\n➕ Enter new description task:\n")
    to_do_list.append(task)
    print("✅Task added.")


def update_task():
    list_task()
    if to_do_list:
        try:
            index = int(input("\n🔁 Select the task number you want to update: ")) - 1
            if 0 <= index < len(to_do_list):
                updated = input("Enter a new task description:\n")
                to_do_list[index] = updated
                print("✅ Task updated.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a number.")


def delete_task():
    list_task()
    if to_do_list:
        try:
            index = int(input("\n🗑️ Select the task number you want to delete:\n")) - 1
            if 0 <= index < len(to_do_list):
                removed = to_do_list.pop(index)
                print(f"✅ Task '{removed}' deleted")
            else:
                print("❌ Invalid task number")
        except ValueError:
            print("⚠️ Please enter a number.")


if __name__ == "__main__":
    main()

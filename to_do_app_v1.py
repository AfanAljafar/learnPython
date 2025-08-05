menu = [
    "1. Read the All Task",
    "2. Add New Task ",
    "3. Update Task",
    "4. Delete Task",
    "5. keluar",
]
to_do_list = []


def main():
    while True:
        show_menu()
        choice = input("choose your action: ")

        if int(choice) == 1:
            list_task()
        elif int(choice) == 2:
            add_new_task()
        elif int(choice) == 3:
            update_task()
        elif int(choice) == 4:
            delete_task()
        elif int(choice) == 5:
            print("exit program")
            break
        else:
            print("Invalid selection, please try again.")


def show_menu():
    print("\nTo Do App")
    for i in menu:
        print(i)


def list_task():
    if not to_do_list:
        print("Nothing To Do, Lets Add New Task")
    else:
        for i, task in enumerate(to_do_list, start=1):
            print(f"{i}. {task}")


def add_new_task():
    task = input("add your new task: \n")
    to_do_list.append(task)
    print("New task added succesfuly")


def update_task():
    list_task()
    if to_do_list:
        try:
            index = int(input("Which task number do you want to update? : ")) - 1
            if 0 <= index < len(to_do_list):
                updated_task = input("input changes: \n")
                to_do_list[index] = updated_task
                print("changes saved successfully")
            else:
                print("invalid selection")
        except ValueError:
            print("enter valid number")


def delete_task():
    list_task()
    if to_do_list:
        try:
            index = int(input("Which task number do you want to delete? : ")) - 1
            if 0 <= index < len(to_do_list):
                deleted = to_do_list.pop(index)
                print(f"task {index + 1}. {deleted} deleted.")
            else:
                print("invalid selection")
        except ValueError:
            print("enter valid number.")


if __name__ == "__main__":
    main()

todo_list = []

def show_menu():
    print("\nTo Do List App")
    print("Pilih menu:")
    print("1. Lihat daftar To Do")
    print("2. Buat tugas baru")
    print("3. Update tugas")
    print("4. Hapus tugas")
    print("5. Keluar")

def list_tasks():
    if not todo_list:
        print("Daftar tugas kosong.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Masukkan nama tugas: ")
    todo_list.append(task)
    print("Tugas berhasil ditambahkan.")

def update_task():
    list_tasks()
    if todo_list:
        try:
            index = int(input("Pilih nomor tugas yang ingin diubah: ")) - 1
            if 0 <= index < len(todo_list):
                new_task = input("Masukkan tugas baru: ")
                todo_list[index] = new_task
                print("Tugas berhasil diubah.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")

def delete_task():
    list_tasks()
    if todo_list:
        try:
            index = int(input("Pilih nomor tugas yang ingin dihapus: ")) - 1
            if 0 <= index < len(todo_list):
                deleted = todo_list.pop(index)
                print(f"Tugas '{deleted}' berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")

while True:
    show_menu()
    choice = input("Pilih menu (1-5): ")
    
    if choice == "1":
        list_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")

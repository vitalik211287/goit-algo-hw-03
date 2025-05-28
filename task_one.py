from pathlib import Path
import shutil

# # Створення об'єкту Path для директорії

start_directory = Path(input("👉 Введіть ПЕРШИЙ шлях (звідки копіювати): ").strip('" '))
dest_input = input("👉 Введіть ДРУГИЙ шлях (куди копіювати): ").strip('" ')
dest_directory = Path(dest_input) if dest_input else Path("dist")

def moving_content(start_directory, dest_directory):
    # while 
    for path in start_directory.iterdir():
        # print(path)
        if path.is_file():
            shutil.copy(path, dest_directory)
        elif path.is_dir():
            moving_content(path, dest_directory)
    

       
    # shutil.copy(start_directory, dest_directory)


    # print(f"📁 Початкова директорія: {start_directory}")
    # print(f"📂 Кінцева директорія: {dest_directory}")

    # # Приклад використання
    # if not start_directory.exists():
    #     print("❗ Початкова директорія не існує.")
    # if not dest_directory.exists():
    #     print("❗ Кінцева директорія не існує.")

moving_content(start_directory, dest_directory)






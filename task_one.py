# from pathlib import Path
# import shutil

# # # Створення об'єкту Path для директорії

# start_directory = Path(input("👉 Введіть ПЕРШИЙ шлях (звідки копіювати): ").strip('" '))
# dest_input = input("👉 Введіть ДРУГИЙ шлях (куди копіювати): ").strip('" ')
# dest_directory = Path(dest_input) if dest_input else Path("dist")

# def moving_content(start_directory, dest_directory):
#         for path in start_directory.iterdir():
#             name_directory = path.suffix[1:] or "unknown"
#             if path.is_file():
#                 new_directory= dest_directory/name_directory
#                 new_directory.mkdir(parents=True, exist_ok=True)
#                 shutil.copy(path, new_directory/path.name)
#             elif path.is_dir():
#                 moving_content(path, dest_directory)
# print("переміщення відбулось успішно")

# moving_content(start_directory, dest_directory)


from pathlib import Path
import shutil

# Створення об'єкту Path для директорії
start_directory = Path(input("👉 Введіть ПЕРШИЙ шлях (звідки копіювати): ").strip('" '))
dest_input = input("👉 Введіть ДРУГИЙ шлях (куди копіювати): ").strip('" ')
dest_directory = Path(dest_input) if dest_input else Path("dist")

def moving_content(start_directory, dest_directory):
    try:
        for path in start_directory.iterdir():
            name_directory = path.suffix[1:] or "unknown"
            if path.is_file():
                try:
                    new_directory = dest_directory / name_directory
                    new_directory.mkdir(parents=True, exist_ok=True)
                    shutil.copy(path, new_directory / path.name)
                except Exception as e:
                    print(f"❌ Помилка копіювання файлу {path}: {e}")
            elif path.is_dir():
                moving_content(path, dest_directory)
    except PermissionError:
        print(f"⛔ Немає доступу до {start_directory}")
    except Exception as e:
        print(f"⚠️ Сталася помилка в {start_directory}: {e}")

moving_content(start_directory, dest_directory)
print("✅ Переміщення відбулося успішно")

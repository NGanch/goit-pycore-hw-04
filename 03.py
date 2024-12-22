import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init()


def visualize_directory_structure(directory_path):
    try:
        # Перетворюємо шлях на об'єкт Path
        root_path = Path(directory_path)

        # Перевірка, чи шлях існує та є директорією
        if not root_path.exists():
            print(Fore.RED + "Помилка: Шлях не існує." + Style.RESET_ALL)
            return

        if not root_path.is_dir():
            print(Fore.RED + "Помилка: Це не директорія." + Style.RESET_ALL)
            return

        # Рекурсивний обхід директорії
        for item in root_path.rglob("*"):

            indent_level = len(item.relative_to(root_path).parts) - 1
            indent = "    " * indent_level

            if item.is_dir():
                # Директорії - синій колір
                print(Fore.BLUE +
                      f"{indent}📂 {item.relative_to(root_path)}" + Style.RESET_ALL)
            else:
                # Файли - зелений колір
                print(Fore.GREEN +
                      f"{indent}📜 {item.relative_to(root_path)}" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Сталася помилка: {e}" + Style.RESET_ALL)


# if name == "main":
if __name__ == "__main__":
    # Отримання шляху до директорії з аргументів командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: python script.py /шлях/до/директорії" + Style.RESET_ALL)
    else:
        directory_path = sys.argv[1]
        visualize_directory_structure(directory_path)
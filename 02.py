def get_cats_info(path):
    try:
        # Відкриваємо файл з вказаним шляхом
        with open(path, "r", encoding="utf-8") as file:
            cats_info = []  # Список для зберігання інформації про котів

            # Читаємо кожен рядок у файлі
            for line in file:
                try:
                    # Розділяємо ідентифікатор, ім'я і вік
                    cat_id, name, age = line.strip().split(",")
                    # Формуємо словник для кота
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    # Додаємо словник у список
                    cats_info.append(cat_dict)
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line.strip()}")

            return cats_info

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []

# Приклад використання функції
if __name__ == "__main__":
    path_to_file = "cats_file.txt"  # Задайте правильний шлях до файлу
    cats_info = get_cats_info(path_to_file)
    print(cats_info)
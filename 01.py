def total_salary(path):
    try:
        # Відкриваємо файл з вказаним шляхом
        with open(path, "r", encoding="utf-8") as file:
            salaries = []  # Список для зберігання зарплат

            # Читаємо кожен рядок у файлі
            for line in file:
                try:
                    # Розділяємо прізвище і зарплату
                    _, salary = line.strip().split(",")
                    salaries.append(float(salary))  # Додаємо зарплату у список
                except ValueError:
                    print(f"Некоректний рядок у файлі: {line.strip()}")

            # Перевіряємо, чи є дані про зарплати
            if not salaries:
                return (0, 0)

            total = sum(salaries)  # Загальна сума зарплат
            average = total / len(salaries)  # Середня зарплата

            return (total, average)

    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях до файлу.")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)

# Приклад використання функції
if __name__ == "__main__":
    path_to_file = "salary_file.txt"  # Задайте правильний шлях до файлу
    total, average = total_salary(path_to_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

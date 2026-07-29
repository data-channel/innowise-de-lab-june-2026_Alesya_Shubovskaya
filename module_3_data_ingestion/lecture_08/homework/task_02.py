# Входные данные
branches = [
    {"city": "Minsk", "revenue": 15000},
    {"city": "Warsaw", "revenue": 32000},
    {"city": "London", "revenue": 12000}
]

# Декоратор, который логирует запуск и завершение функции
def audit_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[AUDIT] Запуск анализа...")
        result = func(*args, **kwargs)    # Вызываем исходную функцию
        print(f"[AUDIT] Анализ завершен.")
        return result    # Возвращаем результат
    return wrapper

# Основная функция с декоратором
@audit_logger
def get_sorted_report(branches):
    sorted_branches = sorted(branches, key=lambda x: x["revenue"], reverse=True)
    return sorted_branches

# Вызов функции и результат
sorted_data = get_sorted_report(branches)

print("\nТоп филиалов:")
for i, branch in enumerate(sorted_data, start=1):
    print(f"{i}. {branch['city']}: {branch['revenue']}")

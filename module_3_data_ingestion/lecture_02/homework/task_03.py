# Инициализация входных данных
raw_sku = "CARROT-001"  # артикул товара (строка, корректный)
raw_regions = ("Minsk", "Warsaw", "Berlin", "Warsaw")  # кортеж регионов (с повторами)
raw_weight_str = "2.5"  # вес товара в виде строки
raw_stock_str = "150"  # количество на складе в виде строки

# Явное преобразование типов
weight_kg = float(raw_weight_str)
stock_quantity = int(raw_stock_str)

# Преобразование коллекций
sku_as_list = list(raw_sku)  # строка → список символов
regions_list = list(raw_regions)  # кортеж → список
unique_regions = set(raw_regions)  # кортеж → множество (удаляются дубликаты)
regions_tuple = tuple(unique_regions)   # множество → кортеж

# Пустые списки
empty_list_1 = []
empty_list_2 = list()

# Пустые словари
empty_dict_1 = {}
empty_dict_2 = dict()

# Пустые кортежи
empty_tuple_1 = ()
empty_tuple_2 = tuple()

# Пустое множество (только 1 способ)
empty_set = set()

# # Проверка пустых коллекций
# print(bool(empty_list_2))   # False
# print(bool(empty_dict_1))   # False
# print(bool(empty_tuple_2))  # False
# print(bool(empty_set))      # False

# Непустые коллекции
non_empty_list = [1, 2, 3]
non_empty_dict = {"a": 8, "b": 6}
non_empty_tuple = (5, 6, 7)
non_empty_set = {7, 8, 9}

# # Проверка непустых коллекций
# print(bool(non_empty_list))   # True
# print(bool(non_empty_dict))   # True
# print(bool(non_empty_tuple))  # True
# print(bool(non_empty_set))    # True

# Преобразованные данные
print(weight_kg, type(weight_kg))
print(stock_quantity, type(stock_quantity))
print(sku_as_list, type(sku_as_list))
print(regions_list, type(regions_list))
print(unique_regions, type(unique_regions))
print(regions_tuple, type(regions_tuple))

print(bool(empty_list_2))
print(bool(empty_dict_1))
print(bool(empty_tuple_2))
print(bool(empty_set))

print(bool(non_empty_list))
print(bool(non_empty_dict))
print(bool(non_empty_tuple))
print(bool(non_empty_set))

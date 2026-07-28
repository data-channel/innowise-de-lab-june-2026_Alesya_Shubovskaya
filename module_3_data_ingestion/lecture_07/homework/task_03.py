# Исходные данные, список
suppliers_log = [
	"FreshFarm Inc",
	"GreenFields Ltd",
	"AgroWorld Co",
	"FreshFarm Inc",
	"GreenFields Ltd"
]

# 1. Преобразование в множество
unique_suppliers = set(suppliers_log)

# 2. Попытка добавить поставщика
unique_suppliers.add("GreenFields Ltd")
#print(unique_suppliers)

# 3. Проврка наличия элемента в множестве
if "FreshFarm Inc" in unique_suppliers:
    print("True")

# 4. Итоговый отчет
print(unique_suppliers)
print(len(unique_suppliers))
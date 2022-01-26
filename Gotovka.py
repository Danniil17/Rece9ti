with open('food.txt.', encoding="utf8") as f:
    data = f.read()
    print(data)


person_count = int(str(input('Введите количество гостей:')))
print(f"Гостей в количестве {person_count} лиц")

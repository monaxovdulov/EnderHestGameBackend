import sqlite3

# 1. Подключение к базе данных (если базы данных не существует, она будет создана)
conn = sqlite3.connect('mydatabase.db') #  'mydatabase.db' - имя файла базы данных

# 2. Создание курсора - объект для выполнения SQL-запросов
cursor = conn.cursor()

# 3. Создание таблицы (если таблица не существует)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- целочисленный первичный ключ, автоинкремент
    username TEXT NOT NULL,                -- текстовое поле, обязательное для заполнения
    password TEXT NOT NULL                 -- целочисленное поле
)
""")

# 4. Вставка данных в таблицу
users_data = [
    ('Alice', 30),
    ('Bob', 25),
    ('Charlie', 35)
]

cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_data)

# 5. Сохранение изменений (фиксация транзакции)
conn.commit()

# 6. Выполнение запроса на выборку данных
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall() # Получение всех строк результата запроса

# 7. Вывод полученных данных
print("Данные из таблицы users:")
for row in rows:
    print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}")

# 8. Закрытие соединения с базой данных
conn.close()

print("\nРабота с SQLite завершена.")

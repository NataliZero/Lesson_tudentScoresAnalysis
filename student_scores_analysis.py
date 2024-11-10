import pandas as pd

# Создание данных
data = {
    'Имя': ['Ученик 1', 'Ученик 2', 'Ученик 3', 'Ученик 4', 'Ученик 5', 'Ученик 6', 'Ученик 7', 'Ученик 8', 'Ученик 9', 'Ученик 10'],
    'Математика': [85, 90, 78, 92, 88, 76, 95, 89, 84, 91],
    'Литература': [78, 85, 80, 90, 79, 82, 87, 84, 86, 88],
    'Физика': [90, 85, 88, 92, 84, 79, 91, 86, 89, 87],
    'Химия': [88, 79, 92, 85, 90, 82, 84, 88, 91, 80],
    'История': [82, 89, 85, 78, 88, 92, 80, 84, 87, 86]
}

# Создание DataFrame
df = pd.DataFrame(data)

# Проверка первых строк
print("Первые строки DataFrame:")
print(df.head())

# Средняя оценка по каждому предмету
mean_scores = df[['Математика', 'Литература', 'Физика', 'Химия', 'История']].mean()
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

# Медианная оценка по каждому предмету
median_scores = df[['Математика', 'Литература', 'Физика', 'Химия', 'История']].median()
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

# Q1 и Q3 для математики
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 для математики: {Q1_math}")
print(f"Q3 для математики: {Q3_math}")

# IQR для математики
IQR_math = Q3_math - Q1_math
print(f"IQR для математики: {IQR_math}")

# Стандартное отклонение по каждому предмету
std_scores = df[['Математика', 'Литература', 'Физика', 'Химия', 'История']].std()
print("\nСтандартное отклонение по каждому предмету:")
print(std_scores)

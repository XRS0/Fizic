import pandas as pd
import matplotlib.pyplot as plt

# Функция для рассчета изменения температуры
def calculate_temperature_change(mass_processor, specific_heat_processor, mass_cooler, specific_heat_cooler):
    # Формула: ΔT = Q / (m * C)
    # Предположим, что количество тепла (Q) равно 100 для примера
    heat = 100
    
    # Рассчитываем изменение температуры для процессора
    delta_t_processor = heat / (mass_processor * specific_heat_processor)

    # Рассчитываем изменение температуры для охлаждающего элемента
    # При условии, что процессор выключается при температуре 100 ℃
    max_temperature = 100
    temperature_difference = max_temperature - delta_t_processor

    delta_t_cooler = temperature_difference / (mass_cooler * specific_heat_cooler)

    return delta_t_cooler

# Ввод данных от пользователя
mass_processor_values = [float(x) for x in input("Введите значения массы процессора (кг) через запятую: ").split(',')]
specific_heat_processor_values = [float(x) for x in input("Введите значения удельной теплоемкости процессора (Дж/(г*°C)) через запятую: ").split(',')]
mass_cooler_values = [float(x) for x in input("Введите значения массы охлаждающего элемента (кг) через запятую: ").split(',')]
specific_heat_cooler_values = [float(x) for x in input("Введите значения удельной теплоемкости охлаждающего элемента (Дж/(г*°C)) через запятую: ").split(',')]

# Создание DataFrame с введенными данными
data = {
    'Масса процессора (кг)': mass_processor_values,
    'Удельная теплоемкость процессора (Дж/(г*°C))': specific_heat_processor_values,
    'Масса охлаждающего элемента (кг)': mass_cooler_values,
    'Удельная теплоемкость охлаждающего элемента (Дж/(г*°C))': specific_heat_cooler_values,
}

df = pd.DataFrame(data)

# Рассчитываем изменение температуры и добавляем в DataFrame
df['Изменение температуры охлаждающего элемента (°C)'] = df.apply(
    lambda row: calculate_temperature_change(row['Масса процессора (кг)'], row['Удельная теплоемкость процессора (Дж/(г*°C))'],
                                             row['Масса охлаждающего элемента (кг)'], row['Удельная теплоемкость охлаждающего элемента (Дж/(г*°C))']),
                                             axis=1
)

# Сохранение в Excel-файл
df.to_excel("temperature_change_graph_cooler_pandas_variable.xlsx", index=False)

# Построение графика
plt.plot(df.index, df['Изменение температуры охлаждающего элемента (°C)'], marker='o')
plt.title('Изменение температуры охлаждающего элемента')
plt.xlabel('Номер значения')
plt.ylabel('Изменение температуры охлаждающего элемента (°C)')
plt.show()

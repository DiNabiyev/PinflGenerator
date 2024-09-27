import random
from datetime import datetime, timedelta


def calculate_control_digit(pinfl):
    """Вычисление контрольной цифры ПИНФЛ"""
    weights = [7, 3, 1]  # Весовые коэффициенты
    total_sum = 0

    for i, digit in enumerate(pinfl):  # Обрабатываем все 13 цифр ПИНФЛ
        weight = weights[i % 3]  # Циклически повторяем веса 7, 3, 1
        total_sum += int(digit) * weight

    control_digit = total_sum % 10  # Контрольная цифра - остаток от деления на 10
    return control_digit


def generate_random_birth_date():
    """Генерация случайной даты рождения между 01.01.1920 и 31.12.2006"""
    start_date = datetime(1920, 1, 1)  # Стартовая дата - 1 января 1920 года
    end_date = datetime(2006, 12, 31)  # Конечная дата - 31 декабря 2006 года

    # Генерация случайного количества дней между начальной и конечной датой
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)

    # Добавляем случайное количество дней к начальной дате
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime("%d%m%y"), random_date.year


def determine_gender_century_index(year, gender):
    """Определение индекса пола и века рождения на основе года рождения и пола"""
    if 1920 <= year <= 1999:
        return 3 if gender == 'male' else 4  # 3 - мужчины, 4 - женщины, 20 век
    elif 2000 <= year <= 2006:  # только до 2006 года
        return 5 if gender == 'male' else 6  # 5 - мужчины, 6 - женщины, 21 век


def generate_pinfl():
    """Основная функция генерации ПИНФЛ"""
    # Генерация случайной даты рождения до 31.12.2006
    birth_date, year = generate_random_birth_date()

    # Случайное определение пола
    gender = random.choice(['male', 'female'])

    # Определение индекса пола и века рождения
    gender_century_index = determine_gender_century_index(year, gender)

    region_code = str(random.randint(1, 9))  # Генерация случайного кода региона (1-9)
    serial_number = str(random.randint(0, 99999)).zfill(4)  # Порядковый номер (4 цифры)

    # Формирование первых 13 цифр ПИНФЛ
    pinfl_without_control_digit = f"{gender_century_index}{birth_date}{region_code}{serial_number}"

    # Вычисление контрольной цифры
    control_digit = calculate_control_digit(pinfl_without_control_digit)

    # Полный ПИНФЛ (14 цифр)
    pinfl = pinfl_without_control_digit + str(control_digit)

    return pinfl, gender, birth_date, year


# Пример генерации ПИНФЛ
pinfl, gender, birth_date, year = generate_pinfl()

# Определение корректного отображения года в зависимости от века
if year >= 2000:
    full_year = f"20{birth_date[4:]}"
else:
    full_year = f"19{birth_date[4:]}"

print(f"Сгенерированный ПИНФЛ: {pinfl}")  # Проверка длины здесь
print(f"Пол: {gender}")
print(f"Дата рождения: {birth_date[:2]}.{birth_date[2:4]}.{full_year}")

# Проверка длины сгенерированного ПИНФЛ
print(f"Длина сгенерированного ПИНФЛ: {len(pinfl)}")  # Это должно вывести 14

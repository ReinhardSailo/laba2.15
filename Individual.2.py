#!/usr/bin/env python 3
# –*– coding: utf–8 –*–
import string

def calculate_letter_frequency(filename):
    # Создаем словарь для хранения частоты букв
    letter_frequency = {letter: 0 for letter in string.ascii_lowercase}

    with open(filename, 'r') as file:
        content = file.read().lower()  # Приводим все к нижнему регистру
        content = ''.join(ch for ch in content if ch.isalpha() or ch.isspace())  # Удаляем знаки препинания

        total_letters = 0
        for letter in content:
            if letter.isalpha():
                total_letters += 1
                letter_frequency[letter] += 1

        # Находим букву, которая встречается реже всего
        rarest_letter = min(letter_frequency, key=letter_frequency.get)

        # Рассчитываем проценты использования каждой буквы
        for letter in letter_frequency:
            letter_frequency[letter] = (letter_frequency[letter] / total_letters) * 100

    return letter_frequency, rarest_letter

# Замените 'gadsby.txt' на путь к вашему файлу
letter_frequency, rarest_letter = calculate_letter_frequency('file2.txt')

# Выводим результаты
for letter, frequency in letter_frequency.items():
    print(f'{letter}: {frequency:.2f}%')

print(f'\nНаименее часто встречающаяся буква: {rarest_letter}')

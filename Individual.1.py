#!/usr/bin/env python 3
# –*– coding: utf–8 –*–
def find_sentences_with_dash(filename):
    with open(filename, 'r') as file:
        content = file.read()
        sentences = content.split('.')
        for sentence in sentences:
            if sentence.strip().startswith('-'):
                print(sentence.strip())

# Замените 'example.txt' на путь к вашему файлу
find_sentences_with_dash('example.txt')

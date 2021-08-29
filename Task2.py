# Write a function that has two arguments - a letter, and a text. The function should return the number of times when a letter appears in the text.
# Написать функцию которая принимает 2 аргумента - букву и текст.
# Создать счётчик буквы.
# Проитерироваться по каждой букве в тексте.
# Если нужная буква, то прибавить в счётчик.
# Вернуть счётчик.
#* Решить в одну строку (без компрехеншена).

def letter(text):
    new_list = []

    for a in text:
        new_list.append((a, len(set(a))))

    new_list = [(a, len(set(a))) for a in text]

    new_list = sorted(new_list, key=lambda x: x[-1], reverse=True)[:3]
    print(new_list)
    return [w[0] for w in new_list]

if __name__ == '__main__':
    words = ['a', 'London is a capital of Great Britain']

    print(letter(words))

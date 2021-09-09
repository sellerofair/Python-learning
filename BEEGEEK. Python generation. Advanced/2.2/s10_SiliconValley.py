# Кремниевая долина

# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
# и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число nn – количество холодильников.
# В последующих nn строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 55 до 100100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел.
# Если таких холодильников нет, ничего выводить не нужно.


sequence = [input() for _ in range(int(input()))]

sick_numbers = []
current_letter_in_anton = 0
sick_founded = False

for i in range(len(sequence)):

    for letter in sequence[i]:
        if letter == 'anton'[current_letter_in_anton]:
            if current_letter_in_anton == 4:
                sick_founded = True
                sick_numbers.append(i + 1)
                current_letter_in_anton = 0
                break
            else:
                current_letter_in_anton += 1

    if sick_founded:
        sick_founded = False
        continue

    current_letter_in_anton = 0

print(*sick_numbers)

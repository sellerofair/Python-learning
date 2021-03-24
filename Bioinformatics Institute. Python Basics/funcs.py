''' Сюда сложил полезные функции '''

# считывание дерева в формате "Новый_элемент : Родитель_1 Родитель_2 ...  Родитель_N"
# в словарь, указанный в качестве аргумента

def read_tree(tree):
    for _ in range(int(input())):
        line = input()
        sep_position = line.find(':')
        if sep_position == -1:
            tree[line] = {}
        else:
            tree[line[:sep_position - 1]] = set(line[sep_position + 2:].split())


# является ли node1 предком node2 в дереве tree

def is_parent(tree, node1, node2):
    result = False
    if len(tree[node2]) > 0:
        if node1 in tree[node2]:
            result = True
        else:
            for class3 in tree[node2]:
                if is_parent(tree, node1, class3):
                    result = True
                    break

    return result
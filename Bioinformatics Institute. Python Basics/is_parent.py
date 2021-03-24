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
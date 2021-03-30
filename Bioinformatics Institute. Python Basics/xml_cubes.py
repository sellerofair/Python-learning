'''
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
Кубики, расположенные прямо под ним, имеют ценность 2.
Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.
Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
'''


from xml.etree import ElementTree

def modify_values(colors_dict, element, level_value):
    colors_dict[element.attrib['color']] += level_value
    for child in element:
        modify_values(colors_dict, child, level_value + 1)

with open('cubes.xml', 'w') as f:
    f.write(input())

tree = ElementTree.parse('cubes.xml')
root = tree.getroot()

values = {
    'red': 0,
    'green': 0,
    'blue': 0
}

modify_values(values, root, 1)

print(values['red'], values['green'], values['blue'])
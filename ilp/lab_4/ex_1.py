#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white', 'text': 'vasya'}

]

# Реализация задания 1
g = field(goods, 'text')
print(next(g))
print(next(g))
# print(*field(goods, 'text', 'рus'))
# print(*gen_random(1, 9, 5))
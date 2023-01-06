from Table import Table
from Word import Word

table = Table(10, 10)

diagonal_right = Word(
    text='palavra1',
    position=(1, 1),
    orientation='DIAGONAL_RIGHT'
)
diagonal_left = Word(
    text='palavra2',
    position=(0, 8),
    orientation='DIAGONAL_LEFT',
    inverted=True
)

try:
    table.add_word(diagonal_right)
    table.add_word(diagonal_left)
except Exception as error:
    print(error)
table.show()

from Table import Table
from Word import Word

table = Table(15, 15)

horizontal = Word(
    text='HORIZONTAL',
    position=(0, 0),
    orientation='HORIZONTAL',
    inverted=True
)
vertical = Word(
    text='VERTICAL',
    position=(1, 0),
    orientation='VERTICAL',
    inverted=True
)
diagonal_right = Word(
    text='DIAGONAL_RIGHT',
    position=(1, 1),
    orientation='DIAGONAL_RIGHT',
    inverted=True
)
diagonal_left = Word(
    text='LEFT',
    position=(10, 8),
    orientation='DIAGONAL_LEFT',
    inverted=True
)

table.add_word(horizontal)
table.add_word(vertical)
table.add_word(diagonal_right)
table.add_word(diagonal_left)
table.show()

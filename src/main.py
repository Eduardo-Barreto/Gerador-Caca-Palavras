from Table import Table
from Word import Word

table = Table(15, 15)

long_test = Word(
    text='isso_obviamente_não_cabe_numa_table_15x15',
    position=(0, 0),
    orientation='HORIZONTAL'
)
normal_test = Word(
    text='essa_cabe',
    position=(1, 0),
    orientation='DIAGONAL_RIGHT'
)

table.add_word(long_test)
table.add_word(normal_test)
table.show()

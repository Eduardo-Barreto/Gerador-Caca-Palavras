from Table import Table
from Word import Word

table = Table(10, 10)
words = [
    'python',
    'caça',
    'abacate',
    'irra'
]

for word_text in words:
    word = Word(
        text=word_text
    )
    word.randomize_orientation()
    word.randomize_position(table.rows, table.cols)
    table.force_add_word(word)

table.fill_table_with_random_letters()
table.show()
table.print_words()

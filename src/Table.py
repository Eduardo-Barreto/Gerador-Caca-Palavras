from Word import Word

orientation_increment_map = {
    'HORIZONTAL': (0, 1),
    'VERTICAL': (1, 0),
    'DIAGONAL_LEFT': (1, -1),
    'DIAGONAL_RIGHT': (1, 1)
}


class Table:
    '''
    Classe que representa um caça palavras
    '''

    def __init__(self, rows: int = 10, cols: int = 10) -> None:
        '''
        Inicializador da classe

        Parâmetros:
        ----------
        rows: int
            Número de linhas do caça palavras

        cols: int
            Número de colunas do caça palavras
        '''
        self.table = [['0' for i in range(rows)] for j in range(cols)]
        self.rows = rows
        self.cols = cols

    def add_word(self, word: Word) -> None:
        '''
        Adiciona uma palavra ao caça palavras

        Parâmetros:
        ----------
        word: Word
            Palavra a ser adicionada
        '''
        # TODO: Adicionar validação: sobreposição
        row, col = word.position
        row_increment = orientation_increment_map[word.orientation][0]
        col_increment = orientation_increment_map[word.orientation][1]

        end_row = row + (row_increment * len(word.text))
        if end_row > self.rows:
            print(f'Palavra não cabe na table: {word.text}')
            return

        end_col = col + (col_increment * len(word.text))
        if end_col > self.cols:
            print(f'Palavra não cabe na table: {word.text}')
            return

        if word.inverted:
            word.text = word.text[::-1]

        for letter in word.text:
            self.table[row][col] = letter
            row += row_increment
            col += col_increment

    def show(self) -> None:
        '''
        Mostra o caça palavras
        '''
        for row in self.table:
            print(' '.join(row))

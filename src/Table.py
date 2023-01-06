import copy

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

    def word_fits(self, word: Word) -> bool:
        '''
        Verifica se a palavra cabe no caça palavras

        Parâmetros:
        ----------
        word: Word
            Palavra a ser verificada

        Retorno:
        -------
        bool
            True se a palavra cabe no caça palavras
        '''
        row, col = word.position
        row_increment = orientation_increment_map[word.orientation][0]
        col_increment = orientation_increment_map[word.orientation][1]

        end_row = row + (row_increment * len(word.text))
        if end_row > self.rows:
            return False

        end_col = col + (col_increment * len(word.text))
        if end_col > self.cols:
            return False

        return True

    def add_word(self, word: Word) -> None:
        '''
        Adiciona uma palavra ao caça palavras

        Parâmetros:
        ----------
        word: Word
            Palavra a ser adicionada
        '''
        row, col = word.position
        row_increment = orientation_increment_map[word.orientation][0]
        col_increment = orientation_increment_map[word.orientation][1]

        if not self.word_fits(word):
            raise Exception('Palavra não cabe no caça palavras')

        if word.inverted:
            word.text = word.text[::-1]

        initial_table = copy.deepcopy(self.table)

        for letter in word.text:
            if self.table[row][col] not in ['0', letter]:
                self.table = initial_table
                raise Exception('Sobreposição de palavras')

            self.table[row][col] = letter
            row += row_increment
            col += col_increment

    def show(self) -> None:
        '''
        Mostra o caça palavras
        '''
        for row in self.table:
            print(' '.join(row))

import copy
from random import choice
from string import ascii_lowercase

from Word import Word
from Exceptions import (
    WordOverlapError,
    WordDoesNotFitError,
    MaxTriesExceededError
)

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
        self.words = []

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
        text = word.text

        if not self.word_fits(word):
            raise WordDoesNotFitError('Palavra não cabe no caça palavras')

        if word.inverted:
            text = text[::-1]

        initial_table = copy.deepcopy(self.table)

        for letter in text:
            if self.table[row][col] not in ['0', letter]:
                self.table = initial_table
                raise WordOverlapError('Sobreposição de palavras')

            self.table[row][col] = letter
            row += row_increment
            col += col_increment

        self.words.append(word)

    def force_add_word(self, word: Word, max_tries: int = 5) -> None:
        '''
        Tenta adicionar uma palavra ao caça palavras, gerando uma nova posição
        se necessário

        Parâmetros:
        ----------
        word: Word
            Palavra a ser adicionada
        '''
        try_count = 0
        while word not in self.words:
            if try_count == max_tries:
                raise MaxTriesExceededError(
                    f'Não foi possível adicionar a palavra "{word.text}"'
                )

            try:
                self.add_word(word)
            except WordOverlapError:
                word.randomize_position(self.rows, self.cols)

            try_count += 1

    def fill_table_with_random_letters(self) -> None:
        '''
        Preenche o caça palavras com letras aleatórias
        '''
        for row in range(self.rows):
            for col in range(self.cols):
                if self.table[row][col] == '0':
                    self.table[row][col] = choice(ascii_lowercase)

    def print_words(self) -> None:
        '''
        Mostra as palavras do caça palavras
        '''
        for word in self.words:
            print(word.text)

    def show(self) -> None:
        '''
        Mostra o caça palavras
        '''
        for row in self.table:
            print(' '.join(row))

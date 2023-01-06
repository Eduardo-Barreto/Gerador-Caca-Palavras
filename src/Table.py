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
        # TODO: Adicionar validação para verificar se a palavra cabe
        # TODO: Adicionar validação para verificar se a palavra não se sobrepõe a outra
        row, col = word.position

        if word.inverted:
            word.text = word.text[::-1]

        for letter in word.text:
            self.table[row][col] = letter
            row += orientation_increment_map[word.orientation][0]
            col += orientation_increment_map[word.orientation][1]

    def show(self) -> None:
        '''
        Mostra o caça palavras
        '''
        for row in self.table:
            print(' '.join(row))

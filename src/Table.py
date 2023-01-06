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

    def show(self) -> None:
        '''
        Mostra o caça palavras
        '''
        for row in self.table:
            print(' '.join(row))

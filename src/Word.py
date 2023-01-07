import random
# from Table import orientation_increment_map


class Word:
    def __init__(
        self,
        text: str,
        position: tuple = (-1, -1),
        orientation: str = 'RANDOM',
        inverted: bool = False
    ) -> None:
        '''
        Inicializador da classe

        Parâmetros:
        ----------
        text: str
            Texto da palavra

        position: tuple
            Posição da palavra no caça palavras

        orientation: int
            Orientação da palavra no caça palavras

        inverted: bool
            Indica se a palavra está invertida
        '''

        self.text = text
        self.position = position
        self.orientation = orientation
        self.inverted = inverted

    def randomize_position(self, rows: int, cols: int) -> None:
        '''
        Gera uma posição aleatória

        Parâmetros:
        ----------
        table: Table
            Tabela do caça palavras
        '''
        if self.orientation == 'HORIZONTAL':
            col = random.randint(0, cols-len(self.text))
            row = random.randint(0, rows-1)

        elif self.orientation == 'VERTICAL':
            col = random.randint(0, cols-1)
            row = random.randint(0, rows-len(self.text))

        elif self.orientation == 'DIAGONAL_RIGHT':
            col = random.randint(0, cols-len(self.text))
            row = random.randint(0, rows-len(self.text))

        elif self.orientation == 'DIAGONAL_LEFT':
            col = random.randint(len(self.text), cols-1)
            row = random.randint(0, rows-len(self.text))

        self.position = (row, col)

    def randomize_orientation(self) -> None:
        '''
        Gera uma orientação aleatória
        '''
        self.orientation = random.choice(
            [
                'HORIZONTAL',
                'VERTICAL',
                'DIAGONAL_RIGHT',
                'DIAGONAL_LEFT'
            ]
        )

class Word:
    def __init__(
        self,
        text: str,
        position: tuple,
        orientation: int,
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

class WordOverlapError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class WordDoesNotFitError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class MaxTriesExceededError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

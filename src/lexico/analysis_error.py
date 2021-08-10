class AnalysisError(Exception):

    def __init__(self, msg, position = -1):

        self.msg = msg
        self.position = position
        super().__init__(msg)

    def getPosition(self):

        return self.position

    def __str__(self):

        return 'Erro na linha ' + str(self.position) + " - " + self.msg 

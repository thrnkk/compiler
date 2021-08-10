class Token(object):

    def __init__(self, id, lexeme, position):

        self.id = id
        self.lexeme = lexeme
        self.position = position
        self.classes = ['', 
                        '', 
                        'identificador', 
                        'constante int', 
                        'constante float', 
                        'constante str', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'palavra reservada', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial', 
                        'simbolo especial' 
                        ]

    def getId(self):

        return self.id

    def getClass(self):

        return self.classes[self.id]

    def getLexeme(self):

        return self.lexeme

    def getPosition(self):

        return self.position

    def __str__(self):

        return str(self.id) + " ( " + self.lexeme + " ) @ " + str(self.position)
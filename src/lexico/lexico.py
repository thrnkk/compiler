from .constants import Constants
from .lexical_error import LexicalError
from .token import Token

class Lexico(Constants):

    def __init__(self, input = None):

        Constants.__init__(self)

        self.position = 0
        self.input = input
        self.linha = [-1]

    def countLines(self):

        pos = 0

        for char in self.input:

            if (pos not in self.linha and char == '\n'):

                self.linha.append(pos)

            pos += 1

    def checkLine(self, pos):

        cont = 0

        for breakLine in self.linha:

            if (pos > breakLine):

                cont += 1

        return cont

    def setInput(self, input):

        self.input = input
        self.setPosition(0)
        self.countLines()

    def setPosition(self, pos):

        self.position = pos

    def hasInput(self):

        return self.position < len(self.input)

    def nextChar(self):
        

        if (self.hasInput()):

            valor = self.input[self.position]

            self.position += 1

            return valor

        else:

            return -1

    def lookupToken(self, base, key):

        start = self.SPECIAL_CASES_INDEXES[base]
        end = self.SPECIAL_CASES_INDEXES[base + 1] - 1

        while (start <= end):

            half = int((start + end) / 2)
            comp = ((self.SPECIAL_CASES_KEYS[half] > key) - (self.SPECIAL_CASES_KEYS[half] < key))

            if (comp == 0):

                return self.SPECIAL_CASES_VALUES[half]

            elif (comp < 0):

                start = half + 1

            else: # (comp > 0)

                end = half - 1

        return base

    def tokenForState(self, state):
        

        if (state < 0 or state >= len(self.TOKEN_STATE)):

            return -1

        return self.TOKEN_STATE[state]

    def nextState(self, c, state):

        start = self.SCANNER_TABLE_INDEXES[state]
        end = self.SCANNER_TABLE_INDEXES[state + 1] - 1

        while (start <= end):

            half = int((start + end) / 2)

            if (self.SCANNER_TABLE[half][0] == ord(c)):

                return self.SCANNER_TABLE[half][1]

            elif (self.SCANNER_TABLE[half][0] < ord(c)):

                start = half + 1

            else: # (self.SCANNER_TABLE[half][0] > c)

                end = half - 1

        return -1

    def nextToken(self):

        if (not self.hasInput()):

            return None

        start = self.position

        state = 0
        lastState = 0
        endState = -1
        end = -1

        while (self.hasInput()):
            lastState = state
            state = self.nextState(self.nextChar(), state)
            
            if (state < 0):

                break

            else:

                if (self.tokenForState(state) >= 0):

                    endState = state
                    end = self.position
                    

        if (endState < 0 or self.tokenForState(lastState) == -2):

            # Caractere não encontrado
            if (lastState == 0):

                retorno = self.input[start] + ' ' + self.SCANNER_ERROR[lastState]

                raise LexicalError(retorno, self.checkLine(start))

            else:

                raise LexicalError(self.SCANNER_ERROR[lastState], self.checkLine(start))

        self.position = end

        token = self.tokenForState(endState)

        if (token == 0):

            return self.nextToken()

        else:

            lexeme = self.input[start : end]
            token = self.lookupToken(token, lexeme)
            return Token(token, lexeme, self.checkLine(start))

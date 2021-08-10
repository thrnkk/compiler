from .constants import Constants
from .syntatic_error import SyntaticError
from .lexico import Lexico
from .token import Token

class Sintatico(Constants):

    def __init__(self):

        Constants.__init__(self)

        self.stack = []
        self.currentToken = None
        self.previousToken = None
        self.scanner = None
        self.semanticAnalyser = None

    def isTerminal(self, x):

        return x < self.FIRST_NON_TERMINAL

    def isNonTerminal(self, x):

        return x >= self.FIRST_NON_TERMINAL and x < self.FIRST_SEMANTIC_ACTION

    def isSemanticAction(self, x):

        return x >= self.FIRST_SEMANTIC_ACTION
    
    def step(self):

        if self.currentToken is None:

            # pos = 0
            pos = 1
            if self.previousToken is not None:

                # pos = self.previousToken.getPosition() + len(self.previousToken.getLexeme())
                pos = self.previousToken.getPosition()

            self.currentToken = Token(self.DOLLAR, '$', pos)

        x = int(self.stack.pop())
        a = self.currentToken.getId()

        if x == self.EPSILON:

            return False

        elif self.isTerminal(x):

            if x == a:

                if len(self.stack) == 0:

                    return True

                else:

                    self.previousToken = self.currentToken
                    self.currentToken = self.scanner.nextToken()
                    return False

            else:

                raise SyntaticError(f"encontrado {self.currentToken.getLexeme()} {self.PARSER_ERROR[x]}", self.currentToken.getPosition())

        elif self.isNonTerminal(x):

            if self.pushProduction(x, a):

                return False

            else:

                raise SyntaticError(f"encontrado {self.currentToken.getLexeme()} {self.PARSER_ERROR[x]}", self.currentToken.getPosition())

        else:

            self.semanticAnalyser.executeAction(x - self.FIRST_SEMANTIC_ACTION, self.previous)
            return False

    def pushProduction(self, topStack, tokenInput):

        p = self.PARSER_TABLE[topStack - self.FIRST_NON_TERMINAL][tokenInput - 1]
        if p >= 0:

            production = self.PRODUCTIONS[p]

            for i in range(len(production) - 1, -1, -1):

                self.stack.append(int(production[i]))

            return True

        else:

            return False

    def parse(self, scanner, semanticAnalyser):

        self.scanner = scanner
        self.semanticAnalyser = semanticAnalyser

        self.stack = []
        self.stack.append(int(self.DOLLAR))
        self.stack.append(int(self.START_SYMBOL))

        self.currentToken = scanner.nextToken()

        while not self.step():

            pass


from .scanner_constants import ScannerConstants
from .parser_constants import ParserConstants

class Constants(ScannerConstants, ParserConstants):

    def __init__(self):

        ScannerConstants.__init__(self)
        ParserConstants.__init__(self)

        self.EPSILON  = 0
        self.DOLLAR   = 1

        self.t_identificador = 2
        self.t_constante_int = 3
        self.t_constante_float = 4
        self.t_constante_str = 5
        self.t_and = 6
        self.t_or = 7
        self.t_not = 8
        self.t_if = 9
        self.t_elif = 10
        self.t_else = 11
        self.t_for = 12
        self.t_in = 13
        self.t_range = 14
        self.t_while = 15
        self.t_end = 16
        self.t_false = 17
        self.t_true = 18
        self.t_input = 19
        self.t_int = 20
        self.t_float = 21
        self.t_str = 22
        self.t_print = 23
        self.t_TOKEN_24 = 24 #"("
        self.t_TOKEN_25 = 25 #")"
        self.t_TOKEN_26 = 26 #"=="
        self.t_TOKEN_27 = 27 #"!="
        self.t_TOKEN_28 = 28 #"<"
        self.t_TOKEN_29 = 29 #"<="
        self.t_TOKEN_30 = 30 #">"
        self.t_TOKEN_31 = 31 #">="
        self.t_TOKEN_32 = 32 #"+"
        self.t_TOKEN_33 = 33 #"-"
        self.t_TOKEN_34 = 34 #"*"
        self.t_TOKEN_35 = 35 #"/"
        self.t_TOKEN_36 = 36 #"//"
        self.t_TOKEN_37 = 37 #"%"
        self.t_TOKEN_38 = 38 #","
        self.t_TOKEN_39 = 39 #":"
        self.t_TOKEN_40 = 40 #"="
        self.t_TOKEN_41 = 41 #"+="
        self.t_TOKEN_42 = 42 #"-="

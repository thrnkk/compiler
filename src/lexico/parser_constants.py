class ParserConstants(object):

    def __init__(self):

        self.START_SYMBOL = 43

        self.FIRST_NON_TERMINAL    = 43
        self.FIRST_SEMANTIC_ACTION = 70

        self.PARSER_TABLE = [
                [ -1,  0, -1, -1, -1, -1, -1, -1,  3, -1, -1,  1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [  4,  5, -1, -1, -1, -1, -1, -1,  5,  4,  4,  5, -1, -1,  5,  4, -1, -1, -1, -1, -1, -1,  5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  6,  7,  7,  7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1,  8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 14, 15, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 11, 11, 11, 11, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, -1, 11, 11, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1, 11, 11, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 23, -1, -1, -1, -1, -1, -1, 23, -1, -1, 23, -1, -1, 23, -1, -1, -1, -1, -1, -1, -1, 23, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, 25, 24, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 27, -1, -1, -1, -1, 26, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 36, -1, -1, 35, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 37, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 28, 29, 30, 31, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 32, -1, -1, -1, -1, -1, -1, -1, 33, 34, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17, 18, 19 ],
                [ -1, 20, 20, 20, 20, -1, -1, 20, -1, -1, -1, -1, -1, -1, -1, -1, 20, 20, 21, 21, 21, 21, -1, 20, -1, -1, -1, -1, -1, -1, -1, 20, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 39, 39, 39, 39, -1, -1, 39, -1, -1, -1, -1, -1, -1, -1, -1, 39, 39, -1, -1, -1, -1, -1, 39, -1, -1, -1, -1, -1, -1, -1, 39, 39, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ 42, 42, -1, -1, -1, 40, 41, -1, 42, 42, 42, 42, -1, -1, 42, 42, -1, -1, -1, -1, -1, -1, 42, -1, 42, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 42, 42, -1, -1, -1 ],
                [ -1, 58, 58, 58, 58, -1, -1, 61, -1, -1, -1, -1, -1, -1, -1, -1, 60, 59, -1, -1, -1, -1, -1, 58, -1, -1, -1, -1, -1, -1, -1, 58, 58, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ 44, 44, -1, -1, -1, 44, 44, -1, 44, 44, 44, 44, -1, -1, 44, 44, -1, -1, -1, -1, -1, -1, 44, -1, 44, 45, 45, 45, 45, 45, 45, -1, -1, -1, -1, -1, -1, 44, 44, -1, -1, -1 ],
                [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 43, 43, 43, 43, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 43, -1, -1, -1, -1, -1, -1, -1, 43, 43, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ -1, 62, 62, 62, 62, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, -1, -1, -1, -1, 62, 62, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ 63, 63, -1, -1, -1, 63, 63, -1, 63, 63, 63, 63, -1, -1, 63, 63, -1, -1, -1, -1, -1, -1, 63, -1, 63, 63, 63, 63, 63, 63, 63, 64, 65, -1, -1, -1, -1, 63, 63, -1, -1, -1 ],
                [ -1, 52, 52, 52, 52, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 52, -1, -1, -1, -1, -1, -1, -1, 52, 52, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                [ 53, 53, -1, -1, -1, 53, 53, -1, 53, 53, 53, 53, -1, -1, 53, 53, -1, -1, -1, -1, -1, -1, 53, -1, 53, 53, 53, 53, 53, 53, 53, 53, 53, 54, 55, 56, 57, 53, 53, -1, -1, -1 ]
            ]

        self.PRODUCTIONS = [
                    [  2, 58, 44 ],
                    [ 55, 44 ],
                    [ 48, 44 ],
                    [ 51, 44 ],
                    [  0 ],
                    [ 43 ],
                    [ 19, 24, 46 ],
                    [ 47, 24, 19, 24, 46 ],
                    [  5, 25 ],
                    [ 25 ],
                    [ 23, 24, 49, 25 ],
                    [ 60, 50 ],
                    [  0 ],
                    [ 38, 60, 50 ],
                    [ 20 ],
                    [ 21 ],
                    [ 22 ],
                    [ 40, 59 ],
                    [ 41, 60 ],
                    [ 42, 60 ],
                    [ 60 ],
                    [ 45 ],
                    [  9, 60, 39, 52, 53, 54 ],
                    [ 43 ],
                    [  0 ],
                    [ 10, 60, 39, 52, 53 ],
                    [ 16 ],
                    [ 11, 39, 52, 16 ],
                    [  2 ],
                    [  3 ],
                    [  4 ],
                    [  5 ],
                    [ 24, 60, 25 ],
                    [ 32, 57 ],
                    [ 33, 57 ],
                    [ 15, 60, 39, 52, 16 ],
                    [ 12,  2, 13, 56 ],
                    [ 14, 24, 60, 25, 39, 52, 16 ],
                    [  2, 39, 52, 16 ],
                    [ 62, 61 ],
                    [  6, 62, 61 ],
                    [  7, 62, 61 ],
                    [  0 ],
                    [ 66, 63 ],
                    [  0 ],
                    [ 64, 66 ],
                    [ 26 ],
                    [ 27 ],
                    [ 28 ],
                    [ 29 ],
                    [ 30 ],
                    [ 31 ],
                    [ 57, 69 ],
                    [  0 ],
                    [ 34, 57, 69 ],
                    [ 35, 57, 69 ],
                    [ 36, 57, 69 ],
                    [ 37, 57, 69 ],
                    [ 65 ],
                    [ 18 ],
                    [ 17 ],
                    [  8, 62 ],
                    [ 68, 67 ],
                    [  0 ],
                    [ 32, 68, 67 ],
                    [ 33, 68, 67 ]
                ]

        self.PARSER_ERROR = [
                "",
                "esperado fim de programa",
                "esperado identificador",
                "esperado constante_int",
                "esperado constante_float",
                "esperado constante_str",
                "esperado and",
                "esperado or",
                "esperado not",
                "esperado if",
                "esperado elif",
                "esperado else",
                "esperado for",
                "esperado in",
                "esperado range",
                "esperado while",
                "esperado end",
                "esperado false",
                "esperado true",
                "esperado input",
                "esperado int",
                "esperado float",
                "esperado str",
                "esperado print",
                "esperado \"(\"",
                "esperado \")\"",
                "esperado \"==\"",
                "esperado \"!=\"",
                "esperado \"<\"",
                "esperado \"<=\"",
                "esperado \">\"",
                "esperado \">=\"",
                "esperado \"+\"",
                "esperado \"-\"",
                "esperado \"*\"",
                "esperado \"/\"",
                "esperado \"//\"",
                "esperado \"%\"",
                "esperado \",\"",
                "esperado \":\"",
                "esperado \"=\"",
                "esperado \"+=\"",
                "esperado \"-=\"",
                "esperada uma gramatica bnf",
                "esperada uma gramatica bnf",
                "esperada uma entrada",
                "esperada uma entrada",
                "esperado tipo",
                "esperada uma saida",
                "esperada uma express??o",
                "esperada uma express??o",
                "esperado um select",
                "esperada uma lista de comandos",
                "esperado elif",
                "esperado else",
                "esperado repeat",
                "esperado repeat",
                "esperado fator",
                "esperado um auxiliar",
                "esperado um auxiliar",
                "esperada uma express??o",
                "esperada uma express??o",
                "esperado um elemento",
                "esperado relacional",
                "esperado operador relacional",
                "esperado relacional",
                "esperada aritmetica",
                "esperada aritmetica",
                "esperado termo",
                "esperado termo"
            ];

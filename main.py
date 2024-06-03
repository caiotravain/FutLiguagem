import sys
from abc import abstractmethod



class Token :
    def __init__(self, tipo: str, valor: int):
        self.tipo = tipo
        self.valor = valor


class Tokenizer :
    def __init__(self, source: str, position: int, next: Token):
        self.source = source
        self.position = position
        self.next = next
        self.lista = ["PRINT", "TEAM", "PASSES", "SCORES", "SHOOTS", "REDCARD", "MATCH", "PLAYER", "SKILL", "PRINT", "AddPlayer","BALLCONTROL", "ENDMATCH", "MATCHTIME", "if", "else", "end", "VS"]
        

    def selectNext(self):
        try:
            if self.source[self.position] == '\n' :
                self.position += 1
                self.next = Token("quebra", 0)
                return
        except:
            self.next = Token("EOF", 0)
            return
        while self.position < len(self.source) and self.source[self.position].isspace():
            self.position += 1
        if self.position == len(self.source):
            self.next = Token("EOF", 0)
            return
  
        elif self.source[self.position] in ["+", "-","*","/"]:
            self.next = Token("sinal", self.source[self.position])
            self.position += 1
            return
        elif self.source[self.position].isdigit() :
            numero = ""
            while self.position < len(self.source) and self.source[self.position].isdigit():
                numero += self.source[self.position]
                self.position += 1
            self.next = Token("numero", int(numero))
            return
        elif self.source[self.position] == "(" :
            self.next = Token("abre", 0)
            self.position += 1
            return
        elif self.source[self.position] == "{" :
            self.next = Token("chave_abre", 0)
            self.position += 1
            return
        elif self.source[self.position] == "}" :
            self.next = Token("chave_fecha", 0)
            self.position += 1
            return
        elif self.source[self.position] == ")" :
            self.next = Token("fecha", 0)
            self.position += 1
            return
        elif self.source[self.position] == "=" :
            if self.source[self.position + 1] == "=":
                self.next = Token("sinal", "==")
                self.position += 2
                return
            self.next = Token("igual", 0)
            self.position += 1
            return
        elif self.source[self.position] == "<" :
            self.next = Token("sinal", "<")
            self.position += 1
            return
        elif self.source[self.position] == ">" :
            self.next = Token("sinal", ">")
            self.position += 1
            return
        elif self.source[self.position] == "."  and self.source[self.position + 1] == ".":
            self.next = Token("sinal", "..")
            self.position += 2
            return
        elif self.source[self.position] == "." :
            self.next = Token("ponto", 0)
            self.position += 1
            return
        elif self.source[self.position] == "," :
            self.next = Token("virgula", 0)
            self.position += 1
            return
        elif self.source[self.position] == "\"" :
            self.position += 1
            palavra = ""
            while self.position < len(self.source) and self.source[self.position] != "\"":
                palavra += self.source[self.position]
                self.position += 1
                if self.position == len(self.source):
                    sys.stderr.write("Erro: Falta aspas")
                    sys.exit(1)
            self.position += 1
            self.next = Token("string", palavra)
            return
        elif self.source[self.position].isalpha() or ("_"  == self.source[self.position]):
            identificador = ""
            while self.position < len(self.source) and (self.source[self.position].isalpha() or self.source[self.position].isdigit() or ("_"  == self.source[self.position])):
                identificador += self.source[self.position]
                self.position += 1
            if identificador in self.lista:
                
                self.next = Token(identificador, 0)
            else:
                self.next = Token("identificador", identificador)
            
            return
        

        self.next = Token("invalido", 0)
        return
    
class Parser:

    def __init__(self, tokenizer: Tokenizer):
        self.tokenizer = tokenizer     

    @staticmethod
    def parseExpression(tokenizer: Tokenizer):
        resultado = Parser.parseTerm(tokenizer)
        while tokenizer.next.valor == "+" or tokenizer.next.valor == "-" or tokenizer.next.valor == "..":
            if tokenizer.next.tipo == "sinal":
                 
                if tokenizer.next.valor == "+":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("+", [resultado, Parser.parseTerm(tokenizer)])
                elif tokenizer.next.valor == "-":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("-", [resultado, Parser.parseTerm(tokenizer)])    
                
                elif tokenizer.next.valor == "..":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    
                    resultado = BinOp("..", [resultado, Parser.parseTerm(tokenizer)])
       
        return resultado
    



    @staticmethod
    def parseTerm(tokenizer: Tokenizer):
        resultado = Parser.parseFactor(tokenizer)
        
        while tokenizer.next.valor == "*" or tokenizer.next.valor == "/":
            if tokenizer.next.tipo == "sinal":
                if tokenizer.next.valor == "*":
                    tokenizer.selectNext()
                    
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("*", [resultado, Parser.parseFactor(tokenizer)])
                elif tokenizer.next.valor == "/":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("/", [resultado, Parser.parseFactor(tokenizer)])
            
            else:
                sys.stderr.write("Erro: Sinal invalido4")
                sys.exit(1) 
        
        return resultado

    #def parseFactor(self) for pareteses
    @staticmethod
    def parseFactor(tokenizer: Tokenizer):
        
        #create node
        
       
        if tokenizer.next.tipo == "numero":
            resultado = tokenizer.next.valor
            tokenizer.selectNext()
            return IntVal(resultado)
        elif tokenizer.next.tipo == "string":
            resultado = tokenizer.next.valor
            tokenizer.selectNext()
            return StrVal(resultado)

        elif tokenizer.next.tipo == "abre":
            tokenizer.selectNext()
            resultado = Parser.parseBoolExpression(tokenizer)
            
            if tokenizer.next.tipo != "fecha":
                sys.stderr.write("Erro: Falta fecha parentese")
                sys.exit(1)
            tokenizer.selectNext()
            return resultado
        elif tokenizer.next.tipo == "sinal":
            if tokenizer.next.valor == "+":
                tokenizer.selectNext()
                if tokenizer.next.tipo == "EOF":
                    sys.stderr.write("Erro: Expressao invalida")
                    sys.exit(1)
                return UnOp("+", [Parser.parseFactor(tokenizer)])
            elif tokenizer.next.valor == "-":
                tokenizer.selectNext()
                if tokenizer.next.tipo == "EOF":
                    sys.stderr.write("Erro: Expressao invalida")
                    sys.exit(1)
                # resultado -= Parser.parseFactor(tokenizer)
                return UnOp("-", [Parser.parseFactor(tokenizer)])
            else:
                sys.stderr.write("Erro: Sinal invalido factor")
                sys.exit(1)
        elif tokenizer.next.tipo == "not":
            tokenizer.selectNext()
            if tokenizer.next.tipo == "EOF":
                sys.stderr.write("Erro: Expressao invalida")
                sys.exit(1)
            return UnOp("not", [Parser.parseFactor(tokenizer)])
        elif tokenizer.next.tipo == "identificador":
            resultado = tokenizer.next.valor
            tokenizer.selectNext()  
            if tokenizer.next.tipo == "abre":
                tokenizer.selectNext()
                resultado2 = []
                
                while tokenizer.next.tipo != "fecha":
                    resultado2.append(Parser.parseBoolExpression(tokenizer))
                    if tokenizer.next.tipo != "virgula" and tokenizer.next.tipo != "fecha":
                        sys.stderr.write("Erro: Falta virgula iden")
                        sys.exit(1)
                    if tokenizer.next.tipo == "fecha":
                        break
                    tokenizer.selectNext()

                if tokenizer.next.tipo != "fecha":
                    sys.stderr.write("Erro: Falta fecha")
                    sys.exit(1)
                tokenizer.selectNext()            
                return FuncCall(resultado, resultado2)
            elif tokenizer.next.tipo == "ponto":
                tokenizer.selectNext()
                if tokenizer.next.tipo == "identificador":
                    resultado2 = tokenizer.next.valor
                    tokenizer.selectNext()
                    if tokenizer.next.tipo != "ponto":
                        sys.stderr.write("Erro: Falta ponto")
                        sys.exit(1)
                    tokenizer.selectNext()
                    if tokenizer.next.tipo != "SKILL":
                        sys.stderr.write("Erro: Falta SKILL")
                        sys.exit(1)
                    tokenizer.selectNext()
                    return [Identifier([resultado, resultado2])]
            else:
                return resultado
        elif tokenizer.next.tipo == "TEAM":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "identificador":
                sys.stderr.write("Erro: Falta identificador TEAM")
                sys.exit(1)
            resultado = tokenizer.next.valor
            tokenizer.selectNext()
            if tokenizer.next.tipo != "quebra":
                sys.stderr.write("Erro: Falta quebra TEAM")
                sys.exit(1)
            return Identifier([resultado])
        elif tokenizer.next.tipo == "PLAYER":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "identificador":
                sys.stderr.write("Erro: Falta identificador PLAYER")
                sys.exit(1)
            resultado = tokenizer.next.valor
            tokenizer.selectNext()
            if tokenizer.next.tipo != "ponto":
                sys.stderr.write("Erro: Falta ponto")
                sys.exit(1)
            tokenizer.selectNext()
            if tokenizer.next.tipo != "identificador":
                sys.stderr.write("Erro: Falta identificador PLAYER")
                sys.exit(1)
            resultado2 = tokenizer.next.valor
            tokenizer.selectNext()

            if tokenizer.next.tipo != "quebra":
                sys.stderr.write("Erro: Falta quebra PLAYER")
                sys.exit(1)
            return [Identifier([resultado, resultado2])]
        elif tokenizer.next.tipo == "MATCHTIME":
            resultado = tokenizer.next.valor
            tokenizer.selectNext()

            return Match_TIME_OP(resultado)
        elif tokenizer.next.tipo == "read":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "abre":
                sys.stderr.write("Erro: Falta abre")
                sys.exit(1)
            tokenizer.selectNext()
            if tokenizer.next.tipo != "fecha":
                sys.stderr.write("Erro: Falta fecha read")
                sys.exit(1)
            tokenizer.selectNext()
            return ReadOp(int(input())) 
            
            
        else:
            print(tokenizer.next.tipo)
            sys.stderr.write("Erro: Expressao invalida Factor")
            sys.exit(1)

    @staticmethod
    def parseBoolExpression(tokenizer: Tokenizer):
        resultado = Parser.parseBoolTerm(tokenizer)
        
        while tokenizer.next.tipo == "or":
                if tokenizer.next.tipo == "or":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("or", [resultado, Parser.parseBoolTerm(tokenizer)])       
        return resultado
    
    @staticmethod
    def parseBoolTerm(tokenizer: Tokenizer):
        resultado = Parser.parseRealExpression(tokenizer)
        
        while tokenizer.next.tipo == "and":
            tokenizer.selectNext()
            if tokenizer.next.tipo == "EOF":
                sys.stderr.write("Erro: Expressao invalida")
                sys.exit(1)
            resultado = BinOp("and", [resultado, Parser.parseRealExpression(tokenizer)])       
        return resultado
    
    @staticmethod
    def parseRealExpression(tokenizer: Tokenizer):
        resultado = Parser.parseExpression(tokenizer)
        while tokenizer.next.valor == "<" or tokenizer.next.valor == ">" or tokenizer.next.valor == "==":
            if tokenizer.next.tipo == "sinal":
                if tokenizer.next.valor == "<":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("<", [resultado, Parser.parseExpression(tokenizer)])
                elif tokenizer.next.valor == ">":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp(">", [resultado, Parser.parseExpression(tokenizer)])
                elif tokenizer.next.valor == "==":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "EOF":
                        sys.stderr.write("Erro: Expressao invalida")
                        sys.exit(1)
                    resultado = BinOp("==", [resultado, Parser.parseExpression(tokenizer)])
                else:
                    sys.stderr.write("Erro: Sinal invalido")
                    sys.exit(1)
        return resultado

    @staticmethod
    def parseStatement(tokenizer: Tokenizer):
        if tokenizer.next.tipo == "TEAM":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "identificador":
                sys.stderr.write("Erro: Falta identificador TEAM")
                sys.exit(1)
            resultado = tokenizer.next.valor
            tokenizer.selectNext()
            resultado = VarDec([resultado, None])
            if tokenizer.next.tipo != "quebra":
                sys.stderr.write("Erro: Falta quebra TEAM")
                sys.exit(1)
            return resultado
        if tokenizer.next.tipo == "identificador":
            time = tokenizer.next.valor
            tokenizer.selectNext()

            if tokenizer.next.tipo != "ponto":
                sys.stderr.write("Erro: Falta ponto")
                sys.exit(1)
            tokenizer.selectNext()
            if tokenizer.next.tipo == "AddPlayer":
                tokenizer.selectNext()
                if tokenizer.next.tipo != "abre":
                    sys.stderr.write("Erro: Falta abre AddPlayer")
                    sys.exit(1)
                tokenizer.selectNext()
                if tokenizer.next.tipo != "identificador":
                    sys.stderr.write("Erro: Falta identificador AddPlayer")
                    sys.exit(1)
                resultado = tokenizer.next.valor
                tokenizer.selectNext()
                if tokenizer.next.tipo != "SKILL":
                    sys.stderr.write("Erro: Falta SKILL AddPlayer")
                    sys.exit(1)
                tokenizer.selectNext()
                if tokenizer.next.tipo != "numero":
                    sys.stderr.write("Erro: Falta numero AddPlayer")
                    sys.exit(1)
                resultado2 = tokenizer.next.valor
                tokenizer.selectNext()
                if tokenizer.next.tipo != "fecha":
                    sys.stderr.write("Erro: Falta fecha AddPlayer")
                    sys.exit(1)
                tokenizer.selectNext()
                return ADDPLAYER([time, resultado, resultado2])
            elif tokenizer.next.tipo == "identificador":
                resultado = tokenizer.next.valor
                tokenizer.selectNext()
                if tokenizer.next.tipo == "ponto":
                    tokenizer.selectNext()
                    if tokenizer.next.tipo == "SKILL":
                        tokenizer.selectNext()

                        if tokenizer.next.tipo == "igual":
                            tokenizer.selectNext()
                            resultado2 = Parser.parseBoolExpression(tokenizer)
                            if tokenizer.next.tipo != "quebra":
                                sys.stderr.write("Erro: Falta quebra identificador")
                                sys.exit(1)
                            return Assign([Identifier([time, resultado]), resultado2])
                        else:
                            return Print([Identifier([time, resultado])])   
        elif tokenizer.next.tipo == "PRINT":
            tokenizer.selectNext()
            resultado = Parser.parseBoolExpression(tokenizer)
            if tokenizer.next.tipo != "quebra":
                sys.stderr.write("Erro: Falta quebra PRINT")
                sys.exit(1)
            return Print([resultado])  
        elif tokenizer.next.tipo == "if":
            tokenizer.selectNext()
            resultado = Parser.parseBoolExpression(tokenizer)
            while tokenizer.next.tipo == "quebra":
                tokenizer.selectNext()
            if tokenizer.next.tipo != "chave_abre":
                sys.stderr.write("Erro: Falta abre IF")
                sys.exit(1)
            tokenizer.selectNext()
            while tokenizer.next.tipo == "quebra":
                tokenizer.selectNext()
            resultado2 = []
            while tokenizer.next.tipo != "chave_fecha" and tokenizer.next.tipo != "else":
                resultado2.append(Parser.parseStatement(tokenizer))
                if tokenizer.next.tipo != "quebra" and tokenizer.next.tipo != "chave_fecha" and tokenizer.next.tipo != "else":
                    sys.stderr.write("Erro: Falta quebra IF LOOP")
                    sys.exit(1)
                tokenizer.selectNext()
            if (tokenizer.next.tipo != "chave_fecha" and tokenizer.next.tipo != "else"):
                sys.stderr.write("Erro: Falta end or else")
                sys.exit(1)
            if tokenizer.next.tipo == "chave_fecha":
                tokenizer.selectNext()
                if tokenizer.next.tipo != "quebra":
                    sys.stderr.write("Erro: Falta quebra IF")
                    sys.exit(1)
                tokenizer.selectNext()
                if tokenizer.next.tipo != "else":
                    return IfOp("if", [resultado, resultado2])
            if tokenizer.next.tipo == "else":
                tokenizer.selectNext()
                while tokenizer.next.tipo == "quebra":
                    tokenizer.selectNext()
                
                if tokenizer.next.tipo != "chave_abre":
                    sys.stderr.write("Erro: Falta chave ELSE")
                    sys.exit(1)
                
                tokenizer.selectNext()
                while tokenizer.next.tipo == "quebra":
                    tokenizer.selectNext()
                resultado3 = []
                while tokenizer.next.tipo != "chave_fecha":
                    resultado3.append(Parser.parseStatement(tokenizer))
                    if tokenizer.next.tipo != "quebra" and tokenizer.next.tipo != "chave_fecha":
                        sys.stderr.write("Erro: Falta quebra else end")
                        sys.exit(1)
                    tokenizer.selectNext()
                if tokenizer.next.tipo != "chave_fecha":
                    sys.stderr.write("Erro: Falta chave_fecha")
                    sys.exit(1)
            tokenizer.selectNext()
            return IfOp("if", [resultado, resultado2, resultado3])
        elif tokenizer.next.tipo == "MATCH":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "identificador":
                sys.stderr.write("Erro: Falta identificador MATCH")
                sys.exit(1)
            time1 = tokenizer.next.valor
            tokenizer.selectNext()
            if tokenizer.next.tipo != "VS":
                sys.stderr.write("Erro: Falta VS")
                sys.exit(1)
            tokenizer.selectNext()
            if tokenizer.next.tipo != "identificador":
                sys.stderr.write("Erro: Falta identificador MATCH")
                sys.exit(1)
            time2 = tokenizer.next.valor
            tokenizer.selectNext()
            if tokenizer.next.tipo != "chave_abre":
                sys.stderr.write("Erro: Falta abre MATCH")
                sys.exit(1)
            tokenizer.selectNext()
            resultado2 = []
            while tokenizer.next.tipo != "chave_fecha":
                if tokenizer.next.tipo == "quebra":
                    tokenizer.selectNext()
                    continue

                if tokenizer.next.tipo != "quebra":
                    resultado2.append(Parser.parseStatement(tokenizer))
                elif tokenizer.next.tipo != "quebra" and tokenizer.next.tipo != "chave_fecha":
                    sys.stderr.write("Erro: Falta quebra WHILE LOOP")
                    sys.exit(1)
            if tokenizer.next.tipo != "chave_fecha":
                sys.stderr.write("Erro: Falta chave_fecha")
                sys.exit(1)

            tokenizer.selectNext()
            return WhileOp("while", (resultado2, [time1, time2]))
        elif tokenizer.next.tipo == "MATCHTIME":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "abre":
                sys.stderr.write("Erro: Falta abre MATCHTIME")
                sys.exit(1)
            tokenizer.selectNext()
            retorno = Parser.parseBoolExpression(tokenizer)
            if tokenizer.next.tipo != "fecha":
                sys.stderr.write("Erro: Falta fecha MATCHTIME")
                sys.exit(1)
            tokenizer.selectNext()
            if tokenizer.next.tipo != "quebra":
                sys.stderr.write("Erro: Falta quebra MATCHTIME")
                sys.exit(1)
            return Match_TIME_SET("MATCHTIME", [retorno])
        elif tokenizer.next.tipo == "ENDMATCH":
            tokenizer.selectNext()
            if tokenizer.next.tipo != "quebra":
                sys.stderr.write("Erro: Falta quebra ENDMATCH")
                sys.exit(1)
            return END_MATCH("ENDMATCH")
        else:
            sys.stderr.write("Erro: Comando invalido {}".format(tokenizer.next.tipo))
            sys.exit(1)


    @staticmethod
    def parseBlock(tokenizer: Tokenizer):
        resultado = []
        tokenizer.selectNext()
        while tokenizer.next.tipo != "EOF":
            resultado.append(Parser.parseStatement(tokenizer))
    
            if tokenizer.next.tipo != "quebra" and tokenizer.next.tipo != "EOF":
                sys.stderr.write("Erro: Falta quebra BLOCK")
                sys.exit(1)
            tokenizer.selectNext()
        return Block(1,resultado)

    @staticmethod
    def run(code):
        tokenizer = Tokenizer(code, 0, None)
        resultado = Parser.parseBlock(tokenizer)
        
        # if tokenizer.next.tipo != "EOF":
        #     sys.stderr.write("Erro: Expressao invalida EOF")
        #     sys.exit(1)
        return resultado


class SymbolTable:
    def __init__(self):
        self.table = {}
    
    def set(self, name: str, value: int, type: str = "int"):
        self.table[name] = {}
    
    def get(self, name: str):
        return self.table[name]
    
    def add (self, name: str, value, type: str = "int"):
        self.table[name][value[0]] = value[1]    


class Match_Table:
    def __init__(self):
        self.table = {}
        self.table["MATCHTIME"] = 0
    
    def set(self, name: str, value: int, type: str = "int"):
        self.table[name] = {}
    
    def get(self, name: str):
        return self.table[name]
    
    def add (self, name: str, value, type: str = "int"):
        self.table[name][value[0]] = value[1]    
    
    def set_time(self, value: int):
        self.table["MATCHTIME"] = value



class Node:
    def __init__(self, value: str, children=None):
        self.value = value
        self.children = children if children is not None else []

    @abstractmethod
    def evaluate(self, SymbolTable):
        pass

class BinOp(Node):
    def __init__(self, value: str, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable: SymbolTable):
        if (self.value in ["+", "-", "*", "/", "<", ">", "==", "and", "or", ".."]):
            if self.value == "+":
                if isinstance(self.children[0], list) and isinstance(self.children[1], list):
                    return self.children[0][0].evaluate(SymbolTable) + self.children[1][0].evaluate(SymbolTable)
                elif isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) + self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) + self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) + self.children[1].evaluate(SymbolTable)
            elif self.value == "-":
                if isinstance(self.children[0], list) and isinstance(self.children[1], list):
                    return self.children[0][0].evaluate(SymbolTable) - self.children[1][0].evaluate(SymbolTable)
                elif isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) - self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) - self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) - self.children[1].evaluate(SymbolTable)
            elif self.value == "*":
                if isinstance(self.children[0], list) and isinstance(self.children[1], list):
                    return self.children[0][0].evaluate(SymbolTable) * self.children[1][0].evaluate(SymbolTable)
                elif isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) * self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) * self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) * self.children[1].evaluate(SymbolTable)
            elif self.value == "/":
                if isinstance(self.children[0], list) and isinstance(self.children[1], list):
                    return self.children[0][0].evaluate(SymbolTable) // self.children[1][0].evaluate(SymbolTable)
                elif isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) // self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) // self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) // self.children[1].evaluate(SymbolTable)
            elif self.value == "<":
                if isinstance(self.children[0], list) and isinstance(self.children[1], list):
                    return self.children[0][0].evaluate(SymbolTable) < self.children[1][0].evaluate(SymbolTable)
                elif isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) < self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) < self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) < self.children[1].evaluate(SymbolTable)
            elif self.value == ">":
                if isinstance(self.children[0], list) and isinstance(self.children[1], list):
                    return self.children[0][0].evaluate(SymbolTable) > self.children[1][0].evaluate(SymbolTable)
                elif isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) > self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) > self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) > self.children[1].evaluate(SymbolTable)
            elif self.value == "==":
                if isinstance(self.children[0], list):
                    return self.children[0][0].evaluate(SymbolTable) == self.children[1].evaluate(SymbolTable)
                elif isinstance(self.children[1], list):
                    return self.children[0].evaluate(SymbolTable) == self.children[1][0].evaluate(SymbolTable)
                else:
                    return self.children[0].evaluate(SymbolTable) == self.children[1].evaluate(SymbolTable)
            
            else:
                sys.stderr.write("Erro: Operacao invalida")
                sys.exit(1)
        

class UnOp(Node):
    def __init__(self, value: int, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable: SymbolTable):
        if self.value == "+":
            if self.children[0].evaluate(SymbolTable)[1] == "int":
                return (self.children[0].evaluate(SymbolTable)[0], "int")
            else:
                sys.stderr.write("Erro: Operacao invalida")
                sys.exit(1)
        elif self.value == "-":
            if self.children[0].evaluate(SymbolTable)[1] == "int":
                return (-self.children[0].evaluate(SymbolTable)[0], "int")
            else:
                sys.stderr.write("Erro: Operacao invalida")
                sys.exit(1)
        elif self.value == "not":
            if self.children[0].evaluate(SymbolTable)[1] == "int":
                return (not self.children[0].evaluate(SymbolTable)[0], "int")
            else:
                sys.stderr.write("Erro: Operacao invalida")
                sys.exit(1)
        
class IntVal(Node):
    def __init__(self, value: int):
        super().__init__(value)

    def evaluate(self, SymbolTable: SymbolTable):
        return (self.value)

class StrVal(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, SymbolTable: SymbolTable):
        return (self.value, "string")
    
class NoOp(Node):
    def __init__(self):
        super().__init__(None)

    def evaluate(self, SymbolTable: SymbolTable):
        pass

class Identifier(Node):
    def __init__(self, value: str):
        super().__init__(value)

    def evaluate(self, SymbolTable: SymbolTable):
        primeiro = SymbolTable.get(self.value[0])
        if (len(self.value) == 2):
            return (primeiro[self.value[1]])
        else:
            return (primeiro)

class Assign(Node):
    def __init__(self, children):
        super().__init__( 0, children)

    def evaluate(self, SymbolTable: SymbolTable):
        if self.children[0].value[0] in SymbolTable.table:
            if self.children[0].value[1] in SymbolTable.table[self.children[0].value[0]]:
                #if self.children[1] is a list
                if isinstance(self.children[1], list):
                    SymbolTable.add(self.children[0].value[0], (self.children[0].value[1], self.children[1][0].evaluate(SymbolTable)))

                else:
                    SymbolTable.add(self.children[0].value[0], (self.children[0].value[1], self.children[1].evaluate(SymbolTable)))
            else:
                sys.stderr.write(f"Erro: Variavel {self.children[0].value[1]} nao declarada\n")
                sys.exit(1)
        else:
            sys.stderr.write(f"Erro: Variavel {self.children[0].value} nao declarada\n")
            sys.exit(1)

class ADDPLAYER(Node):
    def __init__(self, children):
        super().__init__( 0, children)

    def evaluate(self, SymbolTable: SymbolTable):
        # print(f"Adicionando ao time {self.children[0]} o jogador {self.children[1]} com skill {self.children[2]}")
        if self.children[0] in SymbolTable.table:
            SymbolTable.add(self.children[0], (self.children[1], self.children[2]))
        else:
            sys.stderr.write(f"Erro: Variavel {self.children[0].value} nao declarada\n")
            sys.exit(1)

class VarDec(Node):
    def __init__(self, children):
        super().__init__(0, children)

    def evaluate(self, SymbolTable: SymbolTable):
        if self.children[0] in SymbolTable.table:
            sys.stderr.write(f"Erro: Variavel {self.children[0].value} ja declarada\n")
            sys.exit(1)
        SymbolTable.set(self.children[0], 0)


class Print(Node):
    def __init__(self, children):
        super().__init__(0, children)

    def evaluate(self, SymbolTable: SymbolTable): 
        if isinstance(self.children[0], list):
            resultado = str(self.children[0][0].value[1]) +  " SKILL " + str(self.children[0][0].evaluate(SymbolTable))
        else:  
            resultado = (self.children[0].evaluate(SymbolTable))
        print(resultado)

class Block(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable: SymbolTable):
        for child in self.children:
            if isinstance(child, ReturnOp):
                return child.evaluate(SymbolTable)[0]
            else:
                child.evaluate(SymbolTable)
            #if is a return, return the value
            
            

class IfOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable: SymbolTable, MatchTable: Match_Table):
        if self.children[0].evaluate(SymbolTable):
            for child in self.children[1]:
                if isinstance(child, Match_TIME_SET):
                    child.evaluate(MatchTable)
                elif isinstance(child, END_MATCH):
                    return "END_MATCH"
                else:
                    child.evaluate(SymbolTable)
        elif len(self.children) > 2:
            for child in self.children[2]:
                if isinstance(child, Match_TIME_SET):
                    child.evaluate(MatchTable)
                elif isinstance(child, END_MATCH):
                    return "END_MATCH"
                else:
                    child.evaluate(SymbolTable)
            
        else:
            return None

class Match_TIME_OP(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, Match_Table: Match_Table):
        return Match_Table.get("MATCHTIME")
    
class Match_TIME_SET(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
        
    def evaluate(self, Matchtable: Match_Table):
        Matchtable.set_time(self.children[0].evaluate(Matchtable))
        return Matchtable.get("MATCHTIME")
    
class END_MATCH(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, SymbolTable: SymbolTable):
        return None

class WhileOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable: SymbolTable):
        i = 0
        match_table = Match_Table()
        print(f"Match entre {self.children[1][0]} e {self.children[1][1]}")

        match_table.set(self.children[1][0], 0, "int")
        match_table.set(self.children[1][1], 0, "int")
        
        while match_table.get("MATCHTIME") < 90:
            for child in self.children[0]:
                if isinstance(child, Match_TIME_SET):
                    child.evaluate(match_table)
                elif isinstance(child, END_MATCH):
                    return None
                else:
                    if isinstance(child, IfOp):
                        retorno = child.evaluate(SymbolTable, match_table)
                        if retorno == "END_MATCH":
                            return None
                    else:
                        child.evaluate(SymbolTable)
                    
            # print(self.children[0].evaluate(SymbolTable))
            # i += 1
            # if i> 5:
            #     sys.stderr.write("Erro: Loop infinito")
            #     sys.exit(1)
        def get_match_table(self):
            return match_table

class ReadOp(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, SymbolTable: SymbolTable):
        return (self.value, "int")

class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable: SymbolTable):
        if self.children[0] in FuncTable.func_table:
            sys.stderr.write(f"Erro: Funcao {self.children[0]} ja declarada\n")
            sys.exit(1)
        
        FuncTable.add_func(self.children[0], self.children[1], self.children[2])
        


class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def evaluate(self, SymbolTable_2: SymbolTable):
        func = FuncTable.get_func(self.value.value)[0]
        args_numb = FuncTable.get_func(self.value.value)[1]
        args = self.children
        for i in range(len(args)):
            args[i] = args[i].evaluate(SymbolTable_2)[0]

        if len(args) != len(args_numb):
            sys.stderr.write("Erro: Argumentos invalidos")
            sys.exit(1)      
        new_table = SymbolTable()
        new_table.set(self.value.value, 0, "int")
        for i in range(len(args)):
            new_table.set(args_numb[i], args[i], "int")
        saida = func.evaluate(new_table)
        return (saida, "int")

class ReturnOp(Node):
    def __init__(self, value):
        super().__init__(value)

    def evaluate(self, SymbolTable: SymbolTable):
        #return the value of the expression
        return self.value.evaluate(SymbolTable)


class FuncTable():
    func_table = {}

    @staticmethod
    def add_func(name: str, func, args):
        FuncTable.func_table[name] = (func, args)
    

    @staticmethod
    def get_func(name: str):
        return FuncTable.func_table[name]

        

class PrePro:
    @staticmethod
    def filter(s: str):
        linhas = s.split("\n")
        for i in range(len(linhas)):
            index = linhas[i].find('--')
            if index != -1:
                linhas[i] = linhas[i][:index]

        final = ""
        for i in range(len(linhas)):
            if linhas[i] != "":
                final += linhas[i].strip() + "\n"
            else:
                pass
        return final

    

if __name__ == "__main__":
    parser = Parser(None)
    nome = sys.argv[1]

    symboltable = SymbolTable()

    if nome[-4:] != ".fut":
        sys.stderr.write("Erro: Arquivo invalido")
        sys.exit(1)
    
    file = open(nome, "r")
    argumeto = file.read()
    file.close()
    argumeto = PrePro.filter(argumeto)
    resultado = parser.run(argumeto)
    resultado.evaluate(symboltable)
    #print all symbol table
    print(symboltable.table)
    




            

#!/usr/bin/python3

#DEFINES

DIGITS      = '0123456789'
OPERATORS   = '+-*/%='
SPACE       = ' '
NEWLINE     = '\n'
PERIOD      = '.'
STRING      = '\'\"'

T_INT       = 'INT'     #Pure numeric whole number.
T_FLOAT     = 'FLOAT'   #Pure numeric value which contains a decimal.
T_CHAR      = 'CHAR'    #A single character flanked by " ' ".
T_STR       = 'STR'     #An array of characters flanked by " ' ".
T_BOOL      = 'BOOL'    #The words "True" or "False" not flanked by " ' ". Specific logic for 1s and 0s in various instances will need to be programmed in later.
T_NONE      = 'NONE'    #No value.

T_ADD       = 'ADD'     #Addition, denoted by +
T_SUB       = 'SUB'     #Subtraction, denoted by -
T_MUL       = 'MUL'     #Multiplication, denoted by *
T_DIV       = 'DIV'     #Division, denoted by /
T_MOD       = 'MOD'     #Modulus, denoted by %
T_EQL       = 'EQL'     #Equality operator, denoted by ==
T_ASN       = 'ASN'     #Assignment operator, denoted by =

T_ITER_ADD  = 'ITR_ADD' #Iterative addition operator, denoted by ++
T_ITER_SUB  = 'ITR_SUB' #Iterative subtraction operator, denoted by --


class Token:
    def __init__(self, content, type_):
        self.content = content
        self.type_ = type_
            
    def __repr__(self):
        return repr(self.content + self.type)


class Tokenizer:
    def __init__(self, input_):
        self.input = str(input_)
        self.tokens = []
        self.buffer_ = []
        
        for character in input_:
            if character in STRING:
                string_init = character
                self.buffer.append(character.pop())
                self.buffer.append(input_[:input_.index(string_init)])
                input
            else:
                return 0
                
    def _tokenize(self):
        content = ''.join(self.buffer_)

        if content[0] and content[-1] in STRING:
            return Token(str(content), T_STR)
        elif content in DIGITS and PERIOD:
            return Token(float(content), T_FLOAT)
        elif content in DIGITS:
            return Token(int(content), T_INT)
        else:
            print("ERROR, invalid character being tokenized.")
    

        self.buffer_.clear()




















import ply.lex as lex
import ply.yacc as yacc

reserved = {
    'True': 'TRUE',
    'False': 'FALSE',
    'print': 'PRINT',
    'input': 'INPUT',
}
tokens = ['PCOMA','PDERECHO','PIZQUIERDO','COMILLAS','VARIABLE','ENTERO','DECIMAL','SUMA',
          'RESTA','DIVISION','MULTIPLICACION','IGUAL','POTENCIA','MODULO'] + list(reserved.values())
t_PCOMA = r'\,'
t_PIZQUIERDO= r'\('
t_COMILLAS = r'\"'
t_PDERECHO= r'\)'
t_SUMA= r'\+'
t_RESTA= r'\-'
t_DIVISION= r'\/'
t_MULTIPLICACION= r'\*'
t_IGUAL= r'\='
t_POTENCIA= r'\^'
t_MODULO= r'\%'

t_ignore =' \t \n '

def t_VARIABLE(t):
    r'[a-zA-z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input('"')

precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVISION'),
    ('left','MODULO','POTENCIA'))

def p_sentencia(p):
    '''
    sentencia : presentar
              | asignacion
    '''

def p_presentar(p):
    '''
    presentar : PRINT PIZQUIERDO VARIABLE PDERECHO
              | PRINT PIZQUIERDO  cadena PDERECHO
              | PRINT PIZQUIERDO  pvariedad PDERECHO
    '''

def p_pvariedad(p):
    '''
    pvariedad : cadena PCOMA pvariedad
              | VARIABLE PCOMA pvariedad
              | VARIABLE
              | cadena
    '''
def p_asginacion(p):
    '''
    asignacion : VARIABLE IGUAL operacion
               | VARIABLE IGUAL booleano
               | VARIABLE IGUAL ingresar

    '''
def p_ingresar(p):
    '''
    ingresar  : INPUT PIZQUIERDO cadena PDERECHO
    '''


def p_frase(p):
    '''
    frase : VARIABLE
           | ENTERO
           | VARIABLE frase
           | ENTERO frase
    '''

def p_cadena(p):
    '''
    cadena : COMILLAS frase COMILLAS
    '''
    p[0] = p[1]


def p_operacion(p):
    '''
    operacion : expresion SUMA expresion
              | expresion RESTA expresion
              | expresion MULTIPLICACION expresion
              | expresion DIVISION expresion
              | expresion MODULO expresion
              | expresion POTENCIA expresion
    '''

    operaciones = ['-','*','/','&','^']
    if p[2]== '+':
        p[0] = p[1]+p[3]
    elif p[2] == '-':
        p[0] = p[1]-p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '%':
        p[0] = p[1] % p[3]
    elif p[2] == '^':
        p[0] = pow(p[1],p[3])


def p_booleano(p):
    '''
    booleano : TRUE
             | FALSE
    '''
    p[0] = p[1]

def p_expresion(p):
    '''
    expresion : ENTERO
              | DECIMAL
    '''
    p[0]=p[1]

def p_error(p):
    print("Syntax error in input!")


parser= yacc.yacc()

archivo = open("script.txt")
script = archivo.readlines();
for linea in script:
    try:
        s = linea
    except EOFError:
        break
    print(linea)
    parser.parse(s)

archivo.close()

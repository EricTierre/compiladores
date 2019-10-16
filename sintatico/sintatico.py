# Yacc example
 
import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
from lexico import tokens


    
def p_expression(p):
    '''expression : expression PLUS term 
                  | expression  MINUS term'''

    print('expression', 'expression', p[2], 'term')

def p_expression_term(p):
    'expression : term'
    print('expression', 'term')

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
    print('term', 'term', p[3], 'factor')

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
    print('term', 'term', p[3],'factor')

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    print('term', 'factor')

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
    print('factor', p[1])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
    print(p[0], p[1], p[3], p[4])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   #print(result, parser.parse(s))
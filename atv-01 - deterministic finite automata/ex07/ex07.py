# 7. (03 da lista) L = { w ∈ {a, b} | w contém uma quantidade ímpar de 'a' e múltiplo de 3 de 'b' }*

def ex07(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    estado_atual = q0

    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)]
        else:
            return False

    return estado_atual in F

# Estados renomeados: q0 a q5
Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
Sigma = {'a', 'b'}

delta = {
    # Transições com 'a'
    ('q0', 'a'): 'q3',
    ('q1', 'a'): 'q4',
    ('q2', 'a'): 'q5',
    ('q3', 'a'): 'q0',
    ('q4', 'a'): 'q1',
    ('q5', 'a'): 'q2',

    # Transições com 'b'
    ('q0', 'b'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'b'): 'q0',
    ('q3', 'b'): 'q4',
    ('q4', 'b'): 'q5',
    ('q5', 'b'): 'q3',
}

q0 = 'q0'
F = {'q3'}  

M = (Q, Sigma, delta, q0, F)

# Testes
print(ex07(M, ""))            # False
print(ex07(M, "a"))           # True
print(ex07(M, "aa"))          # False
print(ex07(M, "abbb"))        # True
print(ex07(M, "ab"))          # False
print(ex07(M, "aaaabbbbbb"))  # False
print(ex07(M, "aaabbbbbb"))   # True 

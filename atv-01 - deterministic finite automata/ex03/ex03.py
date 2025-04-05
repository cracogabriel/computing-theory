# 3. L6​={w ∈ {a,b}∗ ∣ (∣w∣ a​ + ∣w∣ b) mod2 = 0}
# A quantidade de a's + quantidade de b's deve ser par.

def ex03(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    estado_atual = q0

    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)]
        else:
            return False

    return estado_atual in F

# Definindo o AFD M6
Q = {'q0', 'q1', 'q2', 'q3'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q0',
    ('q3', 'a'): 'q2',
    ('q3', 'b'): 'q1',
}
q0 = 'q0'
F = {'q0', 'q3'}  # Estado de comprimento par

M6 = (Q, Sigma, delta, q0, F)

# Testes
print(ex03(M6, ''))         # True (0 letras = par)
print(ex03(M6, 'a'))        # False (1 letra = ímpar)
print(ex03(M6, 'ab'))       # True (2 letras)
print(ex03(M6, 'aba'))      # False (3 letras)
print(ex03(M6, 'abab'))     # True (4 letras)

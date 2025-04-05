# 2. AFD 𝑀5 que reconheça 𝐿5 = {𝑥 ∈ {𝑎, 𝑏}∗ ∣ |𝑥| mod 3 = 0}

def ex02(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    estado_atual = q0

    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)]
        else:
            return False

    return estado_atual in F

# Definindo o AFD M5
Q = {'q0', 'q1', 'q2'}
Sigma = {'a', 'b'}
delta = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q2',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q0',
    ('q2', 'b'): 'q0',
}
q0 = 'q0'
F = {'q0'}  # Aceita palavras cujo tamanho é múltiplo de 3

M5 = (Q, Sigma, delta, q0, F)

# Testes
print(ex02(M5, ''))          # True (0 letras)
print(ex02(M5, 'ab'))        # False (2 letras)
print(ex02(M5, 'aba'))       # True (3 letras)
print(ex02(M5, 'ababab'))    # True (6 letras)
print(ex02(M5, 'aabbaab'))   # False (7 letras)

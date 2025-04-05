# 4. 𝐿7 = {𝑎^𝑚𝑏^𝑛 ∣ 𝑚, 𝑛 ≥ 0 ∧ (𝑚 + 𝑛) mod 2 = 0}

def ex04(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    estado_atual = q0

    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)]
        else:
            return False

    return estado_atual in F

# Definindo o AFD M7
Q = {'q0', 'q1', 'q2', 'q3', 'q4'} # q4 = error
Sigma = {'a', 'b'}
delta = {
    # Leitura de a's
    ('q0', 'a'): 'q1',
    ('q1', 'a'): 'q0',

    # Começando os b's
    ('q0', 'b'): 'q2',
    ('q1', 'b'): 'q3',

    # Continua lendo b's
    ('q2', 'b'): 'q3',
    ('q3', 'b'): 'q2',

    # Se ler 'a' após b, vai pro estado de erro
    ('q2', 'a'): 'q4',
    ('q3', 'a'): 'q4',
    ('q4', 'a'): 'q4',
    ('q4', 'b'): 'q4',
}
q0 = 'q0'
F = {'q0', 'q3'}  # Aceita se (m + n) é par

M7 = (Q, Sigma, delta, q0, F)

# Testes
print(ex04(M7, ''))          # True (m=0, n=0 → 0 par)
print(ex04(M7, 'a'))         # False (1 letra)
print(ex04(M7, 'aa'))        # True (2 letras)
print(ex04(M7, 'aab'))       # False (3 letras)
print(ex04(M7, 'aabb'))      # True (4 letras)
print(ex04(M7, 'abab'))      # False ('a' depois do 'b')
print(ex04(M7, 'aaabbb'))    # True (6 letras)
print(ex04(M7, 'aaabbbab'))  # False ('a' depois do 'b')

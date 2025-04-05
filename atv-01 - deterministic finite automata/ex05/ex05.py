# 5. AFD 𝑀8 que reconheça 𝐿8 = {𝑥 ∈ Σ∗ ∣ 𝑥 mod 2 = 0}

def ex05(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    estado_atual = q0

    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)]
        else:
            return False

    return estado_atual in F

Q = {'q0', 'q1', 'q2'}
Sigma = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

delta = {}

# transições de q0
for d in Sigma:
    if d in {'0', '2', '4', '6', '8'}:
        delta[('q0', d)] = 'q1'
    else:
        delta[('q0', d)] = 'q2'

# transições de q1
for d in Sigma:
    if d in {'0', '2', '4', '6', '8'}:
        delta[('q1', d)] = 'q1'
    else:
        delta[('q1', d)] = 'q2'

# transições de q2
for d in Sigma:
    if d in {'0', '2', '4', '6', '8'}:
        delta[('q2', d)] = 'q1'
    else:
        delta[('q2', d)] = 'q2'

q0 = 'q0'
F = {'q1'}  

M8 = (Q, Sigma, delta, q0, F)

# Testes
print(ex05(M8, ''))        # False (estado inicial q0, não final)
print(ex05(M8, '1234'))    # True (termina com 4)
print(ex05(M8, '135'))     # False (termina com 5)
print(ex05(M8, '2468'))    # True (termina com 8)
print(ex05(M8, '999'))     # False (termina com 9)
print(ex05(M8, '9992'))    # True (termina com 2)

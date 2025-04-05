# 6. AFD 𝑀9 que reconheça 𝐿9 = {𝑥 ∈ Σ∗ ∣ 𝑥 mod 5 = 0}

def ex06(M, cadeia):
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
    if d in {'0', '5'}:
        delta[('q0', d)] = 'q1'  # vai para o estado de aceitação
    else:
        delta[('q0', d)] = 'q2'  # vai para o de rejeição

# transições de q1 
for d in Sigma:
    if d in {'0', '5'}:
        delta[('q1', d)] = 'q1'  # permanece no final
    else:
        delta[('q1', d)] = 'q2'  # vai para rejeição

# transições de q2 
for d in Sigma:
    if d in {'0', '5'}:
        delta[('q2', d)] = 'q1'  # volta para final se termina em 0 ou 5
    else:
        delta[('q2', d)] = 'q2'  # permanece na rejeição

q0 = 'q0'
F = {'q1'}

M9 = (Q, Sigma, delta, q0, F)

# Testes
print(ex06(M9, ''))         # False (estado inicial q0, não final)
print(ex06(M9, '10'))       # True (termina com 0)
print(ex06(M9, '1235'))     # True (termina com 5)
print(ex06(M9, '4440'))     # True (termina com 0)
print(ex06(M9, '9871'))     # False (termina com 1)

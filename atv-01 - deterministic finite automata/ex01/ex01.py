# 1. AFD 𝑀4 que reconheça 𝐿4 = {𝑏𝑎^n * 𝑏𝑎 ∣ 𝑛 ≥ 0}

def ex01(M, cadeia):
    (Q, Sigma, delta, q0, F) = M
    estado_atual = q0

    for simbolo in cadeia:
        if (estado_atual, simbolo) in delta:
            estado_atual = delta[(estado_atual, simbolo)] # (De onde vou, valor): retorna para onde vou
        else:
            return False

    return estado_atual in F

# Definindo o AFD M4
Q = {'q0', 'q1', 'q2', 'q3', 'q4'}  # Conjuntos de estados
Sigma = {'a', 'b'}                 # Alfabeto
delta = {
    ('q0', 'b'): 'q1',
    ('q1', 'a'): 'q1',
    ('q1', 'b'): 'q2',
    ('q2', 'a'): 'q3',
}
q0 = 'q0'                          # Estado inicial
F = {'q3'}                         # Estados finais

M4 = (Q, Sigma, delta, q0, F)

# Cadeias de exemplo
cadeia_valida = 'baaaaba'
cadeia_invalida = 'baaaa'

# Testes
print("cadeia_valida:",cadeia_valida, ex01(M4, cadeia_valida))    # True
print("cadeia_invalida:",cadeia_invalida, ex01(M4, cadeia_invalida))  # False

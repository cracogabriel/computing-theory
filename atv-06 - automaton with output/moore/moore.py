from automata.fa.dfa import DFA

moore_dfa = DFA(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q2'},
        'q3': {'0': 'q0', '1': 'q4'},
        'q4': {'0': 'q3', '1': 'q5'},
        'q5': {'0': 'q3', '1': 'q2'}
    },
    initial_state='q0',
    final_states={'q5'}
)

outputs = {
    'q0': '0',
    'q1': '0',
    'q2': '0',
    'q3': '0',
    'q4': '0',
    'q5': '1'
}

def simulate_moore(input_sequence):
    current_state = moore_dfa.initial_state
    for symbol in input_sequence:
        print(f"Estado: {current_state}, Entrada: {symbol}, Saída: {outputs[current_state]}")
        current_state = moore_dfa.transitions[current_state][symbol]
    print(f"Estado final: {current_state}, Saída final: {outputs[current_state]}")

simulate_moore(['0', '0', '0', '1', '1', '0', '0', '1', '0'])

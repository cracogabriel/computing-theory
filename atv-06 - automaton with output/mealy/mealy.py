class MealyMachine:
    def __init__(self):
        self.current_state = 'q0'
        self.transitions = {
            ('q0', 'a'): ('q0', '1'),
            ('q0', 'b'): ('q1', 'ε'),
            ('q1', 'b'): ('q1', 'ε'),
            ('q1', 'c'): ('q2', '2'),
            ('q2', 'c'): ('q2', '2'),
            ('q2', 'a'): ('q0', '1'),
        }

    def process_input(self, input_symbol):
        key = (self.current_state, input_symbol)
        if key not in self.transitions:
            raise ValueError(f"Transição inválida: estado {self.current_state}, símbolo {input_symbol}")
        
        self.current_state, output = self.transitions[key]
        return output

machine = MealyMachine()
input_sequence = ['a', 'b', 'b', 'c', 'c', 'a', 'b']  

print("Simulação da Máquina de Mealy:")
for symbol in input_sequence:
    output = machine.process_input(symbol)
    print(f"Estado: {machine.current_state}, Entrada: {symbol}, Saída: {output}")

import numpy as np
from qgate import QGate

class QSimulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1

    def apply_gate(self, gate):
        if isinstance(gate, QGate):
            self.state = gate.apply(self.state)
        else:
            raise TypeError("Unsupported gate type")

    def measure(self):
        probabilities = np.abs(self.state)**2
        outcome = np.random.choice(range(2**self.num_qubits), p=probabilities)
        self.state = np.zeros(2**self.num_qubits, dtype=complex)
        self.state[outcome] = 1
        return outcome

    def reset(self):
        self.state = np.zeros(2**self.num_qubits, dtype=complex)
        self.state[0] = 1

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return repr(self.state)

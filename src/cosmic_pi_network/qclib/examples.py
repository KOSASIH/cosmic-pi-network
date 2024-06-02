from qgate import QGate
from qsimulator import QSimulator
from qutils import random_unitary_matrix, random_quantum_state, fidelity
from circuit import Circuit

def run_example():
    num_qubits = 3
    circuit = Circuit(num_qubits)
    circuit.add_gate(QGate.hadamard(0))
    circuit.add_gate(QGate.pauli_x(1))
    circuit.add_gate(QGate.cnot(0, 2))
    circuit.add_gate(QGate.pauli_z(2))
    circuit.add_gate(QGate.toffoli(0, 1, 2))
    circuit.add_gate(QGate.fredkin(0, 1, 2))

    states = circuit.run(1000)
    state_freqs = np.bincount(states.astype(int), minlength=2**num_qubits)
    state_probs = state_freqs / np.sum(state_freqs)

    for i, prob in enumerate(state_probs):
        if prob > 0.01:
            print(f"State {i}: {prob:.4f}")

    circuit.reset()
    circuit.add_gate(QGate.hadamard(0))
    circuit.add_gate(QGate.pauli_x(1))
    circuit.add_gate(QGate.pauli_y(2))
    circuit.add_gate(QGate.cnot(0, 1))
    circuit.add_gate(QGate.pauli_z(1))
    circuit.add_gate(QGate.toffoli(0, 1, 2))
    circuit.add_gate(QGate.fredkin(0, 1, 2))

    state = random_quantum_state(num_qubits)
    final_state = circuit.simulate_with_state(state)
    print(f"Final state: {final_state}")
    print(f"Fidelity: {fidelity(state, final_state)}")

if __name__ == "__main__":
    run_example()

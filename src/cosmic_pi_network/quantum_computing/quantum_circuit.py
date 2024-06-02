import cirq

class QuantumCircuit:
    def __init__(self):
        pass

    def create_qubit(self, num_qubits):
        qubits = [cirq.LineQubit(i) for i in range(num_qubits)]
        return qubits

    def create_circuit(self, qubits, gates):
        circuit = cirq.Circuit()
        for gate in gates:
            circuit.append(gate.on(*qubits))
        return circuit

    def simulate_circuit(self, circuit):
        simulator = cirq.Simulator()
        result = simulator.run(circuit)
        return result

# Example usage
quantum_circuit = QuantumCircuit()
qubits = quantum_circuit.create_qubit(2)
gates = [cirq.H(qubits[0]), cirq.CNOT(qubits[0], qubits[1])]
circuit = quantum_circuit.create_circuit(qubits, gates)
result = quantum_circuit.simulate_circuit(circuit)
print("Result:", result)

import numpy as np
from qiskit import QuantumCircuit, execute, Aer

class QuantumSimulation:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.backend = Aer.get_backend('qasm_simulator')

    def create_quantum_circuit(self):
        qc = QuantumCircuit(self.num_qubits)
        qc.h(range(self.num_qubits))
        qc.measure_all()
        return qc

    def run_quantum_simulation(self, qc):
        job = execute(qc, self.backend, shots=1024)
        result = job.result()
        counts = result.get_counts(qc)
        return counts

    def simulate_quantum_system(self, hamiltonian, time_step, num_steps):
        qc = self.create_quantum_circuit()
        for i in range(num_steps):
            qc.evolve(hamiltonian, time_step)
            qc.measure_all()
            result = self.run_quantum_simulation(qc)
            print("Time step:", i, "Result:", result)

# Example usage
simulation = QuantumSimulation(4)
hamiltonian = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
time_step = 0.1
num_steps = 10
simulation.simulate_quantum_system(hamiltonian, time_step, num_steps)

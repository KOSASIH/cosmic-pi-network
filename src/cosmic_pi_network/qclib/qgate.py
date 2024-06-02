import numpy as np

class QGate:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.matrix = np.eye(2**num_qubits, dtype=complex)

    def __mul__(self, other):
        if isinstance(other, QGate):
            return QGate(self.num_qubits, np.dot(self.matrix, other.matrix))
        elif isinstance(other, np.ndarray):
            return np.dot(self.matrix, other)
        else:
            raise TypeError("Unsupported operand type for *: '{}' and '{}'".format(type(self).__name__, type(other).__name__))

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return repr(self.matrix)

    @staticmethod
    def pauli_x():
        return QGate(1, np.array([[0, 1], [1, 0]]))

    @staticmethod
    def pauli_y():
        return QGate(1, np.array([[0, -1j], [1j, 0]]))

    @staticmethod
    def pauli_z():
        return QGate(1, np.array([[1, 0], [0, -1]]))

    @staticmethod
    def hadamard():
        return QGate(1, 1/np.sqrt(2) * np.array([[1, 1], [1, -1]]))

    @staticmethod
    def cnot(control, target):
        matrix = np.eye(2**2, dtype=complex)
        matrix[2, 2] = 0
        matrix[2, 3] = 1
        matrix[3, 2] = 1
        matrix[3, 3] = 0
        return QGate(2, matrix)

    @staticmethod
    def toffoli(control1, control2, target):
        matrix = np.eye(2**3, dtype=complex)
        matrix[6, 6] = 0
        matrix[6, 7] = 1
        matrix[7, 6] = 1
        matrix[7, 7] = 0
        return QGate(3, matrix)

    @staticmethod
    def fredkin(control, target1, target2):
        matrix = np.eye(2**3, dtype=complex)
        matrix[4, 4] = 0
        matrix[4, 5] = 1
        matrix[5, 4] = 1
        matrix[5, 5] = 0
        matrix[6, 6] = 0
        matrix[6, 7] = 1
        matrix[7, 6] = 1
        matrix[7, 7] = 0
        return QGate(3, matrix)

    def apply(self, state):
        return np.dot(self.matrix, state)

    def dagger(self):
        return QGate(self.num_qubits, np.conj(self.matrix).T)

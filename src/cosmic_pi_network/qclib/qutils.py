import numpy as np

def random_unitary_matrix(n):
    matrix = np.random.rand(n, n) + 1j * np.random.rand(n, n)
    q, r = np.linalg.qr(matrix)
    return q

def random_quantum_state(n):
    state = np.random.rand(n) + 1j * np.random.rand(n)
    state /= np.linalg.norm(state)
    return state

def fidelity(state1, state2):
    return np.abs(np.dot(state1.conj().T, state2))**2

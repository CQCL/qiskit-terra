"""
Symbolic Rz gate (tket)
"""
from qiskit import Gate
from qiskit import InstructionSet
from qiskit import QuantumCircuit
from qiskit import QuantumRegister
from qiskit.extensions.standard import header


class SymRzGate(Gate):
    """Symbolic Rz gate."""

    def __init__(self, qubit, desc, circ=None):
        """Create new symbolic Rz gate."""
        self.desc = desc
        super().__init__("symrz", [], [qubit], circ)

    def inverse(self):
        """Invert this gate."""
        self.desc = self.desc + ";-"
        return self

    def reapply(self, circ):
        """Reapply this gate to corresponding qubits in circ."""
        self._modifiers(circ.symrz(self.qargs[0], self.desc))


def symrz(self, q, desc):
    """Apply symbolic Rz to q."""
    if isinstance(q, QuantumRegister):
        instructions = InstructionSet()
        for j in range(q.size):
            instructions.add(self.symrz((q, j), desc))
        return instructions

    self._check_qubit(q)
    return self._attach(SymRzGate(q, desc, self))


QuantumCircuit.symrz = symrz

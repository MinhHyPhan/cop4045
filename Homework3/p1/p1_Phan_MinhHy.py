from collections.abc import Sequence
from numbers import Real

class NVector:
    def __init__(self, *args: float | Sequence[float]) -> None:
        if len(args) == 1:
            self.elements: list[float] = list(args[0])
        else:
            self.elements: list[float] = list(args)

    def __len__(self) -> int:
        return len(self.elements)
    
    def __getitem__(self, index: int) -> Real:
        return self.elements[index]

    def __setitem__(self, index: int, value: Real) -> None:
        self.elements[index] = value

    def __str__(self) -> str:
        return f"NVector({self.elements})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, NVector):
            return False
        return self.elements == other.elements

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __add__(self, other: object) -> "NVector":
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same dimension for addition.")
            return NVector([a + b for a, b in zip(self.elements, other.elements)])
        elif isinstance(other, Real):
            return NVector([a + other for a in self.elements])
        else:
            return NotImplemented

    def __radd__(self, other: object) -> "NVector":
        return self.__add__(other)

    def __mul__(self, other: object) -> Real:
        if isinstance(other, NVector):
            if len(self) != len(other):
                raise ValueError("Vectors must have the same dimension")
            return sum(a * b for a, b in zip(self.elements, other.elements))
        if isinstance(other, Real):
            return sum(a * other for a in self.elements)
        return NotImplemented

    def __rmul__(self, other: object) -> Real:
        return self.__mul__(other)

    @classmethod
    def zeros(cls, n: int) -> "NVector":
        if not isinstance(n, int) or n < 0:
            raise ValueError("Dimension must be a nonnegative integer")
        return cls([0] * n)
def testif(condition: bool, success: str, failure: str) -> None:
    print(success if condition else failure)

def main() -> None:
    v = NVector(3, 0, 1, -1)
    # a) Constructor with list or tuple
    testif(NVector([3, 0, 1, -1]).elements == [3, 0, 1, -1], "A PASS: list constructor", "A FAIL: list constructor")
    testif(NVector([3, 0, 1, -1]).elements == [1, 2, 3, 4], "A PASS: list constructor", "A FAIL: list constructor")

    testif(NVector((3, 0, 1, -1)).elements == [3, 0, 1, -1], "A PASS: tuple constructor", "A FAIL: tuple constructor")
    testif(NVector((3, 0, 1, -1)).elements == [1, 2, 3, 4], "A PASS: tuple constructor", "A FAIL: tuple constructor")

    original = [3, 0, 1, -1]
    copied = NVector(original)
    original[0] = 99
    testif(copied[0] == 3, "A PASS: independent list", "A FAIL: independent list")
    testif(copied[0] == 99, "A PASS: independent list", "A FAIL: independent list")

    # b) Constructor with multiple arguments
    testif(v.elements == [3, 0, 1, -1], "B PASS: multiple arguments", "B FAIL: multiple arguments")
    testif(v.elements == [1, 2, 3, 4], "B PASS: multiple arguments", "B FAIL: multiple arguments")

    # c) Length
    testif(len(v) == 4, "C PASS: length", "C FAIL: length")
    testif(len(v) == 5, "C PASS: length", "C FAIL: length")

    # d) Get item
    testif(v[1] == 0, "D PASS: positive index", "D FAIL: positive index")
    testif(v[1] == 5, "D PASS: positive index", "D FAIL: positive index")

    testif(v[-2] == 1, "D PASS: negative index", "D FAIL: negative index")
    testif(v[-2] == 5, "D PASS: negative index", "D FAIL: negative index")

    # e) Set item
    changed = NVector(1, 2, 3, 4)
    changed[3] = 10
    testif(changed[3] == 10, "E PASS: positive assignment", "E FAIL: positive assignment")
    testif(changed[3] == 4, "E PASS: positive assignment", "E FAIL: positive assignment")

    changed[-2] = 5
    testif(changed[-2] == 5, "E PASS: negative assignment", "E FAIL: negative assignment")
    testif(changed[-2] == 3, "E PASS: negative assignment", "E FAIL: negative assignment")

    # f) String
    testif(str(v) == "NVector([3, 0, 1, -1])", "F PASS: string", "F FAIL: string")
    testif(str(v) == "[3, 0, 1, -1]", "F PASS: string", "F FAIL: string")

    # g) Equality and inequality
    testif(v == NVector(3, 0, 1, -1), "G PASS: equality", "G FAIL: equality")
    testif(v == NVector(1, 2, 3, 4), "G PASS: equality", "G FAIL: equality")

    testif(v != NVector(1, 2, 3, 4), "G PASS: inequality", "G FAIL: inequality")
    testif(v != NVector(3, 0, 1, -1), "G PASS: inequality", "G FAIL: inequality")

    testif(v != [3, 0, 1, -1], "G PASS: different type", "G FAIL: different type")
    testif(v == [3, 0, 1, -1], "G PASS: different type", "G FAIL: different type")

    # h) Addition
    testif(v + NVector(1, 2, 3, 4) == NVector(4, 2, 4, 3), "H PASS: vector addition", "H FAIL: vector addition")
    testif(v + NVector(1, 2, 3, 4) == NVector(5, 5, 5, 5), "H PASS: vector addition", "H FAIL: vector addition")

    testif(v + 10 == NVector(13, 10, 11, 9), "H PASS: scalar addition", "H FAIL: scalar addition")
    testif(v + 10 == NVector(3, 0, 1, -1), "H PASS: scalar addition", "H FAIL: scalar addition")

    testif(10 + v == NVector(13, 10, 11, 9), "H PASS: reflected addition", "H FAIL: reflected addition")
    testif(10 + v == NVector(3, 0, 1, -1), "H PASS: reflected addition", "H FAIL: reflected addition")

    # i) Multiplication
    testif(v * NVector(1, 2, 3, 4) == 2, "I PASS: dot product", "I FAIL: dot product")
    testif(v * NVector(1, 2, 3, 4) == 10, "I PASS: dot product", "I FAIL: dot product")

    testif(v * 10 == 30, "I PASS: scalar multiplication", "I FAIL: scalar multiplication")
    testif(v * 10 == 40, "I PASS: scalar multiplication", "I FAIL: scalar multiplication")

    testif(10 * v == 30, "I PASS: reflected multiplication", "I FAIL: reflected multiplication")
    testif(10 * v == 40, "I PASS: reflected multiplication", "I FAIL: reflected multiplication")

    # j) Zero vector
    testif(NVector.zeros(4) == NVector(0, 0, 0, 0), "J PASS: zero vector", "J FAIL: zero vector")
    testif(NVector.zeros(4) == NVector(1, 1, 1, 1), "J PASS: zero vector", "J FAIL: zero vector")

    print("Name: Phan Minh Hy")
    print("Student ID: Z23766758")

if __name__ == "__main__":
    main()
from collections.abc import Sequence

class Nvector:
    def __init__(self, *args: float | Sequence[float]) -> None:
        if len(args) == 1:
            self.elements: list[float] = list(args[0])
        else:
            self.elements: list[float] = list(args)

    def __len__(self) -> int:
        return len(self.elements)
    def __getitem__(self, index: int) -> float:
        return self.elements[index]

def main() -> None:
    n1 = Nvector(3, 0, 1, -1)
    n2 = Nvector([3, 0, 1, -1])
    n3 = Nvector((3, 0, 1, -1))

    print("Vector 1:", n1.elements)
    print("Vector 2:", n2.elements)
    print("Vector 3:", n3.elements)

    print("Length:", len(n1))
    print("Index 1:", n1[1])
    print("Index -2:", n1[-2])

if __name__ == "__main__":
    main()

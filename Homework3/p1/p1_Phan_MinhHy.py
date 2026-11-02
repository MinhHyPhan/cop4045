from collections.abc import Sequence

class Nvector:
    def __init__(self, *args: float | Sequence[float]) -> None:
        if len(args) == 1:
            self.elements: list[float] = list(args[0])
        else:
            self.elements: list[float] = list(args)


if __name__ == "__main__":
   n1 = Nvector(3, 0, 1, -1)
   n2 = Nvector([3, 0, 1, -1])
   n3 = Nvector((3, 0, 1, -1))

   print(n1.elements)
   print(n2.elements)
   print(n3.elements)
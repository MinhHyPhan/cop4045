class Entry:
    def __init__(self, name: str, parent: "Entry | None" = None) -> None:
        self.name = name
        self._parent = parent

    def parent(self) -> "Entry | None":
        return self._parent

    def absolute_path(self) -> list["Entry"]:
        if self._parent is None:
            return [self]
        return [self] + self._parent.absolute_path()

    def size(self) -> int:
        raise NotImplementedError


class File(Entry):
    def __init__(
        self,
        name: str,
        parent: Entry | None = None,
        bytes_used: int = 0,
    ) -> None:
        super().__init__(name, parent)
        self.bytes_used = bytes_used

    @property
    def bytes_used(self) -> int:
        return self._bytes_used

    @bytes_used.setter
    def bytes_used(self, value: int) -> None:
        if value < 0:
            raise ValueError("bytes_used must be nonnegative")
        self._bytes_used = value

    def size(self) -> int:
        return self.bytes_used


class Folder(Entry):
    def __init__(self, name: str, parent: Entry | None = None) -> None:
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        self._children.append(entry)

    def children(self) -> tuple[Entry, ...]:
        return tuple(self._children)

    def size(self) -> int:
        return sum(child.size() for child in self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:
    """Return qualifying files; a file is checked directly, a folder recursively."""
    if isinstance(entry, File):
        return [entry] if entry.size() >= minimum_size else []
    if isinstance(entry, Folder):
        return [
            file
            for child in entry.children()
            for file in find_large_files(child, minimum_size)
        ]
    raise TypeError("entry must be a File or Folder")
import unittest

from p6_Phan_MinhHy import Entry, File, Folder, find_large_files


class FindLargeFilesTests(unittest.TestCase):
    def test_file_meeting_minimum_size_is_returned(self) -> None:
        file = File("large.txt", bytes_used=10)

        self.assertEqual(find_large_files(file, 10), [file])

    def test_file_below_minimum_size_is_not_returned(self) -> None:
        file = File("small.txt", bytes_used=9)

        self.assertEqual(find_large_files(file, 10), [])

    def test_folder_search_includes_nested_files_meeting_minimum_size(self) -> None:
        root = Folder("root")
        nested = Folder("nested", root)
        small_file = File("small.txt", bytes_used=4)
        large_file = File("large.txt", bytes_used=12)
        root.add(small_file)
        root.add(nested)
        nested.add(large_file)

        self.assertEqual(find_large_files(root, 10), [large_file])

    def test_empty_folder_returns_no_files(self) -> None:
        self.assertEqual(find_large_files(Folder("empty"), 0), [])

    def test_deep_folder_size_search_and_absolute_path(self) -> None:
        outer = Folder("outer")
        middle = Folder("middle", outer)
        inner = Folder("inner", middle)
        small_file = File("small.txt", outer, bytes_used=3)
        medium_file = File("medium.txt", middle, bytes_used=7)
        large_file = File("large.txt", inner, bytes_used=11)
        outer.add(small_file)
        outer.add(middle)
        middle.add(medium_file)
        middle.add(inner)
        inner.add(large_file)

        self.assertEqual(outer.size(), 21)
        self.assertEqual(find_large_files(outer, 7), [medium_file, large_file])
        self.assertEqual(find_large_files(outer, 10), [large_file])
        self.assertEqual(large_file.absolute_path(), [large_file, inner, middle, outer])


class AbsolutePathTests(unittest.TestCase):
    def test_root_entry_path_contains_only_itself(self) -> None:
        root = Entry("root")

        self.assertEqual(root.absolute_path(), [root])

    def test_nested_entry_path_runs_from_entry_to_root(self) -> None:
        root = Folder("root")
        nested = Folder("nested", root)
        file = File("document.txt", nested)

        self.assertEqual(file.absolute_path(), [file, nested, root])


if __name__ == "__main__":
    unittest.main()

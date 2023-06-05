from heapq import heapify, heappop, heappush
from os import listdir, makedirs
from functools import total_ordering
from shutil import rmtree


@total_ordering
class LinePointer:
    """
    A class that represents a pointer to a line in a file.

    Attributes:
        __file (file): The file object that the pointer is associated with.
        __current_line (int): The current line number that the pointer points to.

    Methods:
        __init__(file): Initializes a new LinePointer object with the given file object.
        go_next(): Advances the pointer to the next line in the file.
        is_empty(): Returns True if the pointer is currently pointing to an empty line.
        __str__(): Returns a string representation of the current line number.
        __lt__(other): Defines the less-than comparison operator for LinePointer objects.
        __eq__(other): Defines the equality comparison operator for LinePointer objects.
        __repr__(): Returns a string representation of the LinePointer object that can be used to recreate it.

    Usage:
        >>> with open("myfile.txt") as f:
        ...     p = LinePointer(f)
        ...     p.go_next()
        ...     print(p)
        1

    """

    def __init__(self, file):
        self.__file = file
        self.__current_line = None
        self.go_next()

    def go_next(self):
        striped = self.__file.readline().strip()
        if striped:
            self.__current_line = int(striped)
        else:
            self.__current_line = None

    def is_empty(self):
        return not bool(self.__current_line)

    def __str__(self):
        return str(self.__current_line)

    def __lt__(self, other):
        return self.__current_line < other.__current_line

    def __eq__(self, other):
        return self.__current_line == other.__current_line

    def __repr__(self):
        return f'{type(self).__name__}({self.__file!r})'


class ExternalMergeSort:
    """
    A class that performs an external merge sort on a file.

    Attributes:
        __target_file (str): The name of the file to be sorted.
        __result_file (str): The name of the file to write the sorted output to.
        __temp_dir (str): The name of the directory to store temporary files in.
        __chunk_size (int): The number of lines to read into memory at once.

    Methods:
        __init__(target_file, result_file, temp_dir, chunk_size): Initializes a new ExternalMergeSort object.
        __write_lines(lines, target_file): Writes a list of lines to a file.
        __apend_line(line, target_file): Appends a line to a file.
        __split_file(file_name, chunk_size): Splits a file into sorted chunks.
        __merge(): Merges the sorted chunks into a single sorted file.
        do(): Performs the external merge sort.
        __del__(): Deletes the temporary directory and its contents.
        __repr__(): Returns a string representation of the ExternalMergeSort object that can be used to recreate it.

    Usage:
        >>> ems = ExternalMergeSort("unsorted.txt", "sorted.txt", "temp", 1000)
        >>> ems.do()

    Notes:
        The ExternalMergeSort class is intended to be used with text files. If the file contains non-numeric data or if
        the file ends with an empty line, an exception will be raised.
    """

    def __init__(self, target_file, result_file, temp_dir, chunk_size):
        self.__target_file = target_file
        self.__result_file = result_file
        self.__temp_dir = temp_dir
        self.__chunk_size = chunk_size
        self.__temp_files = []
        self.__heap = []
        makedirs(temp_dir, exist_ok=True)

    def __write_lines(self, lines, target_file):
        with open(target_file, "w") as f:
            f.writelines(str(line) for line in lines)

    def __apend_line(self, line, target_file):
        with open(target_file, "a") as f:
            f.write(line)

    def __split_file(self, file_name, chunk_size=10):
        with open(file_name) as r:
            buffer = []
            for index, line in enumerate(r):
                buffer.append(line)
                if (index+1) % chunk_size == 0:
                    buffer = sorted(buffer, key=int)
                    self.__write_lines(buffer, f'{self.__temp_dir}/{index}')
                    self.__temp_files.append(index)
                    buffer.clear()

    def __merge(self):
        for temp_file in self.__temp_files:
            heappush(self.__heap, LinePointer(
                open(f'{self.__temp_dir}/{temp_file}', 'r')))
        while self.__heap:
            min_line_pointer = heappop(self.__heap)
            self.__apend_line(str(min_line_pointer)+'\n', self.__result_file)
            min_line_pointer.go_next()
            if not min_line_pointer.is_empty():
                heappush(self.__heap, min_line_pointer)
            heapify(self.__heap)

    def do(self):
        self.__split_file(self.__target_file, self.__chunk_size)
        self.__merge()

    def __del__(self):
        rmtree(self.__temp_dir)

    def __repr__(self):
        return f'{type(self).__name__}({self.__target_file!r}, {self.__result_file!r}, {self.__temp_dir!r}, {self.__chunk_size!r})'

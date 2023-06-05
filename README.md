# External Merge Sort

This code implements an external merge sort algorithm for sorting large text files that don't fit into memory. The implementation splits the file into smaller sorted chunks, merges them, and writes the result to a new file. The algorithm uses a heap to efficiently keep track of the minimum line in each sorted chunk.

# Requirements

Python 3.6 or later is required to run this implementation. No external libraries are required.

# Usage

To use this implementation, create an instance of the ExternalMergeSort class with the following parameters:

    target_file: the name of the file to be sorted.
    result_file: the name of the file to write the sorted output to.
    temp_dir: the name of the directory to store temporary files in.
    chunk_size: the number of lines to read into memory at once.

Then, call the do() method on the instance to perform the external merge sort.
python

ems = ExternalMergeSort("unsorted.txt", "sorted.txt", "temp", 1000)
ems.do()

Note that the ExternalMergeSort class is intended to be used with text files containing only numeric data. If the file contains non-numeric data or if the file ends with an empty line, an exception will be raised.

# Class Structure

The code consists of two classes: LinePointer and ExternalMergeSort.

## LinePointer

The LinePointer class represents a pointer to a line in a file. It has the following methods:

    __init__(file): Initializes a new LinePointer object with the given file object.
    go_next(): Advances the pointer to the next line in the file.
    is_empty(): Returns True if the pointer is currently pointing to an empty line.
    __str__(): Returns a string representation of the current line number.
    __lt__(other): Defines the less-than comparison operator for LinePointer objects.
    __eq__(other): Defines the equality comparison operator for LinePointer objects.
    __repr__(): Returns a string representation of the LinePointer object that can be used to recreate it.

## ExternalMergeSort

The ExternalMergeSort class performs an external merge sort on a file. It has the following methods:

    __init__(target_file, result_file, temp_dir, chunk_size): Initializes a new ExternalMergeSort object.
    __write_lines(lines, target_file): Writes a list of lines to a file.
    __apend_line(line, target_file): Appends a line to a file.
    __split_file(file_name, chunk_size): Splits a file into sorted chunks.
    __merge(): Merges the sorted chunks into a single sorted file.
    do(): Performs the external merge sort.
    __del__(): Deletes the temporary directory and its contents.
    __repr__(): Returns a string representation of the ExternalMergeSort object that can be used to recreate it.

# Limitations

The code has been tested on small and medium-sized text files. However, it may not be efficient for very large files. Additionally, the implementation assumes that the input file contains only numeric data and does not handle other data types.
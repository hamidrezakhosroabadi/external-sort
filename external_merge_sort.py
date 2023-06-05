import heapq
from os import listdir
from functools import total_ordering


@total_ordering
class Line:
    def __init__(self, line, file):
        self.line = line
        self.file = file

    def __lt__(self, obj):
        return self.line < obj.line

    def __eq__(self, obj):
        return self.line == obj.line


def split_file(file_name, chunk_size=10):
    with open(file_name) as r:
        buffer = []
        for index, line in enumerate(r):
            buffer.append(line)
            if (index+1) % chunk_size == 0:
                buffer = sorted(buffer, key=lambda num: int(num))
                with open(f'temps/{index+1}.txt', 'w') as w:
                    for item in buffer:
                        w.write(item)
                buffer = []


def merge(temp_files, result_file):
    heap = []
    for temp_file in temp_files:
        file = open(f'temps/{temp_file}', 'r')
        line = file.readline()
        heapq.heappush(heap, Line(int(line), file))

    with open(result_file, "w") as w:
        while heap:
            min = heapq.heappop(heap)
            w.write(str(min.line)+'\n')
            file = min.file
            next_line = file.readline()
            if next_line:
                heapq.heappush(heap, Line(int(next_line), file))
            heapq.heapify(heap)


split_file('')
merge(listdir('temps/'), 'result.txt')

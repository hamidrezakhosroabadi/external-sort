from random import randint


def create_test_file(file_name, count=1000, range_begins=0, range_ends=10000):
    with open(file_name, 'w') as f:
        for i in range(count):
            f.write(str(randint(range_begins, range_ends)) + '\n')

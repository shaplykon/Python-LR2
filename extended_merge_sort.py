import random
import linecache
import os
import time


class Error(Exception):
    pass


class OutOfRangeValue(Error):
    pass


def create_file(numbers_amount):
    with open('numbers.txt', 'w') as f:
        f.writelines('{}\n'.format(random.randint(-100000000, 100000000)) for _ in range(numbers_amount))


def file_fragmentation(numbers_amount, memory_limit):
    file_flag = 1
    line = 1
    number_list = []
    while line < numbers_amount:
        number_list.clear()
        for _ in range(0, memory_limit):
            number = linecache.getline("numbers.txt", line)
            number_list.append(number.replace("\n", ""))
            line += 1
        merge_sort(number_list)
        with open(str(file_flag) + ".txt", "a") as file:
            for lines in number_list:
                file.write(str(lines) + "\n")
        if file_flag == 1:
            file_flag = 2
        else:
            file_flag = 1


def merge(left, right, Array):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if int(left[i]) < int(right[j]):
            Array[k] = left[i]
            i = i + 1
        else:
            Array[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
        Array[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        Array[k] = right[j]
        j = j + 1
        k = k + 1


# function for dividing and calling merge function
def merge_sort(Array):
    n = len(Array)
    if n < 2:
        return

    mid = n // 2
    left = []
    right = []

    for i in range(mid):
        number = Array[i]
        left.append(number)

    for k in range(mid, n):
        number = Array[k]
        right.append(number)

    merge_sort(left)
    merge_sort(right)

    merge(left, right, Array)


def sorting(first_file_line, second_file_line, output_file_path, chunk_size, first_file_line_flag,
            second_file_line_flag, first_input, second_input, numbers_amount):
    while first_file_line < numbers_amount // 2 and second_file_line < numbers_amount // 2:
        f = open(output_file_path, "a")
        first_number = linecache.getline(first_input, first_file_line)
        second_number = linecache.getline(second_input, second_file_line)
        while first_file_line_flag <= chunk_size and second_file_line_flag <= chunk_size:

            if int(first_number) <= int(second_number):
                f.write(str(first_number))
                first_file_line += 1
                first_file_line_flag += 1
                first_number = linecache.getline(first_input, first_file_line)
            else:
                f.write(str(second_number))
                second_file_line += 1
                second_file_line_flag += 1
                second_number = linecache.getline(second_input, second_file_line)

        if first_file_line_flag > chunk_size:
            while second_file_line_flag <= chunk_size:
                second_number = linecache.getline(second_input, second_file_line)
                f.write(str(second_number))
                second_file_line += 1
                second_file_line_flag += 1
        else:
            while first_file_line_flag <= chunk_size:
                first_number = linecache.getline(first_input, first_file_line)
                f.write(str(first_number))
                first_file_line += 1
                first_file_line_flag += 1
        output_file_path = change_output(output_file_path)
        first_file_line_flag = 1
        second_file_line_flag = 1


def change_output(path):
    if path == "1.txt":
        return "2.txt"
    elif path == "2.txt":
        return "3.txt"
    elif path == "3.txt":
        return "4.txt"
    elif path == "4.txt":
        return "1.txt"


def change_input(path):
    if path == "1.txt":
        return "3.txt"
    elif path == "2.txt":
        return "4.txt"
    elif path == "3.txt":
        return "1.txt"
    elif path == "4.txt":
        return "2.txt"


def main():
    for i in range(1, 5):
        with open(str(i) + ".txt", "w"):
            pass

    with open("output.txt", "w"):
        pass

    output_file_path = "3.txt"
    numbers_amount = 150000
    memory_limit = numbers_amount // 4
    chunk_size = memory_limit
    start_time = time.time()
    create_file(numbers_amount)
    file_fragmentation(numbers_amount, memory_limit)

    first_file_line = 1
    second_file_line = 1

    first_input_file_path = "1.txt"
    second_input_file_path = "2.txt"

    while chunk_size <= numbers_amount:
        if chunk_size == numbers_amount // 2:
            sorting(1, 1, "output.txt", chunk_size, 1, 1, first_input_file_path, second_input_file_path, numbers_amount)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit(0)
        else:
            sorting(first_file_line, second_file_line, output_file_path, chunk_size, 1, 1, first_input_file_path,
                    second_input_file_path, numbers_amount)
        first_input_file_path = change_input(first_input_file_path)
        second_input_file_path = change_input(second_input_file_path)
        chunk_size *= 2


if __name__ == "__main__":
    main()

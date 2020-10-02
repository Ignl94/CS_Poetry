''' Import module and open poetry text file '''
from random import randint

poetry = "./poetry_slam/poetry.txt"

infile = open(poetry, "r")
# -----------------------------------------------------------------------
lines_list = []
''' Create Functions Section '''


def get_file_lines(filename):
    num = 0  # created counter which is used to display line number
    for line in filename:
        num += 1  # Increase line number by 1 for each line read. first like will read 1
        # Stored what I want to print in variable. The line number and line content
        line_input = f"{num}: {line}"
        lines_list.append(line_input)  # Added stored data to lis
    return lines_list


def lines_printed_backwards(lines_list):
    line_backwards = []
    for line in lines_list:
        if line == lines_list[0]:
            line_backwards.append(line)
        else:
            line_backwards.insert(0, line)

    for line in line_backwards:
        print(line)


def lines_printed_random(lines_list):
    # It should print the lines of your poem in randomly order.
    counter = 17
    index_max = 16
    while counter != 0:
        index = randint(0, index_max)
        print(lines_list[index], end="\n")
        del lines_list[index]
        index_max -= 1
        counter -= 1


get_file_lines(infile)
lines_printed_random(lines_list)


"""def lines_printed_custom(line_list):

        # Make sure that you carefully comment your custom function so it’s clear what it does.
get_file_lines(infile)

lines_printed_backwards(lines_list)"""

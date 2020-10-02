''' Import module and open poetry text file '''
from random import randint
from random import choice

poetry = "./poetry_slam/poetry.txt"

infile = open(poetry, "r")

lines_list = []
# -----------------------------------------------------------------------
# created lines_list variable
''' Create Functions Section '''


def get_file_lines(filename):
    num = 0  # created counter which is used to display line number
    for line in filename:
        num += 1  # Increase line number by 1 for each line read. first like will read 1
        # Stored what I want to print in variable. The line number and line content
        line_input = f"{num}: {line} \n"
        lines_list.append(line_input)  # Added stored data to lis
    return lines_list


def lines_printed_backwards(lines_list):
    """ create empty list to insert poem lines in backwards order """
    line_backwards = []
    for line in lines_list:
        """ make sure line at index 0 is last """
        if line == lines_list[0]:
            line_backwards.append(line)
        else:
            """ insert each other line at index 0 preceding the lines inserted before it. """
            line_backwards.insert(0, line)

    for line in line_backwards:
        print(line, end="\n")


def lines_printed_random(lines_list):
    """ created counters and index-max variable"""
    counter = 17
    index_max = 16
    while counter != 0:
        """ random index generated """
        index = randint(0, index_max)
        """ line at index printed then deleted from list to prevent duplication """
        print(lines_list[index], end="\n")
        del lines_list[index]
        """ max length of list and counter decrease by increments of 1 till counter = 0 """
        index_max -= 1
        counter -= 1


def lines_printed_custom(lines_list):
    """ Prints a choice from configured list of integers """
    counter = 17
    while counter != 0:
        print(choice(lines_list))
        counter -= 1


get_file_lines(infile)
lines_printed_backwards(lines_list)
print("----------------------------------------------------------------------------------------------------------")
lines_printed_custom(lines_list)
print("----------------------------------------------------------------------------------------------------------")
lines_printed_random(lines_list)

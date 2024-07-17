"""
Name: Brian Choo Way Yip
Student Id: 31056334
"""
from random import randint
import time
import sys

def z_algorithm(text,pattern):
    process_string = pattern + "$" + text

    z_lst = [None] * len(process_string)
    #test_lst = [None] * len(pattern)
    #Preprocess String ~ Look for longest substring that matches prefix str[i...i + Zi - 1] == str[1...Zi]


    #RUN z-algorithm
    #Compute base case Z2
    lst = z_lst
    count = 0
    for j in range(len(process_string)-1):
        if process_string[j] == process_string[j+1]:
            count += 1
        else:
            break
    lst[1] = count
    box_i = 1

    #Compute rest of Zi cases
    for i in range(2, len(process_string)):
        r = lst[box_i] + box_i - 1
        if r < i:
            count = 0
            for j in range(len(process_string) - i):
                if process_string[j] == process_string[i+j]:
                    count += 1
                else:
                    break

            if count != 0:
                box_i = i
            lst[i] = count
        else:
            compared_box_i = i - box_i
            if lst[compared_box_i] < r - i + 1:
                lst[i] = lst[compared_box_i]
            else:
                if lst[compared_box_i] > r - i + 1:
                    lst[i] = r - i + 1
                    box_i = i
                else:
                    count = 0
                    for j in range(len(process_string)-r-1):
                        if process_string[r + j + 1] == process_string[(r - i) + j + 1]:
                            count += 1
                        else:
                            break
                    lst[i] = lst[compared_box_i] + count
                    box_i = i

    #Compute Z reverse
    z_lst_reverse = [None] * len(process_string)
    lst = z_lst_reverse

    #Reverse Pattern and Text individually and Join
    process_string_reverse = pattern[::-1] + '$' + text[::-1]

    #Compute Base case for Z reverse
    count = 0
    for j in range(len(process_string_reverse)-1):
        if process_string_reverse[j] == process_string_reverse[j + 1]:
            count += 1
        else:
            break
    lst[1] = count
    box_i = 1


    #Compute rest of Zi cases for Z reverse
    for i in range(2, len(process_string_reverse)):
        r = lst[box_i] + box_i - 1
        if r < i:
            count = 0
            for j in range(len(process_string_reverse) - i):
                if process_string_reverse[j] == process_string_reverse[i + j]:
                    count += 1
                else:
                    break
            if count != 0:
                box_i = i
            lst[i] = count
        else:
            compared_box_i = i - box_i
            if lst[compared_box_i] < r - i + 1:
                lst[i] = lst[compared_box_i]
            else:
                if lst[compared_box_i] > r - i + 1:
                    lst[i] = r - i + 1
                    box_i = i
                else:
                    count = 0
                    for j in range(len(process_string_reverse) - r - 1):
                        if process_string_reverse[r + j + 1] == process_string_reverse[(r - i) + j + 1]:
                            count += 1
                        else:
                            break
                    lst[i] = lst[compared_box_i] + count
                    box_i = i

    string = []

    #Comparing values differing by 2
    for i in range(len(pattern)+1, len(process_string)-len(pattern)+1):
        if z_lst[i] == len(pattern):
            string.append(str(i - len(pattern)))
        else:
            if process_string[z_lst[i] + 1] == process_string[i + z_lst[i]] and process_string[z_lst[i]] == process_string[i + z_lst[i] + 1]:
                str_left = len(pattern) - z_lst[i] - 2
                if z_lst_reverse[len(process_string) - ((i + z_lst[i] + 2 + str_left - 1) - len(pattern))] == str_left:
                    string.append(str(i - len(pattern)) + " " + str(i + z_lst[i] - len(pattern)))
    return string


def read_file(file_path: str) -> str:
    f = open(file_path, 'r')
    line = f.readlines()
    f.close()
    return line

if __name__ == '__main__':
    _, filename1, filename2 = sys.argv
    file1content = read_file(filename1)
    file2content = read_file(filename2)
    result = z_algorithm(file1content[0], file2content[0])
    output = open("output_q1.txt", "w")
    output.write(str(len(result)) + "\n")
    for i in result:
        output.write(i + "\n")
    output.close()





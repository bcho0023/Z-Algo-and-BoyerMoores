"""
Name: Brian Choo Way Yip
Student Id: 31056334
"""
import sys


def boyer_moore(text, pattern):
    #Look for index of special character
    special_ind = pattern.index('.')
    wildcard_z = []
    wildcard_goodsuffix = []

    #Generate z_values for all possible values of the alphabet (reversed twice to calculate z_values from right to left)
    for i in range(26):
        pattern_replace = pattern[::-1].replace('.', chr(i + 97))
        z_lst = z_algo(pattern_replace)[::-1]
        z_lst[-1] = len(pattern)
        wildcard_z.append(z_lst)

    #Generate good suffix table for all possible values of the alphabet
    for i in range(len(pattern)+1):
        wildcard_goodsuffix.append([0] * (26))

    for i in range(len(pattern) - 1):
        for j in range(26):
            ind = len(pattern) - wildcard_z[j][i]
            wildcard_goodsuffix[ind][j] = i + 1

    #Generate match prefix table for all possible values of the alphabet
    wildcard_matchPrefix = []
    for i in range(26):
        wildcard_matchPrefix.append([-1] * len(pattern))
        largest_z = -1
        for j in range(len(pattern)):
            if largest_z < wildcard_z[i][j]:
                largest_z = wildcard_z[i][j]
            wildcard_matchPrefix[i][len(pattern) - j - 1] = largest_z


    #Extend bad character
    extend_bad_character = []
    tracker = [-1] * 26
    for i in range(len(pattern)):
        extend_bad_character.append(tracker[:])
        if pattern[i] != '.':
            tracker[ord(pattern[i]) - 97] = i

    #Boyer Moore's Algorithm
    i = len(pattern) - 1
    j = len(pattern) - 1
    r = i
    good_l = -1
    good_r = -1
    occurrence = []
    count = 0
    while i < len(text) and j < len(pattern):
        # print(f"text index: {i}, pattern index: {j}")
        # print(''.join(str(i) for i in list(range(10))))
        # print(text)
        # print(" " * (r-(len(pattern)-1)) + pattern)


        #Occurance Found
        if j < 0:
            occurrence.append(i+2)
            #special_text = ord(text[i + special_ind + 1]) - 97
            shift = len(pattern) - max(wildcard_matchPrefix[1]) + 1
            j = len(pattern) - 1
            i = i + len(pattern) + shift
            r = i
            #print("Occurrence:", occurrence, good_l, good_r)


        #SKIP compared values
        elif i == good_r and good_l > i - len(pattern):
            i = good_l-1
            j = j - (good_r - good_l)-1
            #print("Optimisation Skipped:", good_l, "and", good_r)


        #Calculate shifts from good_suffix, bad character
        elif pattern[j] != text[i] and pattern[j] != '.':
            textChar = ord(text[i]) - 97
            if max(wildcard_goodsuffix[j+1]) > 0:
                shift = (len(pattern) - max(wildcard_goodsuffix[j+1]))
                #print("good suffix")
            elif extend_bad_character[j][textChar] > -1:
                shift = (j - min(extend_bad_character[j][textChar], special_ind))
                #print("bad", shift)
            else:
                shift = 1
            r += shift
            j = len(pattern) - 1
            i = r
            #print("Shift", shift, "Good_L:", good_l, "Good_R:", good_r)

        #Check values from right to left
        else:
            i -= 1
            j -= 1

        count += 1
        #time.sleep(0.8)
        #print()
    #print("count:", count)
    return  occurrence


def z_algo(process_string):
    lst = [None] * len(process_string)
    # RUN z-algorithm
    # Compute base case Z2
    wildcard = ''
    count = 0
    for j in range(len(process_string) - 1):
        if process_string[j] == process_string[j + 1]:
            count += 1
        else:
            break
    lst[1] = count
    box_i = 1
    # Compute rest of Zi cases
    for i in range(2, len(process_string)):
        r = lst[box_i] + box_i - 1
        if r < i:
            count = 0
            for j in range(len(process_string) - i):
                if process_string[j] == process_string[i + j]:
                    count += 1
                else:
                    break
            if j != 0:
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
                    for j in range(len(process_string) - r - 1):
                        if process_string[r + j + 1] == process_string[(r - i) + j + 1]:
                            count += 1
                        else:
                            break
                    lst[i] = lst[compared_box_i] + count
                    box_i = i
    return lst


def read_file(file_path: str) -> str:
    f = open(file_path, 'r')
    line = f.readlines()
    f.close()
    return line

if __name__ == '__main__':
    _, filename1, filename2 = sys.argv
    file1content = read_file(filename1)
    file2content = read_file(filename2)
    result = boyer_moore(file1content[0], file2content[0])
    output = open("output_q2.txt", "w")
    for i in result:
        output.write(str(i) + "\n")
    output.close()



    # start = time.time()
    # boyer_moore("b"*1000000,"bb.bb")
    # end = time.time()
    # print(end - start)
    # start = time.time()
    # bruteforce_patternmatching_wildcard("b" * 1000000, "bb.bb")
    # end = time.time()
    # print(end - start)
    #print(boyer_moore("gcaatgcctatgtgacc", "tat.tg"))
    #print(boyer_moore("defefeeafeefaerfef", "f.f"))
    #print(boyer_moore("fefafafef", ".ef"))
    #print(boyer_moore("gcag", ".aba"))
    #print(boyer_moore("", "bb.bb"))
    #print(boyer_moore("aatattatacattatttc", "at.att"))
    #print(boyer_moore("aababcabcdabcdeabcdef", ".aba"))
    #print(boyer_moore("aabaacaadaabaaba", "a.ba"))
    #print(boyer_moore("aababcabcdabcdeabcdef", "a.ba"))





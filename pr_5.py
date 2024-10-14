# Task 1 var 3
from unicodedata import digit

# first_str = input('First string: ')
# second_str = input('Second string: ')
#
# def shifting(string_a: str, string_b: str):
#     shift_b = [string_b[i:] + string_b[:i] for i in range(len(string_b))]
#     cnt = 0
#     for shift in shift_b:
#         pos = 0
#         while pos != -1:
#             pos = string_a.find(shift, pos)
#             if pos != -1:
#                 cnt += 1
#                 pos += len(shift)
#
#     return cnt
#
#
# print(shifting(first_str, second_str))7
# ----------------------------------------------------------------------------------------
# Task 2

input_str = input('Input start string: ')

def unpack(str_):
    unpacked = ''
    int_ = ''

    for i in enumerate(str_):
        if i[1].isdigit():
            int_ += i[1]
        else:
            try:
                unpacked += i[1] * int(int_)
            except ValueError:
                unpacked += i[1]
            int_ = ''

    return unpacked


print(unpack(input_str))

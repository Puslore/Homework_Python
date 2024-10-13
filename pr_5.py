# Task 1

first_str = input('First string: ')
second_str = input('Second string: ')

def shifting(string):
    string = f"{string[1]}{string[2:]}{string[0]}"
    return string

def shift(string):
    shift_list = [shifting(string)]

    for i in range(len(string)-1):
        shift_list.append(shifting(shift_list[i]))
    set(shift_list)

    try:
        return shift_list.remove(first_str)

    except KeyError:
        return shift_list


print(shift(first_str))
print(sum([1 if second_str in _ else 0 for _ in shift(first_str)]))

# ----------------------------------------------------------------------------------------
# Task 2

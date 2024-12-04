# big_chislo = 2 ** 74207281 - 1
X = 514229

def start():
    print('Input Pattern and Text like Pattern Text')
    k = input()
    if isinstance(k, str):
        Text, Pattern = k.split()

    else:
        raise ValueError('Check input. It must be only string')

    return Pattern, Text

def hash_(str_):
    p_out = int()
    for i in enumerate(str_):
        p_out += ord(i[1]) * X ** i[0]

    return p_out

def main():
    Pattern, Text = start()

    pat_hash = hash_(Pattern)
    leng = len(Text)

    for i in enumerate(Text):
        check_hash = ''
        for j in range(leng):
            check_hash += Text[i[0]+j-1]

        checked_hash = hash_(check_hash)

        if pat_hash == checked_hash:
            print(Text.index(i))

main()
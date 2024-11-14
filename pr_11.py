import math
import getpass


class Math:

    def __init__(self, cX1_, cY1_, cX2_, cY2_):

        self.cX = cX2_ - cX1_
        self.cY = cY2_ - cY1_

    def vector_length(self):
        return math.sqrt(self.cX ** 2 + self.cY ** 2)

    def coeff_k(self):
        try:
            return (math.degrees(math.atan(abs(self.cY / self.cX))) + 90) if self.cX < 0 else \
                math.degrees(math.atan(abs(self.cY / self.cX)))

        except ZeroDivisionError:
            return 270 if self.cX == 0 else \
                90

    def vector_summ(self, second_vector):
        return [self.cX + second_vector.cX, self.cY + second_vector.cY]

    def vector_subtraction(self, second_vector):
        return [self.cX - second_vector.cX, self.cY - second_vector.cY]

    def vector_power(self, second_vector):
        return [self.cX * second_vector.cX, self.cY * second_vector.cY]


def intro_text():
    print(f'Hi, {getpass.getuser()}!')
    print('Please, choose number of operation that you need to do with vectors:\n')
    print('1) length of vector\n'
          '2) inclination angle of vector\n'
          '3) summ of vectors\n'
          '4) subtraction of vectors\n'
          '5) multiplication of vectors\n')

def intro():
    try:
        intro_text()
        input_type_operation = int(input())

        if input_type_operation in range(1, 6):
            input_vector_cords(input_type_operation)

        else:
            print(f'Please check your input - you must insert only number in range 1-5')
            intro()

    except ValueError as err:
        print(f'Error: {err}. Please check your input - you must insert only number without ")" and other symbols')
        intro()


def input_vector_cords(operation_num):
    try:
        if operation_num in range(1,3):
            print('You need to insert vector coordinates like "1 5 4 6" or "16 24 1 3" (where numbers is x0, y0, x1 and y1 coordinates) with space and without dots, comas and other symbols')
            input_ = map(int, input().split())
            vector = Math(*input_)

            print(vector.vector_length()) if operation_num == 1 else \
                print(vector.coeff_k())

        else:
            print('You need to insert first vector coordinates like "1 5 4 6" or "16 24 1 3" with space and without dots, comas and other symbols')
            input1 = map(int, input().split())
            print('You need to insert second vector coordinates like "1 5 4 6" or "16 24 1 3" with space and without dots, comas and other symbols')
            input2 = map(int, input().split())

            vector1 = Math(*input1)
            vector2 = Math(*input2)

            print(vector1.vector_summ(vector2)) if operation_num == 3 else \
                print(vector1.vector_subtraction(vector2))if operation_num == 4 else \
                print(vector1.vector_power(vector2))


    except ValueError:
        print('Please check your input. You must insert only numbers with spaces')
        input_vector_cords(operation_num)

intro()

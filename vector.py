import math


class Error(Exception):
    pass


class SmallValueError(Error):
    pass


class OutOfRangeValue(Error):
    pass


class Vector(object):
    def __init__(self, dimension, *user_coordinates):
        self.dimension = int(dimension)
        self.coordinates = []
        for index in range(dimension):
            self.coordinates.append(int(user_coordinates[0][index]))

    def __add__(self, other):
        sum_coordinates = []
        for index in range(self.dimension):
            sum_coordinates.append(self.coordinates[index] + other.coordinates[index])
        return Vector(self.dimension, sum_coordinates)

    def __str__(self):
        string = "("
        for index in range(self.dimension):
            string += str(self.coordinates[index])
            if index != self.coordinates.__len__() - 1:
                string += ", "
        string += ")"
        return string

    def __sub__(self, other):
        result_coordinates = []
        for index in range(self.dimension):
            result_coordinates.append(self.coordinates[index] - other.coordinates[index])
        return Vector(self.dimension, result_coordinates)

    def __mul__(self, other):
        result_coordinates = []
        result = 0
        if isinstance(other, int):
            for index in range(self.dimension):
                result_coordinates.append(self.coordinates[index] * other)
            return Vector(self.dimension, result_coordinates)
        if isinstance(other, Vector):
            for index in range(self.dimension):
                result += self.coordinates[index] * other.coordinates[index]
            return result

    def __eq__(self, other):
        for index in range(self.dimension):
            if self.coordinates[index] != other.coordinates[index]:
                return False
        return True


def show_operations():
    operation = input("\nChoose operation:\n" +
                      "1. Addition\n" +
                      "2. Subtraction\n" +
                      "3. Multiplication by a constant\n" +
                      "4. Scalar multiplication\n" +
                      "5. Comparison\n" +
                      "6. Length of vectors\n" +
                      "7. Exit\n")
    while True:
        try:
            if 0 < int(operation) < 8:
                return int(operation)
            else:
                raise OutOfRangeValue
        except OutOfRangeValue:
            print("Value is out of range!")
            operation = input()


def input_coordinates(dimension, vector_number):
    coordinates = []
    print("\nInput coordinates for " + str(vector_number) + " vector:\n")
    for i in range(int(dimension)):
        coordinate = input(str(i + 1) + ": ")
        coordinates.append(coordinate)
    return coordinates


def show_info(first_vector, second_vector):
    print("\nFirst vector: " + str(first_vector) + "\t" * 2 + "Second vector: " + str(second_vector))


def get_vector_length(vector):
    length = 0
    for i in range(vector.dimension):
        length += pow(vector.coordinates[i], 2)
    return math.sqrt(length)


def main():
    while True:
        try:
            dimension = int(input("Input vectors dimension: "))
            if dimension <= 0:
                raise SmallValueError
            else:
                break
        except SmallValueError:
            print("Value is too small!")

    first_vector = Vector(dimension, input_coordinates(dimension, 1))
    second_vector = Vector(dimension, input_coordinates(dimension, 2))
    while True:
        show_info(first_vector, second_vector)
        operation = show_operations()
        if operation == 1:
            print("\n", first_vector, " + ", second_vector, " = ", first_vector + second_vector)
        elif operation == 2:
            print("\n", first_vector, " - ", second_vector, " = ", first_vector - second_vector)
        elif operation == 3:
            constant = int(input("Input a constant: "))
            print("\n", first_vector, " * ", constant, " = ", str(first_vector * constant), "\t" * 2,
                  second_vector, " * ", constant, " = ", str(second_vector * constant))
        elif operation == 4:
            print("\n", first_vector, " * ", second_vector, " = ", first_vector * second_vector)
        elif operation == 5:
            if first_vector == second_vector:
                print("\nVector ", first_vector, "is equal vector ", second_vector)
            else:
                print("\nVector ", first_vector, "is NOT equal vector ", second_vector)
        elif operation == 6:
            print("\nThe length of ", first_vector, " vector = ", "{:1.4f}".format(get_vector_length(first_vector)),
                  "\n")
            print("The length of ", second_vector, " vector = ", "{:1.4f}".format(get_vector_length(second_vector)),
                  "\n")
        elif operation == 7:
            quit()


if __name__ == "__main__":
    main()

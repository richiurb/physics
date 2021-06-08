import sympy as sym
from config import Config


class Matrix:
    def __init__(self, previous_u, a):
        self.previous_u = previous_u
        self.a = a
        self.delta_t = Config.DELTA_T
        self.delta_x = Config.DELTA_X
        self.n = int(Config.LENGTH / Config.DELTA_X)

    def solve(self):
        matrix = self.generate_matrix()
        column = self.generate_column()

        a = sym.Matrix(matrix)
        b = sym.Matrix(column)

        result = sym.linsolve([a, b])

        answers = [Config.U_0]

        a = next(iter(result))
        for i in range(len(a)):
            answers.append(sym.N(a[i]))

        answers.append(Config.U_LENGTH)

        return answers

    def generate_matrix(self):
        matrix = []

        first = [self.coefficient_main(), self.coefficient()]
        for i in range(2, self.n - 1):
            first.append(0)

        matrix.append(first)

        for i in range(self.n - 3):
            line = []

            for j in range(i):
                line.append(0)

            line.append(self.coefficient())
            line.append(self.coefficient_main())
            line.append(self.coefficient())

            for j in range(i + 3, self.n - 1):
                line.append(0)

            matrix.append(line)

        last = []
        for i in range(self.n - 3):
            last.append(0)
        last.append(self.coefficient())
        last.append(self.coefficient_main())

        matrix.append(last)

        return matrix

    def generate_column(self):
        column = []

        first = self.previous_u[1] - self.coefficient() * \
            (self.previous_u[2] - 2 * self.previous_u[1] + self.previous_u[0] + Config.U_0)
        column.append(first)

        for i in range(2, self.n - 1):
            temp = self.previous_u[i] - self.coefficient() * \
                   (self.previous_u[i + 1] - 2 * self.previous_u[i] + self.previous_u[i - 1])
            column.append(temp)

        last = self.previous_u[self.n - 1] - self.coefficient() * \
            (self.previous_u[self.n] - 2 * self.previous_u[self.n - 1] + self.previous_u[self.n - 2] + Config.U_LENGTH)
        column.append(last)

        return column

    def coefficient_main(self):
        return 1 + (self.a * self.a * self.delta_t / (self.delta_x * self.delta_x))

    def coefficient(self):
        return -(self.a * self.a * self.delta_t / (2 * self.delta_x * self.delta_x))

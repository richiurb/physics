from graphic import Graphic
import start

if __name__ == '__main__':
    a = float(input("Введите тепловой коэффициент: "))
    start_u = start.get()
    print(start_u)
    Graphic(a, start_u).get()

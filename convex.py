from deq import Deq
from r2point import R2Point
from convex2 import tri, is_in_triangle


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def otvet(self):
        return 0


class Void(Figure):
    """ "Hульугольник" """

    def __init__(self, treug):
        self.treug = treug

    def add(self, p):
        return Point(p, self.treug)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p, treug):
        self.p = p
        self.treug = treug

    def add(self, q):
        return self if self.p == q else Segment(self.p, q, self.treug)

    def otvet(self):
        if is_in_triangle(self.p, self.treug):
            return 1
        else:
            return 0


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q, treug):
        self.p, self.q = p, q
        self.treug = treug

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def otvet(self):
        if is_in_triangle(self.p, self.treug) and\
           is_in_triangle(self.q, self.treug):
            return 2
        elif (is_in_triangle(self.p, self.treug)) or\
             (is_in_triangle(self.q, self.treug)):
            return 1
        else:
            return 0

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r, self.treug)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r, self.treug)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q, self.treug)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c, treug):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))

        self.treug = treug
        self.otv = 0
        if is_in_triangle(a, self.treug):
            self.otv += 1
        if is_in_triangle(b, self.treug):
            self.otv += 1
        if is_in_triangle(c, self.treug):
            self.otv += 1

    def otvet(self):
        return self.otv

        # print(convex2.spisok())

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                if is_in_triangle(p, self.treug):
                    self.otv -= 1
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())

                if is_in_triangle(p, self.treug):
                    self.otv -= 1

                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())

            if is_in_triangle(t, self.treug):
                self.otv += 1

            # self.otv += 2
            self.points.push_first(t)

        return self


if __name__ == "__main__":
    # print('Введите координаты точек треугольника:')
    p = R2Point(0, 0)
    q = R2Point(1, 1)
    r = R2Point(1, 0)
    A = tri(p, q, r)
    f = Void(A)
    f = f.add(R2Point(0.9, 0.7))
    f = f.add(R2Point(0.9, 0.6))
    f = f.add(R2Point(0.8, 0.6))
    f = f.add(R2Point(0.5, 0.6))
    print(f"S = {f.area()}, P = {f.perimeter()}, tochek = {f.otvet()}\n")

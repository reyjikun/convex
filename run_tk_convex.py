#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from convex2 import tri


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)

tk = TkDrawer()

try:
    print('Введите координаты точек треугольника:')
    p = R2Point()
    q = R2Point()
    r = R2Point()
    A = tri(p, q, r)
    tk.draw_line(p, q)
    f = Void(A)
    s = Void(A)
    tk.clean()
    print()
    print('Введите координаты точек выпуклой оболочки:')
    while True:
        tk.draw_line(p, q)
        tk.draw_line(p, r)
        tk.draw_line(r, q)
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, tochek = {f.otvet()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()

from r2point import R2Point as Point


class tri:

    def __init__(self, a, b, c):
        self.spisok = [a, b, c]

    def pprint(self):
        for i in range(len(self.spisok)):
            print(self.spisok[i].x, self.spisok[i].y)


def is_in_triangle(dot, triangle):
    # Check if dot is on a vertex
    for vertex in triangle.spisok:
        if dot == vertex:
            return True

    # Check if dot is on an edge
    # Calculate area of triangle
    area = abs(Point.area(triangle.spisok[0], triangle.spisok[1],
               triangle.spisok[2]))

    # Calculate area of 3 triangles made between point and triangle vertices
    area1 = -Point.area(dot, triangle.spisok[0], triangle.spisok[1])
    area2 = -Point.area(dot, triangle.spisok[1], triangle.spisok[2])
    area3 = -Point.area(dot, triangle.spisok[2], triangle.spisok[0])
    # print(area1, area2, area3)
    inside = False
    if area == abs(area1) + abs(area2) + abs(area3):
        # print('inside')
        inside = True
    if 2 * area1 / Point.dist(triangle.spisok[0], triangle.spisok[1])\
       < 1 and area1 > 0:
        inside = True
    if 2 * area2 / Point.dist(triangle.spisok[1], triangle.spisok[2])\
       < 1 and area2 > 0:
        inside = True
    if 2 * area3 / Point.dist(triangle.spisok[2], triangle.spisok[0])\
       < 1 and area3 > 0:
        inside = True
    # If sum of three area equals to area of triangle
    # then dot is inside triangle
    if inside:
        return True
    else:
        return False

# Example usage
# print(is_in_triangle(point, A))
# a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
# A.pprint()

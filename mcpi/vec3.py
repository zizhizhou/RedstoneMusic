from random import randint


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.up = self.t
        self.down = self.b

    def __add__(self, rhs):
        c = self.clone()
        c += rhs
        return c

    def __iadd__(self, rhs):
        self.x += rhs.x
        self.y += rhs.y
        self.z += rhs.z
        return self

    def length(self):
        return self.lengthSqr() ** .5

    def lengthSqr(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def __mul__(self, k):
        c = self.clone()
        c *= k
        return c

    def __imul__(self, k):
        self.x *= k
        self.y *= k
        self.z *= k
        return self

    def clone(self):
        return Vec3(self.x, self.y, self.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __sub__(self, rhs):
        return self.__add__(-rhs)

    def __isub__(self, rhs):
        return self.__iadd__(-rhs)

    def __repr__(self):
        return "Vec3(%s,%s,%s)" % (self.x, self.y, self.z)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def _map(self, func):
        self.x = func(self.x)
        self.y = func(self.y)
        self.z = func(self.z)

    def __cmp__(self, rhs):
        dx = self.x - rhs.x
        if dx != 0: return dx
        dy = self.y - rhs.y
        if dy != 0: return dy
        dz = self.z - rhs.z
        if dz != 0: return dz
        return 0

    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y and self.z == rhs.z

    def iround(self):
        self._map(lambda v: int(v + 0.5))
        return self

    def ifloor(self):
        self._map(int)
        return self

    def rotateLeft(self):
        self.x, self.z = self.z, -self.x
        return self

    def rotateRight(self):
        self.x, self.z = -self.z, self.x
        return self

    def cubeCenter(self, len):
        """Get a tuple of two points (vec1, vec2) to create a cube whose center is self"""
        p = Vec3(len // 2, len // 2, len // 2)
        return self.__add__(p), self.__sub__(p)

    def cubeAbove(self, len):
        """Get a tuple of two points (vec1, vec2) to create a cube whose floor center is self"""
        center = self.clone()
        center.y += len // 2
        return center.cubeCenter(len)

    def cubeVertex(self, len):
        """Get a tuple of two points (vec1, vec2) to create a cube whose NW vertex is self"""
        center = self.clone() + Vec3(len // 2, len // 2, len // 2)
        return center.cubeCenter(len)

    def flatCenter(self, len, height):
        """Get a tuple of two points (vec1, vec2) to create a flat cuboid"""
        p = Vec3(len // 2, height // 2, len // 2)
        return self.__add__(p), self.__sub__(p)

    def flatVertex(self, len, height):
        """Get a tuple of two points (vec1, vec2) to create a flat cuboid"""
        return self, self.__add__(Vec3(len, height, len))

    def flatAbove(self, len, height):
        """Get a tuple of two points (vec1, vec2) to create a flat cuboid"""
        return self.up(height // 2).flatCenter(len, height)

    def randFlatCenter(self, len):
        """Get a random position of the same height within len * len square"""
        return self.clone() + Vec3(randint(-len // 2, len // 2),
                                   0, randint(-len // 2, len // 2))

    # Deviations: top (go up), bottom (go down), east, west, south, north
    def t(self, l: int = 1):
        return Vec3(self.x, self.y + l, self.z)

    def b(self, l: int = 1):
        return self.t(-l)

    def e(self, l: int = 1):
        return Vec3(self.x + l, self.y, self.z)

    def w(self, l: int = 1):
        return self.e(-l)

    def s(self, l: int = 1):
        return Vec3(self.x, self.y, self.z + l)

    def n(self, l: int = 1):
        return self.s(-l)


def testVec3():
    # Note: It's not testing everything

    # 1.1 Test initialization
    it = Vec3(1, -2, 3)
    assert it.x == 1
    assert it.y == -2
    assert it.z == 3

    assert it.x != -1
    assert it.y != +2
    assert it.z != -3

    # 2.1 Test cloning and equality
    clone = it.clone()
    assert it == clone
    it.x += 1
    assert it != clone

    # 3.1 Arithmetic
    a = Vec3(10, -3, 4)
    b = Vec3(-7, 1, 2)
    c = a + b
    assert c - a == b
    assert c - b == a
    assert a + a == a * 2

    assert a - a == Vec3(0, 0, 0)
    assert a + (-a) == Vec3(0, 0, 0)

    # Test repr
    e = eval(repr(it))
    assert e == it


if __name__ == "__main__":
    testVec3()

from Cryptodome.Util.number import inverse
# You may also use sympy's inverse function

from collections import namedtuple

Origin = 'O'
Point = namedtuple('Point', ('x','y'))
# a = ?
# b = ?
# p = ?

def point_addition(P, Q):
    if P == Origin:
        return Q
    elif Q == Origin:
        return P
    elif P.x == Q.x and P.y == -P.y:
        return Origin
    else:
        if P != Q:
            l = ((Q.y - P.y)*inverse((Q.x - P.x),p)) % p
        else:
            l = (((3*P.x**2) + a)*inverse((2*P.y),p)) % p
        X = ((l**2) - P.x - Q.x)% p
        Y = (l*(P.x - X) - P.y) % p
        return Point(X,Y)

# P = ?
# Q = ?
print(point_addition(point_addition(P, Q)))



import math
import stdio

class Point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self._x = x
        self._y = y
        self._z = z
    
    def distToOrigin(self):
        #Return the distance of p to origin ie, the point(0,0,0)
        return math.sqrt(self._x**2 + self._y**2 + self._z**2)
    def distTo(self, other):
        #Return the distance of p to the point q
        return math.sqrt((self._x - other._x)**2 + (self._y - other._y)**2 + (self._z - other._z)**2)
        
    def flip(self):
        #Return a Point3D object whose x,y, and z coordinates are negative of p's x, y, and z coords
        return Point3D(-self._x, -self._y, -self._z)
    def __lt__(self, other):
        #Return True of p's distane to origin is less than q's distance to the orign: and false otherwise
        return self.distToOrigin() <= other.distToOrigin()
    
    def __eq__(self, other):
        #Return True of p's distane to origin is equalt to q's distance to the origin; and false otherwise
        return self.distToOrigin() == other.distToOrigin()
    def __str__(self):
        #return a string representation of point p; for example, "(1, 1, 1)"
        return "(" + str(self._x ) + ", " + str( self._y ) + ", " + str( self._z ) + ")"
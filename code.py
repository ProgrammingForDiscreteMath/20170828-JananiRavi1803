from math import *
class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def add(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    def multiply(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber((self.real*other.real) - (self.imaginary*other.imaginary), (self.imaginary*other.real) + (self.real*other.imaginary))
    def complex_conjugate(self):
        """
        In-place method which does not return anything, but replaces the instance by its complex conjugate
        """
        self.real = self.real
        self.imaginary = -self.imaginary
        
        
class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
    def polar_coordinates(self):
        """
        Returns polar co-ordinates for the complex form
        a + bi = rcos0 + i rsin0
        """
        (a, b) = (self.real, self.imaginary)
        theta = atan(b/a)
        r = sqrt(a**2 + b**2)
        return (round(r, 2), round(theta, 2))
    def logarithm(self):
        """
        Returns logarithm of complex number
        log(a+bi) = log(r) + i*theta
        """
        a, b = self.polar_coordinates()
        return NonZeroComplexNumber(round(log(a),2), round(b,2))

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real, self.imaginary = real, imaginary

    def __add__(self, no):
        real = self.real + no.real
        imag = self.imaginary + no.imaginary
        return __class__(real, imag)

    def __sub__(self, no):
        real = self.real - no.real
        imag = self.imaginary - no.imaginary
        return __class__(real, imag)
        
    def __mul__(self, no):
        real = self.real*no.real - self.imaginary*no.imaginary
        imag = self.real*no.imaginary + no.real*self.imaginary
        return __class__(real, imag)

    def __truediv__(self, no):
        real = self.real*no.real + self.imaginary*no.imaginary
        real /= pow(no.real, 2) + pow(no.imaginary, 2)
        imag = self.imaginary*no.real - self.real*no.imaginary
        imag /= pow(no.real, 2) + pow(no.imaginary, 2)
        return __class__(real, imag)

    def mod(self):
        real = math.sqrt(pow(self.real,2) + pow(self.imaginary, 2))
        imag = 0.00
        return __class__(real, imag)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

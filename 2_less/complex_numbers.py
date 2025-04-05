import math

class Complex(object):
    def __init__(self, real, imaginary):
        # your code here
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, no):
        # your code here
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        # your code here
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        # your code here
        # (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = self.real * no.real - self.imaginary * no.imaginary
        imag_part = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real_part, imag_part)

    def __truediv__(self, no):
        # your code here
        # Делим на комплексное число с помощью умножения на сопряженное
        denominator = no.real ** 2 + no.imaginary ** 2
        conj_real = no.real
        conj_imag = -no.imaginary

        numerator_real = self.real * conj_real - self.imaginary * conj_imag
        numerator_imag = self.real * conj_imag + self.imaginary * conj_real

        return Complex(numerator_real / denominator,
                       numerator_imag / denominator)

    def mod(self):
        # your code here
        result = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return round(result, 2)
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

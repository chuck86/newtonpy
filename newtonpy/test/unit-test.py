import unittest

from numpy import sin, cos, abs

from newton import newton


class NewtonTest(unittest.TestCase):
    def test_sin(self):
        assert(abs(sin(newton(sin, cos, 0.5))) < 1e-8)

    def test_polynomial(self):
        def fun(x):
            return x**2-1
        result = newton(fun, lambda x: 2*x, 2.)
        assert(abs(fun(result)) < 1e-8)

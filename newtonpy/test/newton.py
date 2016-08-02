from __future__ import division

from numpy import abs, cos, sin


def newton(fun, gradient, init_value):
    tol = 1e-8

    x = init_value
    f = fun(x)
    df = gradient(x)
    error = abs(fun(x))
    iter = 0
    if iter > 0:
        print("iter is big")
    while error > tol and iter < 100:
        iter += 1
        dx = f/df
        x = x-dx
        f = fun(x)
        df = gradient(x)
        error = abs(f)
    if iter == 100:
        print("max iter reached")
    return x

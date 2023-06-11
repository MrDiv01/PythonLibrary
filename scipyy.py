# from scipy import integrate
# def f(x):
#     return x**2

# result ,err = integrate.quad(f,0,1)

# from scipy import special
# def f(x):
#     return x**2
# resulr=special.jv(1,1.5)

from scipy import integrate
def f(x):
    return x**2
a = integrate.quad(f,0,1)
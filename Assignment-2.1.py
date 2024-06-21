from math import e as e, cos as cos, sin as sin

max_iter = 1000

def bisection(f, a, b, tol):
    iterations = 0
    while abs(f((a + b) / 2)) > tol and iterations < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return (a + b) / 2, iterations

def newtons(f, derf, x, tol):
    iterations = 0
    while abs(f(x)) > tol and iterations < max_iter:
        x = x - f(x) / derf(x)
        iterations += 1
    return x, iterations

def secant(f, x1, x2, tol):
    iterations = 0
    while abs(f(x2)) > tol and iterations < max_iter:
        temp = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        x1 = x2
        x2 = temp
        iterations += 1
    return x2, iterations

def regulaFalsi(f, a, b, tol):
    iterations = 0
    while abs(f(b - (f(b) / ((f(b) - f(a)) / (b - a))))) > tol and iterations < max_iter:
        c = b - (f(b) / ((f(b) - f(a)) / (b - a)))
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return b - (f(b) / ((f(b) - f(a)) / (b - a))), iterations


def f1(x):
    return x ** 31 -1000

def f2(x):
    return (sin(x) ** 5) * (cos(x) ** 3) - (e ** x)

def f3(x):
    q = - x**2 - sin(x) - x
    return 1 / (1 + e**q) - 0.5

def derf1(x):
    return 31 * (x ** 30)

def derf2(x):
    return 5 * (sin(x)**4) * (cos(x)**4) - 3 * (cos(x)**2) * (sin(x)**6) - (e**x)

def derf3(x):
    q = - x**2 - sin(x) - x
    dq = - 2 * x - cos(x) - 1
    eq = e ** q
    return (- eq * dq) / ((1 + eq) ** 2)

tol = 0.001
funcs = (f1, f2, f3)
derf = (derf1, derf2, derf3)
methods = {bisection: 'Bisection Method', newtons: 'Newtons Method', secant:'Secant Method', regulaFalsi:'Regula Falsi Method'}
init_interval = ((-4, 3),   # for f1
                 (-5, 3),   # for f2
                 (-2, -1)   # for f3
)

results = [[], [], []]

for i, (f, der, (a, b)) in enumerate(zip(funcs, derf, init_interval)):
    for method, name in methods.items():
        if name == 'Newtons Method': 
            root, iters = method(f, der, a, tol)
        elif name == 'Secant Method':
            root, iters = method(f, a, b, tol)
        else:
            root, iters = method(f, a, b, tol)
        results[i].append((name, root, iters))


def sortThird(val):
    return val[2]

for i, result in enumerate(results):
    print(f"\nFor function{i+1} (Ranked acc. to no. of iterations):")
    result.sort(key = sortThird)
    for method_res in result:
        name, root, iters = method_res
        print(f"Method: {name}, Root: {root}, Iterations: {iters}")

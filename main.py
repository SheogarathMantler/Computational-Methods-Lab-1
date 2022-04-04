import math as m


def f(x):
    return m.exp(-x ** 2) * x ** 2 + (1 - m.exp(1) - x ** 2) * m.sin(x)
def g(x):
    return x*m.sin(10*x)

def fib(n):
    return (((1 + m.sqrt(5)) / 2) ** n - ((1 - m.sqrt(5)) / 2) ** n) / m.sqrt(5)
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0


def dichotomy(func, a0, b0, epsilon):
    count = 0
    delta = 0.9 * (epsilon / 2)
    a = a0
    b = b0
    while b - a > epsilon:
        x1 = (a + b) / 2 - delta
        x2 = (a + b) / 2 + delta
        f1 = func(x1)
        f2 = func(x2)
        if f1 > f2:
            a = x1
        if f1 < f2:
            b = x2
        if f1 == f2:
            a = x1
            b = x2
        print("a ", a, " b ", b)
        count += 1
    print("итераций: ", count)
    return (a + b) / 2


def golden_ratio(func, a0, b0, epsilon):
    count = 0
    a = a0
    b = b0
    x1 = a + (b - a) * (3 - m.sqrt(5)) / 2
    f1 = func(x1)
    while b - a > epsilon:
        x2 = b - (x1 - a)
        f2 = func(x2)
        if x2 < x1:
            temp = x1
            x1 = x2
            x2 = temp
            temp = f1
            f1 = f2
            f2 = temp
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
        else:
            b = x2
        print("a ", a, " b ", b)
        count += 1
    print("итераций: ", count)
    return (a + b) / 2


def parabola(func, a0, b0, epsilon):
    count = 0
    a = a0
    b = b0
    fa = func(a0)
    fb = func(b0)
    x1 = (a + b) / 2
    f1 = func(x1)
    while abs(b - a) > epsilon:
        x2 = x1 - (((x1 - a) ** 2 * (f1 - fb) - (x1 - b) ** 2 * (fb - fa)) / (
                    (x1 - a) * (f1 - fb) - (x1 - b) * (f1 - a))) / 2
        f2 = func(x2)
        if f1 > f2:
            a = x1
            fa = f1
            x1 = x2
            f1 = f2
        else:
            b = x2
            fb = f2
        print("a ", a, " b ", b)
        count += 1
    print("итераций: ", count)
    return (a + b) / 2


def fibonacci(func, a0, b0, epsilon):
    a = a0
    b = b0
    n = 0
    fn = 0
    while fn <= (b0 - a0) / epsilon:  # computing n
        fn = fib(n + 2)
        n += 1
    x1 = a + fib(n) / fib(n + 2) * (b - a)  # first iteration
    x2 = a + fib(n + 1) / fib(n + 2) * (b - a)
    f1 = func(x1)
    f2 = func(x2)
    if f1 > f2:
        a = x1
        x1 = x2
        f1 = f2
    else:
        b = x2
    for i in range(n):  # other iterations
        x2 = b - (x1 - a)
        f2 = func(x2)
        if x2 < x1:
            temp = x1
            x1 = x2
            x2 = temp
            temp = f1
            f1 = f2
            f2 = temp
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
        else:
            b = x2
        print("a ", a, " b ", b)
    print("итераций: ", n)
    return (a + b) / 2


def combined_Brent(func, a, b, epsilon):
    g_ratio = (1 + m.sqrt(5)) / 2
    number_of_iterations = 1
    x = v = w = (a+b)/2
    fx = fw = fv = f(x)
    d = e = b - a
    while True:
        print(number_of_iterations)
        number_of_iterations += 1
        g = e
        u = -1
        e = d
        if x != v and x != w and w != v and fx != fv and fx != fw and fv != fw:  # если точки разные
            if w > v:
                a1 = (fx - fv) / (x - v)
                a2 = ((fw - fv) / (w - v) - (fx - fv) / (x - v)) / (w - x)
                u = (v + x - (a1 / a2)) / 2
            else:
                a1 = (fx - fw) / (x - w)
                a2 = ((fv - fw) / (v - w) - (fx - fw) / (x - w)) / (v - x)
                u = (w + x - (a1 / a2)) / 2
        if u - a > epsilon and u < b - epsilon and abs(u - x) < g / 2:
            d = abs(u - x)
        else:  # если не выполнено условие то золотое сечение
            if x < (b - a) / 2:
                u = x + (b - x) / g_ratio
                d = b - x
            else:
                u = x - (x - a) / g_ratio
                d = x - a
        if abs(u - x) < epsilon:
            print("итераций: ", number_of_iterations)
            return u
        fu = func(u)
        if fu < fx:
            if u >= x:
                a = x
            else:
                b = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if u >= x:
                b = u
            else:
                a = u
            if fu <= fw or w == x:
                v = w
                w = u
                fv = fw
                fw = fu
            elif fu <= fv or v == x or v == w:
                v = u
                fv = fu


left = 1
right = 5

m = combined_Brent(g, left, right, 0.01)
print("результат: ", m)

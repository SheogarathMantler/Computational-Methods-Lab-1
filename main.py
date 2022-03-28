import math as m


def f(x):
    return m.exp(-x ** 2) * x ** 2 + (1 - m.exp(1) - x ** 2) * m.sin(x)


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
    delta = epsilon / 2
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
    return (a + b) / 2


def golden_ratio(func, a0, b0, epsilon):
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
    return (a + b) / 2


def parabola(func, a0, b0, epsilon):
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
    print("a ", a, " b ", b)
    return (a + b) / 2


def fibonacci(func, a0, b0, epsilon):
    a = a0
    b = b0
    n = 0
    fn = 0
    while fn < (b0 - a0) / epsilon:  # computing n
        fn = fib(n + 2)
        n += 1
    print("n =", n)
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
    return (a + b) / 2


def combined_Brent(func, a0, b0, epsilon):
    a = a0
    b = b0
    x = w = v = (a + b) / 2
    fx = fw = fv = func(x)
    k = (3-m.sqrt(5))/2
    d = e = b - a
    while abs(b - a) > epsilon:
        g = e
        e = d
        if (x != w) and (w != v) and (x != v) and (fx != fw) and (fw != fv) and (fv != fx):  # если точки разные
            u = x - (((x - w) ** 2 * (fx - fv) - (x - v) ** 2 * (fv - fw)) / (
                    (x - w) * (fx - fv) - (x - v) * (fx - fw))) / 2
            if (u >= a + epsilon) and (u <= b - epsilon) and (abs(u - x) < g/2):
                d = abs(u - x)
            else:    # если не выполнено условие то золотое сечение
                if x < (b - a) / 2:
                    u = x + k * (b - x)
                    d = b - x
                else:
                    u = x - k * (x - a)
                    d = x - a
        else:        # если не выполнено условие то золотое сечение
            if x < (b - a)/2:
                u = x + k*(b - x)
                d = b - x
            else:
                u = x - k*(x - a)
                d = x - a
        if abs(u - x) < epsilon:
            u = x + sign(u - x)*epsilon
        fu = func(u)
        if fu <= fx:
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
            if u > x:
                b = u
            else:
                a = u
            if (fu < fw) or (w == x):
                v = w
                w = u
                fv = fw
                fw = fu
            elif (fu < fv) or (v == x) or (v == w):
                v = u
                fv = fu
            else:
                print("STOP")
        print("a ", a, " b ", b)
    print("a ", a, " b ", b)
    return (a + b) / 2


left = 0
right = 2 * m.pi

m = combined_Brent(f, left, right, 0.01)
print(m)

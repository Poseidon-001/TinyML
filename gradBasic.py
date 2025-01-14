import numpy as np
import matplotlib.pyplot as plt

# giả sử ta có hàm số f(x) = x^2 + 5 sin(x)
# -> f'(x) = 2x + 5 cos(x)
# Có hàm số học hỏi: x(update) = x(previous) - learning_rate * f’(x)
# x* là điểm cực tiểu của hàm số f(x)
# xt là điểm sau lần lặp t ta cần tìm điểm xt gần với điểm x* nhất


def gradFx(x):
    return 2 * x + 5 * np.cos(x)


def f(x):
    return x**2 + 5 * np.sin(x)


def f2(x):
    return 1 / 2 * (x - 1) ** 2 - 2


def gradFx2(x):
    return x - 1


def preview_func(x=np.linspace(-10, 10, 100)):
    plt.plot(x, f(x), color="blue")
    return plt


def preview_func2(x=np.linspace(-10, 10, 100)):
    plt.plot(x, f2(x), color="blue")
    return plt


def draw(it, x: list, y: list):
    xl = np.linspace(-10, 10, 10)
    yl = f2(xl)
    amount = 9
    fig, axs = plt.subplots(3, 3)
    fig.suptitle("Vertically stacked subplots")
    for i in range(it - amount, it):
        for col in range(3):
            for row in range(3):
                # axs[np.abs(i-(it-1))].plot(xl, yl)
                # axs[np.abs(i-(it-1))].plot([x[i]], [y[i]], "ro")
                axs[col][row].plot(xl, yl)
                axs[col][row].plot([x[i]], [y[i]], "ro")


def gradDescent(x0, learning_rate, precision, case=1):
    x_current = x0
    y0 = f2(x0) if case == 2 else f(x0)
    it = 0
    x_point = np.array([])
    y_point = np.array([])
    plt1 = preview_func2() if case == 2 else preview_func()
    plt1.plot([x0], [y0], "ro")
    while True:
        x_new = (
            x_current - learning_rate * gradFx2(x_current)
            if case == 2
            else x_current - learning_rate * gradFx(x_current)
        )
        x_point = np.append(x_point, x_new)
        y_point = (
            np.append(y_point, f2(x_new)) if case == 2 else np.append(y_point, f(x_new))
        )
        y_rs = f2(x_new) if case == 2 else f(x_new)
        plt1.plot([x_new], [y_rs], "ro")
        if abs(x_new - x_current) < precision:
            break
        x_current = x_new
        it += 1
    plt.title(f"x= {x_new} with iteration: {it}")
    plt.annotate(
        "start point",
        xy=(x0, y0),
        xytext=(x0 + 3, y0 + 1.5),
        arrowprops=dict(facecolor="black", shrink=0.05),
    )
    plt1.show()
    return x_new, it


c = 1
l_r = 0.3
thresh = 0.001
x, it = gradDescent(-5, l_r, thresh, case=c)
x, it = gradDescent(5, l_r, thresh, case=c)
print(f"x :{x}, iterate: {it}")

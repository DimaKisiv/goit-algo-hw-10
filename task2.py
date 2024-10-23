import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
points = 1000  # Кількість випадкових точок

# Випадкові точки для методу Монте-Карло
x_rand = np.random.uniform(a, b, points)
y_rand = np.random.uniform(0, b**2, points)
y_f = f(x_rand)
points_grey_zone = y_rand < y_f
# Загальна площа прямокутника
area_rectangle = (b - a) * (b**2)
# Площа сірої зони під кривою
area_grey_zone = area_rectangle * np.mean(points_grey_zone)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))

# Додаємо точки: червоні поза зоною, сині ті, що входять
ax.scatter(x_rand[points_grey_zone == True], y_rand[points_grey_zone == True], color='b')
ax.scatter(x_rand[points_grey_zone == False], y_rand[points_grey_zone == False], color='r')

ax.text(-0.5, 5.8, f"Площа сірої зони Монте-Карло = {area_grey_zone:.3f}")

# Вираховуємо площу аналітично та порівнюємо з результатами методу Монте-Карло
area_quad, error = spi.quad(f, a, b)
ax.text(-0.5, 5.4, f"Площа сірої зони аналітично = {area_quad:.3f}")
ax.text(-0.5, 5.0, f"Похибка = {abs(area_grey_zone - area_quad):.3f}")


plt.grid()
plt.show()

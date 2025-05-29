import turtle
# import sys


def koch_curve(t, order, size):
    # 
    if order == 0:
        t.forward(size)
    else:
        for triangle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(triangle)

while True:
    try:
        d_order = int(input("👉 Введіть рівень рекурсії (ціле число): "))
        if d_order < 0:
            print("❗ Будь ласка, введіть невід’ємне число.")
        else:
            break
    except ValueError:
        print("❗ Помилка: потрібно ввести ціле число.")

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, 0)
    t.pendown()
    t.color("#3FACDF", "#1013f3")

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # koch_curve(t, order, size)

    window.mainloop()

# Виклик функції
draw_koch_curve(d_order)


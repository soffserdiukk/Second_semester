import math

class Shape:
    def validate_positive_sides(self, *sides):
        """Перевіряє, чи всі сторони додатні."""
        if any(side <= 0 for side in sides):
            raise ValueError("Усі сторони мають бути додатніми.")

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.validate_positive_sides(a, b, c)
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Трикутник з такими сторонами не існує.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle(Shape):
    def __init__(self, a, b):
        self.validate_positive_sides(a, b)
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b


class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        self.validate_positive_sides(a, b, c, d)
        self.a = a  # верхня основа
        self.b = b  # нижня основа
        self.c = c  # бічна сторона
        self.d = d  # інша бічна сторона

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        # Обчислення висоти трапеції
        if self.c <= (self.b - self.a) / 2:
            return 0  # або можна викинути виключення
        try:
            h = math.sqrt(self.c**2 - ((self.b - self.a) / 2)**2)
            return ((self.a + self.b) / 2) * h
        except ValueError:
            return 0  # Повертаємо 0, якщо обчислення не вдається


class Parallelogram(Shape):
    def __init__(self, a, b, height):
        self.validate_positive_sides(a, b, height)
        self.a = a
        self.b = b
        self.height = height

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.validate_positive_sides(radius)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


def read_shapes_from_file(filename):
    shapes = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue  # Пропустити порожні рядки
            shape_name = parts[0]
            try:
                params = list(map(float, parts[1:]))
                if shape_name == "Triangle":
                    shapes.append(Triangle(*params))
                elif shape_name == "Rectangle":
                    shapes.append(Rectangle(*params))
                elif shape_name == "Trapeze":
                    shapes.append(Trapeze(*params))
                elif shape_name == "Parallelogram":
                    shapes.append(Parallelogram(*params))
                elif shape_name == "Circle":
                    shapes.append(Circle(*params))
            except (ValueError, IndexError):
                continue  # Пропустити рядок з помилкою
    return shapes


def find_max_area_and_perimeter(shapes):
    if not shapes:
        return None, None  # Якщо немає допустимих фігур
    max_area_shape = max(shapes, key=lambda shape: shape.area())
    max_perimeter_shape = max(shapes, key=lambda shape: shape.perimeter())
    return max_area_shape, max_perimeter_shape


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    try:
        with open("output.txt", "w", encoding="utf-8") as output_file:
            for input_file in input_files:
                shapes = read_shapes_from_file(input_file)
                max_area_shape, max_perimeter_shape = find_max_area_and_perimeter(shapes)

                output_file.write(f"Файл: {input_file}\n")
                if max_area_shape:
                    output_file.write(f"Фігура з найбільшою площею: {type(max_area_shape).__name__}, Площа: {max_area_shape.area()}\n")
                else:
                    output_file.write("Не знайдено жодної допустимої фігури.\n")

                if max_perimeter_shape:
                    output_file.write(f"Фігура з найбільшим периметром: {type(max_perimeter_shape).__name__}, Периметр: {max_perimeter_shape.perimeter()}\n")
                else:
                    output_file.write("Не знайдено жодної допустимої фігури.\n")

                output_file.write("\n")
    except Exception as e:
        print(f"Помилка при запису у файл: {e}")


if __name__ == "__main__":
    main()
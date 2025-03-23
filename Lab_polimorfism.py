import math

# Base class "Shape"
class Shape:
    def dimension(self):
        raise NotImplementedError("Method 'dimension' is not implemented")

    def perimeter(self):
        raise NotImplementedError("Method 'perimeter' is not implemented")

    def area(self):
        raise NotImplementedError("Method 'area' is not implemented")

    def surface_area(self):
        raise NotImplementedError("Method 'surface_area' is not implemented")

    def base_area(self):
        raise NotImplementedError("Method 'base_area' is not implemented")

    def height(self):
        raise NotImplementedError("Method 'height' is not implemented")

    def volume(self):
        raise NotImplementedError("Method 'volume' is not implemented")

# Class "Triangle"
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def dimension(self):
        return 2  # 2D shape

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        # Heron's formula for the area of a triangle
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.side_a) *
            (semi_perimeter - self.side_b) *
            (semi_perimeter - self.side_c)
        )

    def volume(self):
        # For 2D shapes, volume equals area
        return self.area()

# Class "Rectangle"
class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def dimension(self):
        return 2  # 2D shape

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b

    def volume(self):
        # For 2D shapes, volume equals area
        return self.area()

# Class "Circle"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def dimension(self):
        return 2  # 2D shape

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def volume(self):
        # For 2D shapes, volume equals area
        return self.area()

# Class "Sphere"
class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def dimension(self):
        return 3  # 3D shape

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

# Function to find the shape with the largest measure
def find_largest_shape(shapes):
    largest_shape = None
    max_volume = -1

    for shape in shapes:
        vol = shape.volume()
        if vol > max_volume:
            max_volume = vol
            largest_shape = shape

    return largest_shape

# Function to read shapes from a file
def read_shapes_from_file(filename):
    shapes = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            shape_name = parts[0]
            params = list(map(float, parts[1:]))

            if shape_name == "Triangle":
                shapes.append(Triangle(*params))
            elif shape_name == "Rectangle":
                shapes.append(Rectangle(*params))
            elif shape_name == "Circle":
                shapes.append(Circle(*params))
            elif shape_name == "Sphere":
                shapes.append(Sphere(*params))
            # Add other shapes here (e.g., Trapeze, Parallelogram, etc.)

    return shapes

# Analyze multiple files
def analyze_files(file_names):
    all_shapes = []

    # Read shapes from each file and combine them into one list
    for file_name in file_names:
        try:
            shapes = read_shapes_from_file(file_name)
            all_shapes.extend(shapes)
            print(f"Прочитано {len(shapes)} фігур з файлу {file_name}")
        except FileNotFoundError:
            print(f"Файл {file_name} не знайдено.")
        except Exception as e:
            print(f"Помилка при читанні файлу {file_name}: {e}")

    # Find the largest shape among all shapes
    if all_shapes:
        largest_shape = find_largest_shape(all_shapes)
        print(f"Фігура з найбільшою мірою: {type(largest_shape).__name__}, міра: {largest_shape.volume()}")
    else:
        print("Фігури не знайдено в жодному з файлів.")

# List of files to analyze
file_names = ["input01.txt", "input02.txt", "input03.txt"]

# Analyze the files
analyze_files(file_names)
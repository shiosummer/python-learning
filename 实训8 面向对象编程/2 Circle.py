class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_perimeter(self):
        return 2*self.radius*3.14
    def get_area(self):
        return 3.14*self.radius**2

obj=Circle(4)
print(f'⚪的周长为:{obj.get_perimeter()}')
print(f'⚪的面积为:{obj.get_area()}')
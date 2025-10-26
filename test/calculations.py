import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def kinetic_energy(mass, velocity):
    if mass < 0 or velocity < 0:
        return 0
    return 0.5 * mass * (velocity ** 2)

def gravitational_potential_energy(mass, height, gravity=9.81):
    return mass * gravity * height

class GeometryCalculator:
    
    def __init__(self, precision=2):
        self.precision = precision
        self.pi = math.pi
    
    def circle_area(self, radius):
        if radius < 0:
            return 0
        area = self.pi * (radius ** 2)
        return round(area, self.precision)
    
    def rectangle_area(self, base, height):
        if base < 0 or height < 0:
            return 0
        area = base * height
        return round(area, self.precision)
    
    def triangle_area(self, base, height):
        area = 0.5 * base * height
        return round(area, self.precision)

class PersonalFinance:
    
    def simple_interest(self, principal, rate, time):
        if rate < 0:
            rate = 0
        amount = principal * (1 + rate * time)
        return amount
    
    def compound_interest(self, principal, rate, time):
        if rate < 0:
            rate = 0
        amount = principal * ((1 + rate) ** time)
        return amount

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list
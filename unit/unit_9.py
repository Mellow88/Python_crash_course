"""Класи"""

# NOTE: Створення та використанння класу
class Dog:
    """Проста спроба змоделювати собаку"""

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def sit(self):
        """Виконання команди 'Сидіти'."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Виконання команди 'Лежати'."""
        print(f"{self.name} rollled over!")

# NOTE: Створення екземпляру класу
my_dog = Dog('Jessi', 7)
print(f"{my_dog.name.title()} is my dogs")
print(f"My dog is {my_dog.age} years old")


my_dog.roll_over()
my_dog.sit()

class Car:
    """Моделювання класу 'Car'"""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів що описують клас"""
        self.make = make
        self.model = model
        self.year = year
        self.odometr = 0

    def get_name(self):
        """Return format car name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometr(self):
        """Read car odometr"""
        print(f"This car has {self.odometr} miles on it.")

    def update_odometr(self, miles):
        """Задання значення одометра"""
        if miles >= self.odometr:
            self.odometr = miles
        else:
            print('Can not roll back an odometr!')

    def increment_odometr(self, miles):
        """Додати задане значення до показника одометру"""
        if miles < 0:
            print('Can not roll back an odometr!')
        else:
            self.odometr += miles

new_car = Car('audi', 'a4', 2019)
new_car.get_name()

# NOTE: Зміна атрибута класу та його безпосереднє читання
new_car.odometr = 34
new_car.update_odometr(56)
new_car.increment_odometr(10)
new_car.read_odometr()

# NOTE: Успадкування класів
class ElectricCar(Car):
    """Моделювання класу ElectricCar."""

    def __init__(self, make, model, year):
        """Ініціалізація атрибутів що описують клас
           Тоді ініціалізація атрибутів електрокара
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_barttery(self):
        """Виведення повідомлення про розмір акумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery")

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.odometr = 200
print(my_tesla.get_name())
my_tesla.describe_barttery()

"""HW_9"""

class Restaurant:
    """Моделювання класу Restaurant."""

    def __init__(self, res_name, res_type):
        self.res_name = res_name
        self.res_type = res_type
        self.res_number_served = 0

    def describe_restaurant(self):
        """Опис найменування та типу ресторану"""
        print(f"Welcome to our restaurant - {self.res_name.title()}!")
        print(f"Type {self.res_type} ")

    def read_number_served(self):
        """Виведення кількості наявних місць"""
        print(f"Number served = {self.res_number_served}")

    def open_restaurant(self):
        """Перевірка чи ресторан відкрито"""
        print(f"The restaurant {self.res_name.title()} is open!")

    def set_number_served(self, number):
        """Зміна значення кількості місць"""
        self.res_number_served = number

    def increment_number_served(self, number):
        """Збільшення кількості місць"""
        self.res_number_served += number

res = Restaurant('Good morning', 'small')

print(res.res_name)
print(res.res_type)

res.describe_restaurant()
res.read_number_served()
res.open_restaurant()

res.res_number_served = 100
res.read_number_served()

res.set_number_served(200)
res.read_number_served()

res.increment_number_served(30)
res.read_number_served()

res_list = []
res_list.append({'r_name': 'Fredis', 'r_type': 'small'})
res_list.append({'r_name': 'Wood', 'r_type': 'big'})
res_list.append({'r_name': 'Star', 'r_type': 'small'})

for i in res_list:
    new_rest = Restaurant(i['r_name'], i['r_type'])
    print(new_rest.res_name)
    print(new_rest.res_type)


class User:
    """Моделювання класу User."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Опис найменування та типу user"""
        print(f"First name - {self.first_name.title()}")
        print(f"Last name - {self.last_name.title()} ")
        print(f"Login attempts = {self.login_attempts} ")

    def greet_user(self):
        """Привітання user"""
        print(f"Hello friend - {self.first_name.title()}")

    def increment_login_attemts(self):
        """Збільшення кількості спроб авторизації"""
        self.login_attempts += 1

    def reset_login_attemts(self):
        """Обнулення кількості спроб авторизації"""
        self.login_attempts = 0


user_i = User('ihor', 'sereda')
user_i.increment_login_attemts()
user_i.describe_user()
user_i.greet_user()

user_i.reset_login_attemts()
user_i.describe_user()

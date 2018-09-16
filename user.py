class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name2 = first_name
        self.last_name2 = last_name
        self.age2 = age
        self.country2 = country

    def describe_user(self):
        print("Hello," + self.first_name2.title() + self.last_name2.title() + " ,")

users = User("li", "zhixin", 18, "china")
users.describe_user()



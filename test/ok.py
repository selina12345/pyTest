class Privilegs():
    def __init__(self):
        self.privilegs2 = ["can add post", "can delete post", "can ban user"]

    def show_privilegs(self):
        print("If you are an administrator account, you can have the following permissions: ")
        for privileg in self.privilegs2:
            print(privileg)


class Admin():
    def __init__(self):
        self.privilegs2 = Privilegs()

    def show_privilegs2(self, test):
        self.privilegs2.show_privilegs()
        print(test)
        print("If you are an administrator account, you can have the following permissions: ")


class Admin2():
    def __init__(self, privilegs):
        self.privilegs = Privilegs(privilegs)

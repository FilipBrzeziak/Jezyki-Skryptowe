import User


class Service:
    def __init__(self, operations):
        self._users = []
        self._operations = operations
        self._nick = "visitor"

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, value):
        self._users = value

    @property
    def operations(self):
        return self._operations

    @operations.setter
    def operations(self, value):
        self._operations = value

    @property
    def nick(self):
        return self._nick

    @nick.setter
    def nick(self, value):
        self._nick = value

    def add_default_values(self):
        self.operations.add_discount("Laundry machine", 12.2, 20, "Media expert", "23.4.2022",
                                     "Best on the market", "DiscRider")
        self.operations.add_discount("Laundry robot", 8.4, 20, "Media Markt", "22.1.2022",
                                     "Nice tool", "Go12")
        self.operations.add_discount("Laundry Smart T", 16.2, 20, "Allegro.pl", "3.06.2021"
                                     , "Easy to use", "Filip123")
        self.operations.add_discount("OLED Smart TV", 14, 25, "Neonet", "03.01.2022",
                                     "Worth considering", "YoungRedNeck123")
        self.operations.add_discount("Smartphone Redmi 9", 599, 1199, "Neonet", "01.06.2022",
                                     "Best xiaomi up to 1000", "Filip123")
        self.operations.add_discount("Smartphone Samsung", 799, 899, "Electro.pl", "31.03.2022",
                                     "64MP camera for 799zl", "Simplyfy@")
        self.operations.add_discount("Huwawei Smartphone", 1024, 1599, "telefony.pl", "01.05.2022",
                                     "good phone without android", "Filip123")
        self.operations.add_discount("Smartphone Redmi 9", 719, 1199, "Media.pl", "01.03.2022",
                                     "Good guarantee", "Kapix")
        self.operations.add_discount("Smartphone Redmi 9", 699, 1199, "Saturn", "20.01.2022",
                                     "From tv ad", "Baczynski")
        self._users.append(User.User("Filip123", "Filip123@gmail.com", "123"))
        self._users.append(User.User("1", "jke@gmail.com", "1"))

    def start_service_for_registred_user(self, nickname):
        print("DISCOUNTER APP VERSION 1.0.0\n")
        action = -1

        while action != 0:
            if action == 1:
                print("|Actual discounts|")
                print(self.operations.show_discounts())
            if action == 2:
                print("|Creating new discount|")
                self.operations.add_discount_input(nickname)
            if action == 3:
                print("|Finding discount by product name|")
                name = input("Input product  name or phrase: ")
                print(self.operations.find_discounts_name(name))
            if action == 4:
                print("|Finding discount by product name and price|")
                name = input("Input product  name or phrase")
                price_min = input("Input minimal price: ")
                price_max = input("Input maximal price: ")
                self.operations.find_discounts_price(name, price_min, price_max)
            if action == 5:
                print("|Finding discount by name and minimal discount|")
                name = input("Input product name or phrase: ")
                discount = input("Input minimal discount: ")
                self.operations.find_discounts_discount(name, discount)
            if action == 6:
                print("|Find discounts added by specific user|")
                nickname = input("Input nickname: ")
                self.operations.find_discounts_nickname(nickname)
            if action == 7:
                print("|Show average prices for specific product|")
                name = input("Input product name: ")
                self.operations.check_average_price(name)
            if action == 8:
                print("|Show prices for specific product over time|")
                name = input("Input product name: ")
                self.operations.show_previous_prices(name)
            if action == 9:
                self.choose_version()
                return
            if action == 0:
                print("Bye!")

            action = float(input("Select action:\n1 - Show actual discounts"
                                 "\n2 - Add new discount"
                                 "\n3 - Find discount by product name"
                                 "\n4 - Find discount by product name and price"
                                 "\n5 - Find discount by name and minimal discount"
                                 "\n6 - Find discounts added by specific user"
                                 "\n7 - Show average prices for specific product"
                                 "\n8 - Show prices for specific product over time"
                                 "\n9 - Logout"
                                 "\n0 - Exit"
                                 "\nChoice: "))

        print("Filip corp. All rights reserved")

    def start_service_for_visitor(self):
        print("DISCOUNTER APP VERSION 1.0.0\n")
        action = -1

        while action != 0:
            if action == 1:
                print("|Actual discounts|")
                print(self.operations.show_discounts())
            if action == 2:
                print("|Finding discount by product name|")
                name = input("Input product  name or phrase: ")
                self.operations.find_discounts_name(name)
            if action == 3:
                print("|Finding discount by product name and price|")
                name = input("Input product  name or phrase")
                price_min = input("Input minimal price: ")
                price_max = input("Input maximal price: ")
                self.operations.find_discounts_price(name, price_min, price_max)
            if action == 4:
                self.choose_version()
                return
            if action == 0:
                print("Bye!")

            action = float(input("Select action:\n1 - Show actual discounts"
                                 "\n2 - Find discount by product name"
                                 "\n3 - Find discount by product name and price"
                                 "\n4 - Log in/Register"
                                 "\n0 - Exit"
                                 "\nChoice: "))

        print("Filip corp. All rights reserved")

    def register_user(self):
        print("Registration\n")
        nickname = input("Input nickname: ")
        email = input("Input email: ")
        password = input("Input password: ")
        exists = False
        for x in self.users:
            if str(x.nick).__eq__(nickname):
                exists = True

        if not exists:
            user = User.User(nickname, email, password)
            self._users.append(user)
            print("Logged as a " + nickname)
            self._nick = nickname
            return True
        else:
            print("User already exists!")
            return False

    def login(self):
        print("Log in\n")
        nickname = input("Input nickname: ")
        password = input("Input password: ")
        accepted = False
        for x in self.users:
            if str(x.nick).__eq__(nickname):
                if str(x.password).__eq__(password):
                    accepted = True
        if not accepted:
            print("Wrong nick or password!")
            return False
        else:
            print("Hello " + nickname + "!")
            self._nick = nickname
            return True

    def choose_version(self):
        print("Welcome in Discounter!")
        action = float(input("Choose option:\n1 - Login for more options"
                             "\n2 - Just a visitor"
                             "\n3 - Register and become a part of Discounter!"
                             "\nChoice: "))
        if action == 1:
            if self.login():
                self.start_service_for_registred_user(self.nick)
            else:
                self.choose_version()
                return

        elif action == 2:
            self.start_service_for_visitor()

        elif action == 3:
            if self.register_user():
                self.start_service_for_registred_user(self.nick)
            else:
                self.choose_version()
                return

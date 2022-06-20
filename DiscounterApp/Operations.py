import unittest

import matplotlib.pyplot as plt
import datetime
from Discount import Discount


class Operations:
    def __init__(self):
        self._number = None
        self.discounts = []

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def add_discount(self, name, discount_price, normal_price, shop_name, date, comment, discounter_nick):
        self.discounts.append(Discount(name,
                                       discount_price,
                                       normal_price,
                                       shop_name,
                                       date,
                                       comment,
                                       discounter_nick))

    def add_discount_input(self, nickname):
        name = input("Input name: ")
        discount_price = input("Input discount price: ")
        normal_price = input("Input normal price: ")
        shop_name = input("Input shop name: ")
        date = input("Input valid to date: ")
        comment = input("Input comment: ")
        discounter_nick = nickname
        self.discounts.append(Discount(name,
                                       discount_price,
                                       normal_price,
                                       shop_name,
                                       date,
                                       comment,
                                       discounter_nick))

    def show_discounts(self):
        print("\nProduct name".ljust(30) + '\t' + "Discount price".ljust(20) + '\t' + "Normal price".ljust(
            20) + '\t' + "Discount".ljust(20) + '\t' + "Shop name".ljust(20) + '\t' + "Date".ljust(
            20) + '\t' + "Comment".ljust(
            30) + '\t' + "Discounter nick".ljust(20) + '\n')
        if len(self.discounts) == 0:
            print("No discounts yet!")
        else:
            for i in self.discounts:
                print(i)

    def find_discounts_name(self, name):
        result = []
        if len(self.discounts) == 0:
            print("No discounts yet!")
        else:
            print("Results:")
            for Discount in self.discounts:
                if Discount.name is name or str(Discount.name).lower().__contains__(str(name).lower()):
                    print(Discount)
                    result.append(Discount)

        return result

    def find_discounts_price(self, name, price_min, price_max):
        result = []
        if len(self.discounts) == 0:
            print("No discounts yet!")
        else:
            print("Results:")
            for x in self.discounts:
                if x.name is name or str(x.name).__contains__(name):
                    if float(price_min) < x.discount_price < float(price_max):
                        print(x)
                        result.append(x)
        return result

    def find_discounts_discount(self, name, discount_min):
        result = []
        if len(self.discounts) == 0:
            print("No discounts yet!")
        else:
            print("Results:")
            for x in self.discounts:
                if x.name is name or str(x.name).__contains__(name):
                    if float(x.disc) >= float(discount_min):
                        print(x)
                        result.append(x)
        return result

    def find_discounts_nickname(self, nickname):
        result = []
        if len(self.discounts) == 0:
            print("No discounts yet!")
        else:
            print("Results:")
            for x in self.discounts:
                if x.discounter_nick is nickname or str(x.discounter_nick).lower().__contains__(str(nickname).lower()):
                    print(x)
                    result.append(x)
        return result

    def check_average_price(self, name):
        sum = 0
        i = 0
        if len(self.discounts) == 0:
            print("No discounts yet!")
        else:
            for x in self.discounts:
                if x.name is name or str(x.name).__contains__(name):
                    sum = sum + float(x.discount_price)
                    i = i + 1
        if i != 0:
            print("%.2f" % (sum / i) + "zl")
            return "%.2f" % (sum / i) + "zl"
        else:
            print("No products find!")

    def show_previous_prices(self, productName):
        dates = []
        prices = []
        data = self.find_discounts_name(productName)

        for Discount in data:
            prices.append(Discount.discount_price)

        for Discount in data:
            date_split = str.split(Discount.date, ".")
            dates.append(datetime.date(int(date_split[2]), int(date_split[1]), int(date_split[0])))

        plt.bar(dates, prices, color='red', width=10)
        plt.xlabel("Date")
        plt.ylabel("Price [PLN]")
        plt.title(productName + " prices over time", fontsize=15)
        plt.show()

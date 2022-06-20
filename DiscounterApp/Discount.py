class Discount:
    def __init__(self, name, discount_price, normal_price, shop_name, date, comment, discounter_nick):
        self.name = name
        self.discount_price = discount_price
        self.normal_price = normal_price
        self.shop_name = shop_name
        self.date = date
        self.comment = comment
        self.discounter_nick = discounter_nick
        self.disc = (1 - (float(discount_price) / float(normal_price))) * 100

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def discount_price(self):
        return self._discount_price

    @discount_price.setter
    def discount_price(self, value):
        self._discount_price = value

    @property
    def normal_price(self):
        return self._normal_price

    @normal_price.setter
    def normal_price(self, value):
        self._normal_price = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    def __str__(self) -> str:
        return self._name.ljust(30) + '\t' + str(self._discount_price).ljust(20) + '\t' + str(self._normal_price).ljust(
            20) + '\t' + str(str("%.2f" % self.disc) + '%').ljust(20) + '\t' + self.shop_name.ljust(20) + '\t' + str(
            self._date).ljust(20) + '\t' + self._comment.ljust(30) + '\t' + self._discounter_nick.ljust(20)

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value

    @property
    def discounter_nick(self):
        return self._discounter_nick

    @discounter_nick.setter
    def discounter_nick(self, value):
        self._discounter_nick = value

    def to_dict(self):
        date_split = str.split(self.date, ".")
        return {

            'Product name': self.name,
            'Year': date_split[2],
            'Month': date_split[1],
            'Day': date_split[0],
            'Discount price': self.discount_price,
        }

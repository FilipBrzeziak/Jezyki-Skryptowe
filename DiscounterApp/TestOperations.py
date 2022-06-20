import unittest
from App import Operations, Discount, User


class TestOperations(unittest.TestCase):

    def test_add_discount(self):
        operations = Operations.Operations()
        operations.add_discount("1", 1, 2, "1", "1", "1", "1")
        self.assertTrue(len(operations.discounts) != 0)

    def test_find_discounts(self):
        operations = Operations.Operations()
        operations.add_discount("1", 1, 2, "1", "1", "1", "1")
        self.assertTrue(str(operations.find_discounts_name("1")[0]).__eq__(
            "1                             	"
            "1                   	2                   	"
            "50.00%              	1                   	1                   	"
            "1                             	1                   "))

    def test_average_price(self):
        operations = Operations.Operations()
        operations.add_discount("1", 1, 2, "1", "1", "1", "1")
        operations.add_discount("1 and 1", 2, 4, "2", "2", "2", "2")

        self.assertTrue(operations.check_average_price("1").__eq__("1.50zl"))

    def test_find_by_discount(self):
        operations = Operations.Operations()
        operations.add_discount("1", 1, 2, "1", "1", "1", "1")
        operations.add_discount("1 and 1", 2, 3, "2", "2", "2", "2")
        self.assertTrue(str(operations.find_discounts_discount("1", 40)[0]).__eq__(
            "1                             	"
            "1                   	2                   	"
            "50.00%              	1                   	1                   	"
            "1                             	1                   "))

    def test_find_discounts_nickname(self):
        operations = Operations.Operations()
        operations.add_discount("1", 1, 2, "1", "1", "1", "MArio")
        operations.add_discount("1 and 1", 2, 3, "2", "2", "2", "2")
        self.assertTrue(str(operations.find_discounts_nickname("MArio")[0]).__eq__(
            "1                             	"
            "1                   	2                   	"
            "50.00%              	1                   	1                   	"
            "1                             	MArio               "))


if __name__ == '__main__':
    unittest.main()

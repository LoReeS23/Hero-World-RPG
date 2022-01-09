class NumberFormat:
    def __init__(self, number):
        """

        :param number: number given by user
        """
        self.number = number

    def multiplier(self, multiply_value):
        return self.number * multiply_value

    def divider(self, divide_value):
        return self.number / divide_value

    def is_divisible_by(self, number):
        return self.number % number == 0

    def to_the_power_of(self, number):
        return self.number ** number


# a = NumberFormat(4)
# print(a.divider(2))
# print(a.multiplier(4))
# print(a.is_divisible_by(2))
# print(a.to_the_power_of(5))

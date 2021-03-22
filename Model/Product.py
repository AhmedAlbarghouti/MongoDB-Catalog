import uuid
"""
By Ahmed Albarghouti
22/3/2021
"""

class Product:
    def __init__(self, name, brand, price, description, category):
        """
        :param name:
        :param brand:
        :param price:
        :param description:
        :param category:
        """
        self.id = uuid.uuid4()
        self.name = name
        self.brand = brand
        self.price = price
        self.description = description
        self.category = category

    @property
    def id(self):
        """
        :return id:
        """
        return self.id

    @property
    def name(self):
        """
        :return name:
        """
        return self.name

    @name.setter
    def name(self, value):
        """
        :param value:
        :return:
        """
        self.name = value

    @property
    def brand(self):
        """
        :return brand:
        """
        return self.brand

    @brand.setter
    def brand(self, value):
        """
        :param value:
        :return:
        """
        self.brand = value

    @property
    def price(self):
        """
        :return price:
        """
        return self.price

    @price.setter
    def price(self, value):
        """
        :param value:
        :return:
        """
        self.price = value

    @property
    def description(self):
        """
        :return description:
        """
        return self.description

    @description.setter
    def description(self, value):
        """
        :param value:
        :return:
        """
        self.description = value

    @property
    def category(self):
        """
        :return category:
        """
        return self.category

    @category.setter
    def category(self, value):
        """
        :param value:
        :return:
        """
        self.category = value

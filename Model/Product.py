import uuid

"""
By Ahmed Albarghouti
22/3/2021
"""


class Product:
    def __init__(self, name, brand, price, description, category, subCategory):
        """
        :param name:
        :param brand:
        :param price:
        :param description:
        :param category:
        :param subCategory:
        """
        self._id = uuid.uuid4().__str__()
        self._name = name
        self._brand = brand
        self._price = price
        self._description = description
        self._category = category
        self._subCategory = subCategory

    @property
    def id(self):
        """
        :return id:
        """
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        """
        :return name:
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        :param value:
        :return:
        """
        self._name = value

    @property
    def brand(self):
        """
        :return brand:
        """
        return self._brand

    @brand.setter
    def brand(self, value):
        """
        :param value:
        :return:
        """
        self._brand = value

    @property
    def price(self):
        """
        :return price:
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        :param value:
        :return:
        """
        self._price = value

    @property
    def description(self):
        """
        :return description:
        """
        return self._description

    @description.setter
    def description(self, value):
        """
        :param value:
        :return:
        """
        self._description = value

    @property
    def category(self):
        """
        :return category:
        """
        return self._category

    @category.setter
    def category(self, value):
        """
        :param value:
        :return:
        """
        self._category = value

    @property
    def subCategory(self):
        """
        :return subCategory:
        """
        return self._subCategory

    @subCategory.setter
    def subCategory(self, value):
        """
        :param value:
        :return:
        """
        self._subCategory = value

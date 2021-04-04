from pymongo import MongoClient

from Model.Product import Product

cluster = MongoClient(
    "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
db = cluster['catalog']

prod_collection = db['Product']


class CatalogDAO:


    def getAllCategories(self):
        """Returns a dict object containing all the categories in every product"""
        return prod_collection.find({}, {"Category"})

    def getAllSubCategoriesFromCategory(self, category):
        """Returns a dict object containing all the sub-category in a specific category"""
        return prod_collection.find({"Category": category}, {"Sub-Category"})

    def getAllProductsFromSubCategory(self, subcategory):
        """Returns a dict object containing all the products in a specific subcategory"""
        return prod_collection.find({"Sub-Category": subcategory})

    def addProduct(self, product_name, brand, price_cad, product_description, category, sub_cat):
        """Inserts a new product into the Product collection"""
        prod = Product(product_name, brand, price_cad, product_description, category, sub_cat)

        return prod_collection.insert_one({"_id": prod.id, "Name": prod.name, "Brand": prod.brand, "Price": prod.price,
                                           "Description:": prod.description, "Sub-Category": prod.subCategory,
                                           "Category": prod.category})

    def deleteProduct(self, product_id):
        """Deletes a product with a specific ID"""
        return prod_collection.find_one_and_delete({"_id": product_id})

    def deleteAll(self):
        """Deletes all of the documents/products"""
        return prod_collection.delete_many({})


# c = CatalogDAO()
# # c.addProduct("Cherry Cake", "Kinder", 50, "Cake", "Food", "Pastry")
# # c.getAllSubCategoriesFromCategory("Electronics")
# # c.getAllProductsFromSubCategory("Mobiles")
# c.deleteAll()

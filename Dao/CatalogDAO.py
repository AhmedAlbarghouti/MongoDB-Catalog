from bson import ObjectId
from flask import request
from pymongo import MongoClient

from Model.Product import Product

try:
    cluster = MongoClient(
        "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
    db = cluster['catalog']
    prod_collection = db['Product']
    cate_collection = db['Category']
except:
    print("ERROR - Cannot connect to db")


class CatalogDAO:

    def getAllCategories(self):
        """Returns a dict object containing all the categories in every product"""
        return cate_collection.find({})

    def getAllSubCategoriesFromCategory(self, category):
        """Returns a dict object containing all the sub-category in a specific category"""
        return prod_collection.find({"Category": category}, {"Sub-Category"})

    def getAllProductsFromSubCategory(self, subcategory):
        """Returns a dict object containing all the products in a specific subcategory"""
        return prod_collection.find({"Sub-Category": subcategory})

    def getAllProducts(self):
        return prod_collection.find({})

    def getProductWithId(self, id):
        return prod_collection.find_one({'_id': id})

    def addProduct(self, product_name, brand, price_cad, product_description, category, sub_cat):
        """Inserts a new product into the Product collection"""
        prod = Product(product_name, brand, price_cad, product_description, category, sub_cat)

        return prod_collection.insert_one({"_id": prod.id, "Name": prod.name, "Brand": prod.brand, "Price": prod.price,
                                           "Description:": prod.description, "Sub-Category": prod.subCategory,
                                           "Category": prod.category})

    def editProduct(self,id):
        prod_collection.update_one(
            {"_id": id},
            {"$set":
                {
                    "name": request.form["name"],
                    "brand": request.form["brand"],
                    "price": request.form["price"],
                    "description": request.form["description"],
                    "category": request.form["category"]
                }
            }
        )

    def deleteProduct(self, product_id):
        """Deletes a product with a specific ID"""
        return prod_collection.find_one_and_delete({"_id": product_id})

    def deleteAll(self):
        """Deletes all of the documents/products"""
        return prod_collection.delete_many({})


# c = CatalogDAO()
# c.addProduct("Iphone 7", "Apple", 500, "Smart Phone", "Electronics", "Mobiles")
# # c.getAllSubCategoriesFromCategory("Electronics")
# # c.getAllProductsFromSubCategory("Mobiles")
# c.deleteAll()

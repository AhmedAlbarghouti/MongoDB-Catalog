from bson import ObjectId
from pymongo import MongoClient
from Model.Product import Product

"""
By Rita Busygina
29/3/2021
"""

# Connecting to the database & collections with try catch
try:
    cluster = MongoClient(
        "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
    db = cluster['catalog']
    prod_collection = db['Product']
    cate_collection = db['Category']
except:
    print("ERROR - Cannot connect to db")

# Class in charge of accessing the remote database
class CatalogDAO:

    def getAllProducts(self):
        """returns result of all products within the Product collection"""
        return prod_collection.find({})

    def getProduct(self, id):
        """returns result of a single product with a specific unique id"""
        return prod_collection.find_one({'_id': ObjectId(id)})

    def addProduct(self, prod):
        """returns result of inserting one new product into the product collection"""
        return prod_collection.insert_one(prod)

    def editProduct(self, id, name, brand, price, description, category):
        """returns result of updating a products fields with a specific unique id"""
        return prod_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set":
                {
                    "name": name,
                    "brand": brand,
                    "price": price,
                    "description": description,
                    "category": category
                }
            }
        )

    def deleteProduct(self, product_id):
        """:returns the result of deleting a product with a specific unique id"""
        return prod_collection.find_one_and_delete({"_id": ObjectId(product_id)})

    # New Functions
    def addCategory(self, category_name):
        """returns result of inserting a new Category into the Category collection"""
        return cate_collection.insert_one({"Category_Name": category_name})

    def getAllCategories(self):
        """Returns result of all Categories within the Category collection"""
        return cate_collection.find()

    def getCategoryProducts(self, category):
        """Returns result of all products with a specific Category_Name"""
        return prod_collection.find({'category': category})

    def deleteCategory(self, cate_name):
        """:return result of deleting a category with a specific name"""
        return cate_collection.delete_one({"Category_Name": cate_name})

    def deleteAll(self):
        """:returns result of deleting all products in the product collection"""
        return prod_collection.delete_many({})

from bson import ObjectId
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

    def getAllProducts(self):
        return prod_collection.find({})

    def getProduct(self, id):
        return prod_collection.find_one({'_id': ObjectId(id)})

    def addProduct(self, prod):
        return prod_collection.insert_one(prod)

    def editProduct(self,id,name,brand,price,description,category):
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
        return prod_collection.find_one_and_delete({"_id": ObjectId(product_id)})

    # New Functions
    def addCategory(self, category_name):
        return cate_collection.insert_one({"Category_Name": category_name})

    def getAllCategories(self):
        return cate_collection.find()

    def getCategoryProducts(self,category):
        return prod_collection.find({'category': category})

    def deleteCategory(self, cate_name):
        return cate_collection.delete_one({"Category_Name": cate_name})

    def deleteAll(self):
        return prod_collection.delete_many({})

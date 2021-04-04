from pymongo import MongoClient

from Model.Product import Product

cluster = MongoClient(
    "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
db = cluster['catalog']
prod_collection = db['Product']
cate_collection = db['Category']


class CatalogDAO:

    def getAllProducts(self):
        return prod_collection.find()

    def addProduct(self, product_name, brand, price_cad, product_description, category):
        prod = Product(product_name, brand, price_cad, product_description, category)
        # new_product=({prod})
        return prod_collection.insert_one(
            {"_id": prod.id.__str__(), "name": prod.name, "brand": prod.brand, "price": prod.price,
             "description:": prod.description,
             "category": prod.category})

    def deleteProduct(self, product_id):
        return prod_collection.find_one_and_delete({"_id": product_id})

    #New Functions
    def addCategory(self, category_name):
        return cate_collection.insert_one({"Category_Name": category_name})

    def getAllCategories(self):
        return cate_collection.find()

    def deleteCategory(self, cate_name):
        return cate_collection.find_one_and_delete({"Category_Name": cate_name})


    def deleteAll(self):
        return prod_collection.delete_many({})


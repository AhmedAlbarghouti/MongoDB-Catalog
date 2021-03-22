from pymongo import MongoClient

class CatalogDAO:
    pass

cluster = MongoClient(
    "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
db = cluster['catalog']
prod_collection = db['Product']
cate_collection = db['Category']

def getAllProducts():
   return prod_collection.find()

def addProduct(product_id, product_name,brand,price_cad,product_description, category):
    new_product={{"_id": product_id, "name": product_name, "brand": brand,  "price": price_cad,"description": product_description, "category": category}}
    return prod_collection.insert_one(new_product)

def deleteProduct(product_id, product_name):
    prod_to_delete = prod_collection.find({"_id":product_id, "name": product_name})
    return prod_collection.remove(prod_to_delete)






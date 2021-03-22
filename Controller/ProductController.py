# from pymongo import MongoClient
#
# cluster = MongoClient(
#     "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
# db = cluster['catalog']
# prod_collection = db['Product']
# cate_collection = db['Category']
#
# prod_post = {"_id": 0, "name": "blueberry cake", "description": "its a cake that has blueberry", "price": 5, "category": "Pastry"}
# cate_post = {"_id": 0, "name": "Pastry"}
#
# prod_collection.insert_one(prod_post)
# cate_collection.insert_one(cate_post)
from Dao.CatalogDAO import CatalogDAO



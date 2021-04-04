from pymongo import MongoClient

from Model.Product import Product

cluster = MongoClient(
    "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
db = cluster['catalog']

cate_collection = db['Category']


class CatalogDAO:

    def getAllCategories(self):
        categories = []
        for cat in cate_collection.find({}, {"Category_Name"}):
            categories.append(cat)

        return categories

    def getAllSubCategoriesFromCategory(self, category):
        return cate_collection.find({'Category_Name': category}, {"Mini_Categories.Mini_Cat_Name"})

    def getAllProductsFromSubCategory(self, subcategory):
        return cate_collection.find({"Mini_Categories.Mini_Cat_Name": subcategory})
            # for a in cate_collection.find({}, {"Category_Name":0, "Mini_Id": 0, "_id":0}):


    def addProduct(self, product_name, brand, price_cad, product_description, sub_cat, category):
       prod = Product(product_name, brand, price_cad, product_description, sub_cat, category)
       # new_product=({prod})
       return cate_collection.insert_one({"_id":prod.id, "name":prod.name, "brand":prod.brand, "price": prod.price, "description:":prod.description, "sub":prod.subCategory,
                                            "category":prod.category})

    def deleteProduct(product_id):
        return cate_collection.find_one_and_delete({"_id": product_id})

    def deleteAll(self):
        return cate_collection.delete_many({})


c = CatalogDAO()
c.addProduct( "Samsung Galaxy A71", "Sansung", 500, "Android Phone", "Phones", "Electronics")

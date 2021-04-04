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

    def getAllSubCategories(self):
        subCategories = []
        for subCat in cate_collection.find({}, {'_id': False, "Mini_Categories.Mini_Cat_Name": True}):
            subCategories.append(subCat)
        return subCategories

    def getAllSubCategoriesFromCategory(self, category):
        subCategories = []
        # '_id': False, "Mini_Categories.Mini_Cat_Name": True,
        for cat in cate_collection.find(
                                        {'Category_Name': 'Food'}):
            for subCat in cate_collection.find({}, {'_id': False,  "Mini_Categories.Mini_Cat_Name": True}):
             subCategories.append(cat)

        for row in subCategories:
            print(row)

    # def getAllProductsFromSubCategory(self, subcategory):
    #    products=[]
    #    for subCat in cate_collection

    # def addProduct(self, product_name, brand, price_cad, product_description, category):
    #     prod = Product(product_name, brand, price_cad, product_description, category)
    #     # new_product=({prod})
    #     return prod_collection.insert_one({"_id":prod.id.__str__(), "name":prod.name, "brand":prod.brand, "price": prod.price, "description:":prod.description,
    #                                        "category":prod.category})
    #
    # def deleteProduct(product_id):
    #     return prod_collection.find_one_and_delete({"_id": product_id})
    #
    # def deleteAll(self):
    #     return prod_collection.delete_many({})


c = CatalogDAO()
c.getAllSubCategoriesFromCategory("Food")

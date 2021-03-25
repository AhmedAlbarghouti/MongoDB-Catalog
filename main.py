
from flask import Flask, Response, request, render_template, redirect
from pymongo import MongoClient
import json
from bson import ObjectId

from Model.Product import Product

app = Flask(__name__)


try: 
    cluster = MongoClient(
        "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
    db = cluster['catalog']
    prod_collection = db['Product']
    cate_collection = db['Category']

except:
    print("ERROR - Cannot connect to db")
    
    
#====================================
# GET ADD VIEW (VIEW CONTROLLER)
@app.route("/add", methods=["GET"])
def getAddView():
    return render_template("add.html")

#====================================
# GET ALL PRODUCTS (PRODUCT CONTROLLER) & GET ALL VIEW (VIEW CONTROLLER)
@app.route("/", methods=["GET"])
@app.route("/products", methods=["GET"])
def getAllProducts():
    try:
        data = list(db.Product.find({}))
        for product in data:
            product["_id"] = str(product["_id"])
        return render_template("index.html", products=data)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get products"}),
            status=400,
            mimetype='application/json'
        )
      
      
#====================================
# ADD ONE PRODUCT (PRODUCT CONTROLLER)
@app.route("/products", methods=["POST"])
def addProduct():
    try:
        product = {
            "name":request.form["product_name"], 
            "brand":request.form["brand"],
            "price":request.form["price_cad"],
            "description":request.form["product_description"],
            "category":request.form["category"],
        }
        dbResponse = db.Product.insert_one(product)
        print(dbResponse.inserted_id)
        return redirect('/')
    except Exception as ex:
        print(ex)


#====================================
# EDIT ONE PRODUCT (PRODUCT CONTROLLER)
@app.route("/products/<id>", methods=["PATCH"])
def editProduct(id):
    try:
        dbResponse = db.Product.update_one(
            {"_id": ObjectId(id)},
            {"$set":
                {
                    "name": request.form["product_name"],
                    "brand": request.form["brand"],
                    "price": request.form["price_cad"],
                    "description": request.form["product_description"],
                    "category": request.form["category"]
                }
            }
        )
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps({"message": "product was updated successfully!"}),
                status=200,
                mimetype='application/json'
            )
        else: 
            return Response(
                response=json.dumps({"message": "nothing to update"}),
                status=200,
                mimetype='application/json'
            )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "Error: Cannot update product"}),
            status=400,
            mimetype='application/json'
        )


# #====================================
# DELETE ONE PRODUCT (PRODUCT CONTROLLER)
@app.route("/products/<id>", methods=["DELETE"])
def deleteProduct(id):
    try:
        dbResponse = db.Product.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            return Response(
                response=json.dumps({"message": "product was deleted successfully"}),
                status=200,
                mimetype='application/json'
            )
        return Response(
            response=json.dumps({
                "message": "product not found", 
                # "id": f"{id}"
            }),
            status=200,
            mimetype='application/json'
        )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "Error: Cannot delete product"}),
            status=400,
            mimetype='application/json'
        )


# #====================================
# DELETE ALL PRODUCTS (PRODUCT CONTROLLER)
@app.route("/products", methods=["DELETE"])
def deleteAllProducts():
    try:
        db.Product.delete_many({})
        return Response(
            response=json.dumps({"message": "products were deleted successfully!"}),
            status=200,
            mimetype='application/json'
        )    
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "Error: cannot delete products"}),
            status=400,
            mimetype='application/json'
        )
        

#====================================
if __name__ == "__main__":
    app.run(port=5000, debug=True)
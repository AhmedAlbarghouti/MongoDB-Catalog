from flask import Flask, Response, request, render_template, redirect, url_for, flash
from pymongo import MongoClient
import json
from bson import ObjectId

from Dao.CatalogDAO import CatalogDAO
from Model.Product import Product
from View.forms import AddForm, AddCategoryForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '9be304c55f10cb66f6e0e148348d1012'

try:
    cluster = MongoClient(
        "mongodb+srv://CST8276:Algonquin2021@cluster0.n9qal.mongodb.net/catalog?retryWrites=true&w=majority")
    db = cluster['catalog']
    prod_collection = db['Product']
    cate_collection = db['Category']

except:
    print("ERROR - Cannot connect to db")

categories = ['Home', 'Electronics', 'Sporting Goods']
c = CatalogDAO()


@app.context_processor
def inject_categories():
    return dict(categories=categories)


# ====================================
# GET ADD VIEW (VIEW CONTROLLER)
@app.route("/add", methods=["GET"])
def getAddView():
    form = AddForm()
    form.category.choices = categories
    if form.validate_on_submit():
        flash(f' {form.name.data} has been added to the catalog', 'success')
        return redirect(url_for('index.html'))
    return render_template("add.html", form=form, title='Add')


# ====================================
# GET ALL PRODUCTS (PRODUCT CONTROLLER) & GET ALL VIEW (VIEW CONTROLLER)
@app.route("/", methods=["GET"])
@app.route("/products", methods=["GET"])
def getAllProducts():
    try:
        data = list(c.getAllProducts())
        for product in data:
            product["_id"] = str(product["_id"])
            print(data)
        return render_template('index.html', products=data, title='Index')
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get products"}),
            status=400,
            mimetype='application/json'
        )

    # ====================================
    # GET SINGLE PRODUCT (PRODUCT CONTROLLER) & GET SINGLE VIEW (VIEW CONTROLLER)


@app.route('/products/<item_id>', methods=["GET"])
def getSingleProduct(item_id):
    try:
        data = db.Product.find_one({'_id': ObjectId(item_id)})
        print(data)
        return render_template('product_page.html', product=data, title='Home')
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get products"}),
            status=400,
            mimetype='application/json'
        )


@app.route('/categories/<category>', methods=["GET"])
def getCategoryView(category):
    try:
        data = list(db.Product.find({'category': category}))
        print(data)
        for product in data:
            product["_id"] = str(product["_id"])
            print(data)
        return render_template('index.html', products=data, title=category)
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get products"}),
            status=400,
            mimetype='application/json'
        )


# ====================================
# GET EDIT VIEW (VIEW CONTROLLER)
@app.route("/edit/<item_id>", methods=["GET"])
def getEditView(item_id):
    try:
        data = db.Product.find_one({'_id': ObjectId(item_id)})
        form = AddForm(data=data)
        form.category.choices = categories
        if form.validate_on_submit():
            flash(f' {form.name.data} has been added to the catalog', 'success')
            return redirect(url_for('index.html'))
        return render_template("update.html", form=form, item_id=item_id, title='Update')
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps({"message": "cannot get products"}),
            status=400,
            mimetype='application/json'
        )


# ====================================
# ADD ONE PRODUCT (PRODUCT CONTROLLER)
@app.route("/products", methods=["POST"])
def addProduct():
    try:
        product = {
            "name": request.form["name"],
            "brand": request.form["brand"],
            "price": request.form["price"],
            "description": request.form["description"],
            "category": request.form["category"],
        }
        dbResponse = db.Product.insert_one(product)
        print(dbResponse.inserted_id)
        name = product.get('name')
        flash(f' {name} has been added to the catalog', 'success')
        return redirect(url_for('getAllProducts'))
    except Exception as ex:
        print(ex)


# ====================================
# EDIT ONE PRODUCT (PRODUCT CONTROLLER)
@app.route("/products/<id>", methods=["POST"])
def editProduct(id):
    print('here')
    try:
        dbResponse = db.Product.update_one(
            {"_id": ObjectId(id)},
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
        if dbResponse.modified_count == 1:
            name = request.form["name"]
            flash(f' {name} has been added to the catalog', 'success')
            return redirect(url_for('getAllProducts'))
            # return Response(
            #     response=json.dumps({"message": "product was updated successfully!"}),
            #     status=200,
            #     mimetype='application/json'
            # )
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
@app.route("/products/delete/<id>", methods=["GET"])
def deleteProduct(id):
    try:
        dbResponse = db.Product.delete_one({"_id": ObjectId(id)})
        if dbResponse.deleted_count == 1:
            flash(f'Item has been removed from the catalog', 'success')
            return redirect(url_for('getAllProducts'))
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


@app.route("/categories/add", methods=['GET', 'POST'])
def AddCategory():
    form = AddCategoryForm()

    if form.validate_on_submit():
        categories.append(form.category.data)
        flash(f' {form.category.data} has been updated', 'success')
        return redirect(url_for('getAllProducts'))
    return render_template('add_category.html', title='Add Category', form=form)


# ====================================
if __name__ == "__main__":
    app.run(port=5000, debug=True)

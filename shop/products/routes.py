from flask import redirect, url_for, render_template, flash, request
from shop import db, app, photos
from .models import Brand, Category, AddProduct
from .forms import AddProducts
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} has been added to databse', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
        

    return render_template('addbrand.html', brands='brands')

@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
#    if 'email' not in session:
#        flash(f'please log in first')
#        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method == "POST":
        updatebrand.name = brand
        flash(f'Your brand has been updates', 'success')
        db.session.commit()
        return redirect(url_for('brands'))
    return render_template('updatebrand.html', title='Update Brand Page', updatebrand=updatebrand)

@app.route('/updatecategory/<int:id>', methods=['GET', 'POST'])
def updatecategory(id):
#    if 'email' not in session:
#        flash(f'please log in first')
#        return redirect(url_for('login'))
    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('categories')
    if request.method == "POST":
        updatecategory.name = category
        flash(f'Your brand has been updates', 'success')
        db.session.commit()
        return redirect(url_for('categories'))
    return render_template('updatebrand.html', title='Update category Page', updatecategory=updatecategory)


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == "POST":
        getcat = request.form.get('category')
        cat = Category(name=getcat)
        db.session.add(cat)
        flash(f'The category {getcat} has been added to databse', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))


    return render_template('addbrand.html')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    form = AddProducts(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        color = form.color.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('categories')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")

        addpro = AddProduct(name=name, price=price, stock=stock, discount=discount, color=color, description=desc, brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)
        db.session.add(addpro)
        db.session.commit()
        flash(f'The product {name} has been added to database', 'success')
        return redirect(url_for('admin'))


    return render_template('addproduct.html', title='Add product page', form=form, brands=brands, categories=categories)

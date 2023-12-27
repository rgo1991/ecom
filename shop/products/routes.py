from flask import redirect, url_for, render_template, flash, request
from shop import db, app
from .models import Brand, Category
from .forms import AddProduct

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
    form = AddProduct(request.form)
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('addproduct.html', title='Add product page', form=form, brands=brands, categories=categories)

from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from .form.form import ProductForm

def index(req):
    if req.method == "POST":
        form =ProductForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('views:index')
        return render(req, 'views/new.jinja',{'form':form})
    
    products = Product.objects.order_by('-id')
    return render(req, 'views/index.jinja',{'products':products})

def new(req):
    form = ProductForm()
    return render(req, 'views/new.jinja',{'form':form})    

def edit(req,id):
    product = get_object_or_404(Product,id=id)
    form = ProductForm(instance=product)
    return render(req, 'views/edit.jinja',{'product':product,'form':form})

def delete(req,id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    return redirect('views:index')

def show(req,id):
    product = get_object_or_404(Product,id=id)
    if req.method == "POST":
        form =ProductForm(req.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('views:show',id=id)
        return render(req, 'views/edit.jinja',{'form':form,'product':product})
    return render(req, 'views/show.jinja',{'product':product})
   
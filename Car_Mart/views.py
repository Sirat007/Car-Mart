from django.shortcuts import render
from Cars.models import Car
from CarBrand.models import Brand

def home(request,brand_slug = None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand_car = Brand.objects.get(slug = brand_slug)
        data = Car.objects.filter(brand = brand_car)
    brands = Brand.objects.all()
    return render(request,'home.html',{'data':data, 'brands':brands})
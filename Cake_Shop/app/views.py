from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'loginpage.html')


def add_customer(request):
    return render(request,'add_customer.html')


def add_item(request):
    return render(request,'add_item.html')



def add_product(request):
    return render(request,'add_product.html')


def add_supplier(request):
    return render(request,'add_supplier.html')


def add_supplyorder(request):
    return render(request,'add_supplyorder.html')


def conform_order(request):
    return render(request,'confirm_order.html')


def dashboard(request):
    return render(request,'dashboard.html')


def find_customer(request):
    return render(request,'find_customer.html')


def homepage(request):
    return render(request,'homepageview.html')


def pie_chart(request):
    return render(request,'pie_chart.html')


def printbill(request):
    return render(request,'printbillview.html')


def take_homedelivery(request):
    return render(request,'take_homedelivery.html')


def take_order(request):
    return render(request,'take_order.html')


def update_product(request):
    return render(request,'update_product.html')


def view_delivery(request):
    return render(request,'view_homedelivery.html')


def view_order(request):
    return render(request,'view_order.html')


from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Customer
from .forms import CustomerForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def customer(request):
    customer_list = Customer.objects.all()
    template = loader.get_template("myapp/customer.html")
    context = {
        "customer_list": customer_list,
    }
    return HttpResponse(template.render(context, request))

def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():

            return HttpResponseRedirect("/thanks/")
    else:
        form = CustomerForm()

        for field in form:
            print(field.name)


    return render(request, "myapp/customer_create.html", {"form": form})
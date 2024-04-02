from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'Anusha','father':'Devendra Nath Reddy','age':22}
    return render(request,'jinja.html',context=d)
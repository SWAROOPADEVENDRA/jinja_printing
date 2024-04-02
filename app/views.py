from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'Anusha','father':'Devendra Nath Reddy'}
    return render(request,'jinja.html',context=d)
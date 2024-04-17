from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "main/index.html")

def class_page(request):
    return render(request, "main/class.html")

def blog_page(request):
    return render(request, "main/blog.html")

def about_page(request):
    return render(request, "main/about.html")
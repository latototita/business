from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)
def privacy(request):
    return render(request,'pricing.html',{})
def article(request):
    return render(request,'work-single.html',{})
def terms(request):
    return render(request,'contact.html',{})

def about(request):
    return render(request,'about.html',{})
def work(request):
    return render(request,'work.html',{})

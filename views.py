from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from webApp.models import *
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

def index(request):
    if(request.session.__contains__('userName')):
        username = request.session['userName']
    else:
        username=""

    return render(request, 'index.html',{'name':username})
    
def shop1(request):
    if(request.session.__contains__('userName')):
        username = request.session['userName']
    else:
        username=""
    obj=shop.objects.all()
    return render(request, 'shop.html',{'data':obj,'name':username})

def blog(request):
    return render(request, 'blog.html')

def account(request):
    return render(request, 'myaccount.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    obj1=CartProduct.objects.all()
    newobj=list(obj1)
    total=0
    for i in newobj:
        total=total+int(i.subtotal)
    length=len(obj1)
    return render(request,'cart.html',{"data":obj1,"length":length,'totalAmount':total})

def signup(request):
    return render(request, 'signup.html')

def data(request):
    a=request.POST.get('fn')
    b=request.POST.get('ln')
    c=request.POST.get('em')
    d=request.POST.get('cm')

    obj=Information(firstname=a , lastname=b , email=c , comment=d)
    obj.save()

    messages.success(request, "send your information!!!!")

    return redirect('/contact')

def submit(request):
    a=request.POST.get('name')
    b=request.POST.get('email')
    c=request.POST.get('pass')

    obj=sign(uname=a,password=c,email=b)
    obj.save()

    messages.success(request, "Data saved!!!!")

    return redirect('/account')

def logincheck(request):
    a=request.POST.get('name')
    b=request.POST.get('pass')

    obj=sign.objects.all()
    login=False

    for i in obj:
        if ((i.uname==a or i.email==a) and i.password==b):
            login=True
            request.session['userName'] = i.uname 
            messages.success(request, "Login Successfully!!!!")
            return redirect('/')

    if login==False:
        messages.warning(request, "You are not register!!!!")
        return render(request,'/account')


def cartItem(request):
    a=request.POST.get("nm")
    b=request.POST.get("mg")
    c=request.POST.get("prce")

    obj=CartProduct(name=a,img=b,price=c)
    obj.save()

    obj1=CartProduct.objects.all()
    messages.success(request, "PRODECT ADDED!!!!")

    
    return redirect('/shop1')

def deletecart(request):
    a=request.POST.get('cartproduct')

    obj=CartProduct.objects.get(id=a)
    obj.delete()
    messages.success(request, "Product deleted successfully !!")

    return redirect('/cart')

def increment(request):
    a=request.POST.get('id')

    obj=CartProduct.objects.get(id=a)
    obj.quantity=int(obj.quantity)+1
    obj.subtotal=int(obj.subtotal)+50
    obj.save()

    return redirect('/cart')

def decrement(request):
    a=request.POST.get('id')

    obj=CartProduct.objects.get(id=a)
    obj.quantity=int(obj.quantity)-1
    obj.subtotal=int(obj.subtotal)-50
    obj.save()

    if obj.quantity==0:
        obj.delete()

    return redirect('/cart')


def logout(request):
    if(request.session['userName']):
        del request.session['userName']
    

    messages.success(request, "Log out successfully....!!!!!")

    return render(request,"index.html")
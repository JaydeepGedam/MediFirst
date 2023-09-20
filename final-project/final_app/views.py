from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group, User, auth
from django.contrib import messages
from .forms import ProductForm, Admin_Registation_Form, Doctor_Registation_Form, User_Profile_Form
from .models import Appointment, Product, Contact, Admin_Register, Doctor_Register, User_Profile, Order, Appointment, Donate
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from final_app.middlewares.auth import auth_middleware
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
import os

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])

        return redirect('index')

    def get(self,request):
        usergroup = 'default'
        if request.session.get('group', 'default') == 'user':
            print(usergroup)
            usergroup = 'user'
        if request.session.get('group', 'default') == 'admin':
            print(usergroup)
            usergroup = 'admin'
        if request.session.get('group', 'default') == 'doctor':
            print(usergroup)
            usergroup = 'doctor'

        print(usergroup)

        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        context = {
        "products": Product.objects.filter(featured=True),
        "latests": Product.objects.filter(latest=True),
        "usergroup":usergroup  
        }
        return render(request, 'index.html', context)

class Cart(View):
    def get(self,request):
        usergroup = 'default'
        if request.session.get('group', 'default') == 'user':
            print(usergroup)
            usergroup = 'user'
        if request.session.get('group', 'default') == 'admin':
            print(usergroup)
            usergroup = 'admin'
        if request.session.get('group', 'default') == 'doctor':
            print(usergroup)
            usergroup = 'doctor'

        products = {}
        cartprods = request.session.get('cart',None)
        print("Cart : ",cartprods)
        if cartprods is None:
            print("inside if")
            return render(request, 'cartempty.html')
        else:
            print("Inside else")
            ids = list(cartprods.keys())
            products = Product.get_products_by_id(ids)
        context = {'products':products,"usergroup":usergroup}
        return render(request, 'cart.html',context)

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.user
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, user, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(username=user,
            product = product,
            price = product.prod_price,
            address = address,
            phone = phone,
            quantity= cart.get(str(product.id)))

            print(order.placeOrder())
            
        request.session['cart'] = {}

        return redirect('cart')

class OrderView(View):
    def get(self, request):
        username = request.user
        orders = Order.get_order_by_customer(username)
        print(orders)
        orders = orders.reverse()
        return render(request, 'orders.html', {'orders':orders})

def cartlogin(request):
    return redirect('cart')


# def index(request):
#     context = {
#         "products": Product.objects.filter(featured=True),
#         "latests": Product.objects.filter(latest=True)
#     }
#     return render(request, 'index.html', context)

# def products(request):
#     context = {
#         "products": Product.objects.all()
#     }
#     return render(request, 'products.html', context)

class Products(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])

        return redirect('products')

    def get(self,request):
        usergroup = 'default'
        if request.session.get('group', 'default') == 'user':
            print(usergroup)
            usergroup = 'user'
        if request.session.get('group', 'default') == 'admin':
            print(usergroup)
            usergroup = 'admin'
        if request.session.get('group', 'default') == 'doctor':
            print(usergroup)
            usergroup = 'doctor'
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        context = {
        "products": Product.objects.all(),
        "usergroup":usergroup 
        }
        return render(request, 'products.html', context)

def base(request):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    context = {
            "usergroup":usergroup 
        }
    return render(request, 'base.html',context)

def product_details(request, id=0):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    if id != 0:
        product = Product.objects.get(id=id)
        context = {
            "product": product,
            "usergroup":usergroup 
        }
        return render(request, 'product-details.html', context)
    return render(request, 'product-details.html')

def services(request):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    context = {
        "usergroup":usergroup 
        }
    return render(request, 'services.html',context)
    
def developers(request):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    context = {
        "usergroup":usergroup 
        }
    return render(request, 'developers-section.html',context)

def disclaimer(request):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    context = {
        "usergroup":usergroup 
        }
    return render(request, 'disclaimer.html',context)

def privacy(request):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    context = {
        "usergroup":usergroup 
        }
    return render(request, 'privacy.html',context)

def terms(request):
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    context = {
        "usergroup":usergroup 
        }
    return render(request, 'terms.html',context)

def admin_register(request):
    if request.method == "POST":
        form = Admin_Registation_Form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('admin_dashboard')
            except:
                pass
        else:
            print(form.errors)
    else:
        form = Admin_Registation_Form()
    context={'form':form}
    # return render(request,'admin_register.html',context)
    if request.session.has_key('username'):
        return render(request,'admin_register.html',context)
    else:
        return render(request,'index.html')


def admin_login(request):
    if 'is_logged' in request.session:
        return redirect('admin_dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        count = Admin_Register.objects.filter(username=username, password=password).count()
        if count > 0:
            request.session['is_logged'] = True
            request.session['username'] = username
            user = Admin_Register.objects.get(username=username)
            request.session['group'] = user.group 
            print(request.session['group'])
            return redirect('admin_dashboard')
        else:
            # messages.error(request, "Invalid credentials")
            return render(request, 'admin_login.html', {'alert_flag': True})
    return render(request,'admin_login.html')


def admin_dashboard(request):
    if request.session.has_key('username'):
        print(request.session['group'])
        if str(request.session['group']) == 'doctor':
            return redirect('doctor_dashboard')
        context = {
        "allproducts" : Product.objects.all().count(),
        "pending" : Order.objects.filter(status=False).count(),
        "delivered" : Order.objects.filter(status=True).count(),
        "users" : User.objects.all().count(),
        "orders" : Order.objects.all().count(),
        "feedbacks" : Contact.objects.all(),
        "donates" : Donate.objects.all(),
        }
        return render(request,'admin_dashboard.html',context)
    else:
        return redirect('admin_login')


def admin_logout(request):
    try:
        del request.session['is_logged']
        del request.session['username']
        del request.session['group']
    except KeyError:
        pass 
    return redirect('/')


def login(request):
    return_url = None
    login.return_url = request.GET.get('return_url')
    if 'is_logged' in request.session:
        return redirect('user_dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            request.session['is_logged'] = True
            auth.login(request, user)
            request.session['username'] = username

            request.session['group'] = 'user'

            if login.return_url:
                return HttpResponseRedirect(login.return_url)
            else:
                login.return_url = None
                return redirect("index")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                user_profile = User_Profile(username=user)
                user_profile.save()
                return redirect('login')
        else: 
            messages.info(request, 'Password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

def user_dashboard(request):
    try:
        myuser = User_Profile.objects.get(username=request.user)
    except User_Profile.DoesNotExist:
        myuser = None
    if myuser is not None:
        data = {'myuser': myuser,"appointments": Appointment.objects.filter(username=request.user)}
    else:
        data = {}
    if request.method == "POST":
        user = request.user
        photo = request.FILES.get('photo')
        fullname = request.POST.get('fullname')
        email = request.user.email
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if photo is None:
            photo= myuser.photo
        else:
            image_path = myuser.photo.path
            if os.path.exists(image_path):
                os.remove(image_path)
        try:
            myuser.username=user
            myuser.photo=photo
            myuser.fullname=fullname
            myuser.email=email
            myuser.phone=phone
            myuser.address=address
            myuser.save()
        except ValidationError:
            messages.success(request,'Record Not Saved...')
        return redirect('user_dashboard')
    # if request.POST.get('changepass'):
    #     fm = PasswordChangeForm(user=request.user)
    #     return render(request,'user_dashboard.html',{'form':fm})
    return render(request,'user_dashboard.html',data)

def logout(request):
    auth.logout(request)
    try:
        del request.session['group']
    except KeyError:
        pass
    return redirect('/')

def prodform(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    context = {
        "form": form
    }
    if request.session.has_key('username'):
        if request.session['group'] == 'admin':
            return render(request,'InsertProduct.html', context)
        return render(request,'index.html')
    else:
        return render(request, 'index.html')


def submit_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        msg = request.POST.get('message')
        try:
            Contact(name=name,email=email,subject=subject,msg=msg).save()
        except ValidationError:
            data = {'msg':False}
            return JsonResponse(data)
        data1 = {'msg':True}
        return JsonResponse(data1)

def delete_feedback(request, id):
    Contact.objects.get(id=id).delete()
    return redirect('admin_dashboard')


def submit_appointment(request):
    if request.method == "POST":
        if request.session.has_key('username'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            aptdate = request.POST.get('aptdate')
            tddate = request.POST.get('tddate')
            selectdoctor = request.POST.get('selectdoctor')
            msg = request.POST.get('message')
            try:
                if selectdoctor == "":
                    raise ValidationError(('Invalid value'), code='invalid')
                Appointment(username = request.user,name=name,email=email,phone=phone,aptdate=aptdate,tddate=tddate,selectdoctor=selectdoctor,msg=msg).save()
            except ValidationError:
                data = {'msg':False}
                return JsonResponse(data)
            data = {'msg':True}
            return JsonResponse(data)
        else:
            return render(request,'login.html')
    return render(request,'index.html')

def donate(request):
    print("above if")
    usergroup = 'default'
    if request.session.get('group', 'default') == 'user':
        print(usergroup)
        usergroup = 'user'
    if request.session.get('group', 'default') == 'admin':
        print(usergroup)
        usergroup = 'admin'
    if request.session.get('group', 'default') == 'doctor':
        print(usergroup)
        usergroup = 'doctor'
    if request.method == "POST":
        print("inside post")
        if request.session.has_key('username'):
            print("inside user login")
            dnr_name = request.POST.get('dnr_name')
            dnr_address = request.POST.get('dnr_address')
            dnr_phone = request.POST.get('dnr_phone')
            drg_name = request.POST.get('drg_name')
            drg_lotno = request.POST.get('drg_lotno')
            drg_exdate = request.POST.get('drg_exdate')
            drg_quantity = request.POST.get('drg_quantity')
            drg_strength = request.POST.get('drg_strength')
            signature = request.FILES.get('signature')
            today_date = request.POST.get('today_date')
            try:
                print("inside try")
                Donate(username=request.user,dnr_name=dnr_name,dnr_address=dnr_address,dnr_phone=dnr_phone,drg_name=drg_name,drg_lotno=drg_lotno,drg_exdate=drg_exdate,drg_quantity=drg_quantity,drg_strength=drg_strength,signature=signature,today_date=today_date).save()
            except ValidationError:
                print("something wrong")
                messages.success(request,'Not Submitted...')
                return redirect('/')
    context = {"usergroup":usergroup}
    return render(request,'thankyou.html',context)

def delete_donate(request,id):
    Donate.objects.get(id=id).delete()
    return redirect('admin_dashboard')


# def search(request): 
#     query = request.GET['query']
#     if len(query) > 80:
#         allProducts = Product.objects.none()
#     else:
#         allProductsName = Product.objects.filter(prod_name__icontains=query)
#         allProductsDetails = Product.objects.filter(prod_detail__icontains=query)
#         allProducts = allProductsName.union(allProductsDetails)
#     if allProducts.count() == 0:
#         messages.warning(request, "No search results found. PLease try with another search.")
#     params = {'allProducts': allProducts, 'query': query}
#     return render(request, 'search.html', params)



class Search(View):
    def get(self,request):
        usergroup = 'default'
        if request.session.get('group', 'default') == 'user':
            print(usergroup)
            usergroup = 'user'
        if request.session.get('group', 'default') == 'admin':
            print(usergroup)
            usergroup = 'admin'
        if request.session.get('group', 'default') == 'doctor':
            print(usergroup)
            usergroup = 'doctor'
        if 'search' in request.GET:
            query = request.GET.get('query')
            print(query)
            if len(query) > 80:
                allProducts = Product.objects.none()
            else:
                allProductsName = Product.objects.filter(prod_name__icontains=query)
                allProductsDetails = Product.objects.filter(prod_detail__icontains=query)
                allProducts = allProductsName.union(allProductsDetails)
            if allProducts.count() == 0:
                messages.warning(request, "No search results found. Please try with another search.")
            params = {'allProducts': allProducts, 'query': query, "usergroup":usergroup }
            return render(request, 'search.html', params)
        return redirect('cart')

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart',request.session['cart'])

        return redirect('search')


def doctor_register(request):
    if request.method == "POST":
        form = Doctor_Registation_Form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('admin_dashboard')
            except:
                pass
        else:
            print(form.errors)
    else:
        form = Doctor_Registation_Form()
    context={'form':form}
    if request.session.has_key('username'):
        if request.session['group'] == 'admin':
            return render(request,'doctor_register.html',context)
        return render(request,'index.html')
    else:
        return render(request,'index.html')

def doctor_login(request):
    if 'is_logged' in request.session:
        return redirect('doctor_dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # doctor = authenticate(request, username=username, password=password)
        # if doctor is not None:
        #     login(request, doctor)
        #     return redirect('doctor_dashboard')
            
        count = Doctor_Register.objects.filter(username=username, password=password).count()
        if count > 0:
            request.session['is_logged'] = True
            request.session['username'] = request.POST["username"]
            user = Doctor_Register.objects.get(username=username)
            request.session['group'] = user.group
            print(request.session['group'])
            return redirect('doctor_dashboard')
        else:
            return render(request, 'doctor_login.html', {'alert_flag': True})
    return render(request,'doctor_login.html')


def doctor_dashboard(request):
    if request.session.has_key('username'):
        print(request.session['group'])
        if str(request.session['group']) == 'admin':
            return redirect('admin_dashboard')
        doctor = Doctor_Register.objects.get(username=request.session['username'])
        context = {
        "pending_appointments": Appointment.objects.filter(status=False,selectdoctor=doctor.name),
        "successfull_appointments": Appointment.objects.filter(status=True,selectdoctor=doctor.name),
        }
        return render(request,'doctor_dashboard.html', context)
    else:
        return redirect('doctor_login')

def delete(request, id):
    Appointment.objects.get(id=id).delete()
    return redirect('doctor_dashboard')

def update(request, id):
    Appointment.objects.filter(id=id).update(status=True)
    return redirect('doctor_dashboard')

def doctor_logout(request):
    try:
        del request.session['is_logged']
        del request.session['username']
        del request.session['group']
    except KeyError:
        pass
    return redirect('/')


def error_404(request):
    return render(request,'404.html')

def error_500(request):
    return render(request,'500.html')
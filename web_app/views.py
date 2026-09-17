from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import contectform, profileform, aaddimgform, laddimgform, maddimgform
from .models import contectus, profile, aaddimage, laddimage, maddimage

# Index function
def index(request):
    return render(request, 'index.html')

# Home function
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

# base_home function
def bhome(request):
    return render(request, 'basehome.html')

# About function
@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')

# Services(mobile) function
@login_required(login_url='login')
def mobiles(request):
    data = maddimage.objects.all()
    return render(request, 'mobile.html', {'data': data})

# Services(laptop) function
@login_required(login_url='login')
def laptops(request):
    data = laddimage.objects.all()
    return render(request, 'laptop.html', {'data': data})

# Services(Accessories) function
@login_required(login_url='login')
def accessoriess(request):
    data = aaddimage.objects.all()
    return render(request, 'accessories.html', {'data': data})

# Signup function
def signup(request):
    if request.method == 'POST':
        user = request.POST['user']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password == confirm:
            if User.objects.filter(username=user).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')

            else:
                User.objects.create_user(username=user, email=email, password=password)
                messages.success(request, 'Account created successfully! Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# Login function
def login(request):
    if request.method == 'POST':
        user = request.POST['user']
        password = request.POST['password']

        user_obj = auth.authenticate(username=user, password=password)

        if user_obj is None:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
        else:
            auth.login(request, user_obj)
            return redirect('bhome')
    else:
        return render(request, 'login.html') 

# Logout function
def logout(request):
    auth.logout(request)
    return redirect('login')

# Show contact function
@login_required(login_url='login')
def cshow(request):
    data = contectus.objects.all()
    return render(request, 'contects.html', {'data': data})

# Form contact function
@login_required(login_url='login')
def cform(request):
    if request.method == 'GET':
        form = contectform()
        return render(request, 'contectf.html', {'form': form})
    else:
        form = contectform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('contects')
        else:
            return render(request, 'contectf.html', {'form': form})

# Show Profile
@login_required(login_url='login')
def pshow(request):
    if request.user.is_authenticated:
        images = profile.objects.filter(user=request.user.username)
        return render(request, 'profiles.html', {'image': images})
    else:
        return redirect('login')

# Profile form
@login_required(login_url='login')       
def pform(request):
    existing = profile.objects.filter(user=request.user.username).first()
    if existing:
        return redirect('profiles')
        
    if request.method == 'GET':
        form = profileform()
        return render(request, 'profilef.html', {'form': form})
    else:
        form = profileform(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user.username
            prof.save()
            return redirect('profiles')
        return render(request, 'profilef.html', {'form': form})

# Update profile photo function
@login_required(login_url='login')
def updatei(request, id):
    data = profile.objects.get(id=id)
    if request.method == 'GET':
        form = profileform(instance=data)
        return render(request, 'profilef.html', {'form': form})
    else:
        form = profileform(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('profiles')
        else:
            return render(request, 'profilef.html', {'form': form})

# Delete photo function
@login_required(login_url='login')
def deletei(request, id):
    data = profile.objects.filter(id=id)
    data.delete()
    return redirect('profiles')

# Add new Mobile Function
@login_required(login_url='login')
def addm(request):
    if request.method == 'GET':
        form = maddimgform()
        return render(request, 'mobileform.html', {'form': form})
    else:
        form = maddimgform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mobile')
        else:
            return render(request, 'mobileform.html', {'form': form})

# Add new Laptop Function
@login_required(login_url='login')
def addl(request):
    if request.method == 'GET':
        form = laddimgform()
        return render(request, 'laptopform.html', {'form': form})
    else:
        form = laddimgform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('laptop')
        else:
            return render(request, 'laptopform.html', {'form': form})

# Add new Accessories Function
@login_required(login_url='login')
def adda(request):
    if request.method == 'GET':
        form = aaddimgform()
        return render(request, 'accessoriesform.html', {'form': form})
    else:
        form = aaddimgform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accessrioes')
        else:
            return render(request, 'accessoriesform.html', {'form': form})

# Unified search function for all products
@login_required(login_url='login')
def search(request):
    query = request.GET.get('search', '').strip() or request.POST.get('search', '').strip()
    if query:
        mobiles = maddimage.objects.filter(title__icontains=query)
        laptops = laddimage.objects.filter(title__icontains=query)
        accessories = aaddimage.objects.filter(title__icontains=query)
    else:
        mobiles = maddimage.objects.none()
        laptops = laddimage.objects.none()
        accessories = aaddimage.objects.none()
    
    total_count = mobiles.count() + laptops.count() + accessories.count()
    context = {
        'query': query,
        'mobiles': mobiles,
        'laptops': laptops,
        'accessories': accessories,
        'total_count': total_count,
    }
    return render(request, 'search.html', context)

# Read for accessories
@login_required(login_url='login')
def areadmore(request, id):
    data1 = aaddimage.objects.get(id=id)
    return render(request, 'readmore.html', {'data': data1})

# Read for Mobile
@login_required(login_url='login')
def mreadmore(request, id):
    data1 = maddimage.objects.get(id=id)
    return render(request, 'mreadmore.html', {'data': data1})

# Read for Laptop
@login_required(login_url='login')
def lreadmore(request, id):
    data1 = laddimage.objects.get(id=id)
    return render(request, 'lreadmore.html', {'data': data1})

# function for not found
def Not(request):
    return render(request, 'not.html')

# ---------------- Cart (session-based) ----------------
def _cart_model_map():
    return {
        "m": (maddimage, "Mobile"),
        "l": (laddimage, "Laptop"),
        "a": (aaddimage, "Accessory"),
    }

def _get_cart(request):
    cart = request.session.get("cart", {})
    if not isinstance(cart, dict):
        cart = {}
    return cart

def _save_cart(request, cart):
    request.session["cart"] = cart
    request.session.modified = True

@login_required(login_url='login')
def cart(request):
    cart = _get_cart(request)
    items = []
    total_qty = 0
    for key, item in cart.items():
        total_qty += int(item.get("qty", 0))
        items.append(item)
    return render(request, 'cart.html', {"items": items, "total_qty": total_qty})

@login_required(login_url='login')
def cart_add(request, item_type, item_id):
    model_map = _cart_model_map()
    if item_type not in model_map:
        messages.error(request, "Invalid item type.")
        return redirect('cart')

    model_cls, label = model_map[item_type]
    try:
        obj = model_cls.objects.get(id=item_id)
    except model_cls.DoesNotExist:
        messages.error(request, "Item not found.")
        return redirect('cart')

    cart = _get_cart(request)
    key = f"{item_type}:{item_id}"
    if key in cart:
        cart[key]["qty"] = int(cart[key].get("qty", 0)) + 1
    else:
        cart[key] = {
            "key": key,
            "type": label,
            "item_type": item_type,
            "id": item_id,
            "title": obj.title,
            "image_url": obj.image.url if getattr(obj, "image", None) else "",
            "qty": 1,
        }

    _save_cart(request, cart)
    messages.success(request, f"Added {obj.title} to cart.")
    return redirect('cart')

@login_required(login_url='login')
def cart_remove(request, item_type, item_id):
    cart = _get_cart(request)
    key = f"{item_type}:{item_id}"
    if key in cart:
        del cart[key]
        _save_cart(request, cart)
        messages.success(request, "Removed item from cart.")
    return redirect('cart')

@login_required(login_url='login')
def cart_buy(request):
    if request.method == "POST":
        _save_cart(request, {})
        messages.success(request, "Thank you! Your order has been placed successfully.")
    return redirect('cart')

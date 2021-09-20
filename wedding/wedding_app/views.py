from django.shortcuts import render, redirect
from .models import User, Wedding, Registry, Credit, Post
import bcrypt
from django.contrib import messages
from datetime import datetime
from django.utils import formats


def index(request):
    return render(request, 'register.html')

def home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    wedding_complete = False
    weddings = Wedding.objects.all()
    this_user = User.objects.get(id=request.session['user_id'])
    
    for each_wedding in weddings:
        if this_user.id == each_wedding.wedding_owner.id:
            wedding_complete = True
            
    context = {
        # "users": User.objects.all(),
        "wedding_complete": wedding_complete,
        "this_user": this_user,
        # "weddings": Wedding.objects.all(),
        # "weddings_user_ids": Wedding.objects.filter().only('wedding_owner_id'),
        # "user_weddings_ids": User.objects.filter().only('wedding_created').values('id'),
        # "registries": Registry.objects.all(),
    }
    # print(context["this_user"])
    # print(context['weddings_user_ids'])
    # print(User.objects.filter().only('wedding_created').values('id'))
    return render(request, 'index.html', context)

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashedpassword = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        print(hashedpassword)
        new_user = User.objects.create(
            fname = request.POST['fname'],
            lname = request.POST['lname'],
            email = request.POST['email'],
            password = hashedpassword
        )
    request.session['user_id'] = new_user.id
    return redirect('/create_wedding')

def log(request):
    return render(request, 'login.html')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/log')
    else:
        user = User.objects.get(email = request.POST['logemail'])
        request.session['user_id'] = user.id
        return redirect('/home')

def create_wedding(request):
    if 'user_id' not in request.session:
        return redirect('/')
    wedding_complete = False
    weddings = Wedding.objects.all()
    this_user = User.objects.get(id=request.session['user_id'])
    for each_wedding in weddings:
        if this_user.id == each_wedding.wedding_owner.id:
            wedding_complete = True
        if wedding_complete:
            return redirect('/home')
    user = User.objects.get(id=request.session['user_id'])
    wedding_id = Wedding.objects.filter().only('wedding_owner_id'),
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "this_user": user,
    }
    return render(request, 'create_wedding.html', context)

def add_wedding(request):
    wedding_owner = User.objects.get(id=request.session['user_id'])
    errors = Wedding.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create_wedding')
    else:
        Wedding.objects.create(
            sfname = request.POST['sfname'],
            slname = request.POST['slname'],
            cvenue = request.POST['cvenue'],
            caddress = request.POST['caddress'],
            ccity = request.POST['ccity'],
            cstate = request.POST['cstate'],
            cdate = request.POST['cdate'],
            czip = request.POST['czip'],
            ctime = request.POST['ctime'],
            rvenue = request.POST['rvenue'],
            raddress = request.POST['raddress'],
            rcity = request.POST['rcity'],
            rstate = request.POST['rstate'],
            rzip = request.POST['rzip'],
            rdate = request.POST['rdate'],
            rtime = request.POST['rtime'],
            description = request.POST['description'],
            wedding_owner = wedding_owner
        )
    return redirect('/create_registry')

def create_registry(request):
    if 'user_id' not in request.session:
        return redirect('/')
    wedding_complete = False
    weddings = Wedding.objects.all()
    this_user = User.objects.get(id=request.session['user_id'])
    
    for each_wedding in weddings:
        if this_user.id == each_wedding.wedding_owner.id:
            wedding_complete = True
    context = {
        "this_user": this_user,
        "wedding_complete": wedding_complete,
    }
    return render(request, 'create_registry.html', context)

def add_registry(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    registry_owner = User.objects.get(id=request.session['user_id'])
    Registry.objects.create(
        funame = request.POST['funame'],
        remaining_balance = request.POST['goal'],
        goal = request.POST['goal'],
        registry_owner = registry_owner,
    )
    return redirect(f'/wedding/{user_id}')

def wedding(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=user_id)
    context = {
        "this_user": User.objects.get(id=request.session['user_id']),
        "user": user,
        "weddings": Wedding.objects.all(),
        "registries": Registry.objects.all()
    }
    return render(request, 'wedding.html', context)

def my_account(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    wedding_complete = False
    weddings = Wedding.objects.all()
    this_user = User.objects.get(id=request.session['user_id'])
    
    for each_wedding in weddings:
        if this_user.id == each_wedding.wedding_owner.id:
            wedding_complete = True
    context = {
        "weddings": Wedding.objects.all(),
        "this_user": this_user,
        "wedding_complete": wedding_complete,
    }
    return render(request, 'my_account.html', context)

def edit_account(request, user_id):
    errors = User.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/my_account/{user_id}')
    else:
        edit = User.objects.get(id=user_id)
        edit.fname = request.POST['fname']
        edit.lname = request.POST['lname']
        edit.email = request.POST['email']
        edit.save()
    return redirect(f'/my_account/{user_id}')

def contribute(request, registry_id):
    if 'user_id' not in request.session:
        return redirect('/')
    registry = Registry.objects.get(id=registry_id)
    context = {
        "registry": registry,
    }
    return render(request, 'contribute.html', context)

def make_contribution(request, registry_id):
    registry = Registry.objects.get(id=registry_id)
    errors = Credit.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/contribute/{registry_id}')
    else: 
        amount = request.POST['amount']
        message = request.POST['message']
        card_number = request.POST['card_number']
        card_zip = request.POST['card_zip']
        card_date = request.POST['card_date']
        registry.remaining_balance -= int(amount)
        registry.save()
    return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    return render(request, 'success.html')

def registry(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=user_id)
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": user,
        "this_user": this_user,
        "weddings": Wedding.objects.all(),
        "registries": Registry.objects.all()
    }
    return render(request, 'registry.html', context)

def details(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=user_id)
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": user,
        "this_user": this_user,
        "weddings": Wedding.objects.all(),
        "registries": Registry.objects.all()
    }
    return render(request, 'details.html', context)

def posts(request, user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=user_id)
    this_user = User.objects.get(id=request.session['user_id'])
    context = {
        "user": user,
        "this_user": this_user,
        "weddings": Wedding.objects.all(),
        "posts": Post.objects.all().order_by("-created_at")
        
    }
    return render(request, 'posts.html', context)

def make_post(request, user_id):
    user = User.objects.get(id=user_id)
    uploaded_by = User.objects.get(id=request.session['user_id'])
    new_post = Post.objects.create(
        post = request.POST['post'],
        uploaded_by = uploaded_by
    )
    context = {
        "user": user,
        "posts": Post.objects.all().order_by("-created_at"),
        "this_user": User.objects.get(id=request.session['user_id']),
        "weddings": Wedding.objects.all(),
    }
    return render(request, 'post_partial.html', context)

def like_post(request, post_id, user_id):
    post = Post.objects.get(id=post_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.likes.add(post)
    return redirect(f'/posts/{user_id}')

def unlike_post(request, post_id, user_id):
    post = Post.objects.get(id=post_id)
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.likes.remove(post)
    return redirect(f'/posts/{user_id}')

def search(request):
    if 'user_id' not in request.session:
        return redirect('/')
    wedding_complete = False
    weddings = Wedding.objects.all()
    this_user = User.objects.get(id=request.session['user_id'])
    for each_wedding in weddings:
        if this_user.id == each_wedding.wedding_owner.id:
            wedding_complete = True
    if request.method == "POST":
        search = request.POST['search']
        users = User.objects.filter(fname__contains=search)
        weddings = Wedding.objects.all()
        return render(request, 'search.html', {'search': search, 'users': users, 'weddings': weddings, "wedding_complete": wedding_complete, "this_user": this_user})

def my_wedding(request, wedding_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "this_user": User.objects.get(id=request.session['user_id']),
        "item": Wedding.objects.get(id=wedding_id)
        }
    return render(request, 'my_wedding.html', context)

def edit_wedding(request, wedding_id, user_id):
    errors = Wedding.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect(f'/my_wedding/{wedding_id}')
    else:
        edit = Wedding.objects.get(id=wedding_id)
        edit.sfname = request.POST['sfname']
        edit.slname = request.POST['slname']
        edit.cvenue = request.POST['cvenue']
        edit.caddress = request.POST['caddress']
        edit.ccity = request.POST['ccity']
        edit.cstate = request.POST['cstate']
        edit.cdate = request.POST['cdate']
        edit.czip = request.POST['czip']
        edit.ctime = request.POST['ctime']
        edit.rvenue = request.POST['rvenue']
        edit.raddress = request.POST['raddress']
        edit.rcity = request.POST['rcity']
        edit.rstate = request.POST['rstate']
        edit.rzip = request.POST['rzip']
        edit.rdate = request.POST['rdate']
        edit.rtime = request.POST['rtime']
        edit.description = request.POST['description']
        edit.save()
    return redirect(f'/wedding/{user_id}')

def delete_wedding(request, wedding_id):
    delete = Wedding.objects.get(id=wedding_id)
    delete.delete()
    return redirect('/home')

def logout(request):
    request.session.clear()
    return redirect('/log')

# from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from .models import Emp
# from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
# from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib import messages
# from django.core.mail import send_mail

# def home(request):
#     return render(request, 'emp/home.html')

# def navbar(request):
#     return render(request,"emp/navbar.html")

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'You have been logged in successfully')
#             return redirect('home')
#         else:
#             messages.warning(request, "Username or Password is incorrect !!")
#             return redirect('login')
#     else:
#         return render(request, 'emp/login.html')
    


# def logout_user(request):
#     logout(request)
#     messages.success(request, "Logged out successfully")
#     return redirect('home')


# def register_user(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(request, username=username, password=password)
#             login(request, user)
#             return redirect('home')
#         else:
#             form = SignUpForm(request.POST)
#     else:
#         form = SignUpForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'emp/register.html', context)



# def change_password(request):
#     if request.method == 'POST':
#         form = ChangePasswordForm(data=request.POST, user=request.user)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, form.user)
#             messages.success(request, "Password Changed Successfully")
#             return redirect('home')
#     else:
#         form = ChangePasswordForm(user=request.user)
#         print(form)
#     context = {
#         'form': form,
#     }
#     return render(request, 'emp/change_password.html', context)




# def emp_home(request):
#     emps=Emp.objects.all()
#     return render(request,"emp/home1.html",{'emps':emps})


# def add_emp(request):
#     if request.method=="POST":
#         emp_name=request.POST.get("emp_name")
#         emp_id=request.POST.get("emp_id")
#         emp_phone=request.POST.get("emp_phone")
#         emp_address=request.POST.get("emp_address")
#         emp_working=request.POST.get("emp_working")
#         emp_department=request.POST.get("emp_department")
#         e=Emp()
#         e.name=emp_name
#         e.emp_id=emp_id
#         e.phone=emp_phone
#         e.address=emp_address
#         e.department=emp_department
#         if emp_working is None:
#             e.working=False
#         else:
#             e.working=True
#         e.save()
#         return redirect("/emp/home/")
#     return render(request,"emp/add_emp.html",{})

# def delete_emp(request,emp_id):
#     emp=Emp.objects.get(pk=emp_id)
#     emp.delete()
#     return redirect("/emp/home/")

# def update_emp(request,emp_id):
#     emp=Emp.objects.get(pk=emp_id)
#     print("Yes Bhai")
#     return render(request,"emp/update_emp.html",{
#         'emp':emp
#     })

# def do_update_emp(request,emp_id):
#     if request.method=="POST":
#         emp_name=request.POST.get("emp_name")
#         emp_id_temp=request.POST.get("emp_id")
#         emp_phone=request.POST.get("emp_phone")
#         emp_address=request.POST.get("emp_address")
#         emp_working=request.POST.get("emp_working")
#         emp_department=request.POST.get("emp_department")

#         e=Emp.objects.get(pk=emp_id)

#         e.name=emp_name
#         e.emp_id=emp_id_temp
#         e.phone=emp_phone
#         e.address=emp_address
#         e.department=emp_department
#         if emp_working is None:
#             e.working=False
#         else:
#             e.working=True
#         e.save()
#     return redirect("/emp/home/")



from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'emp/home.html')

def navbar(request):
    return render(request, "emp/navbar.html")

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in successfully')
            return redirect('home')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login')
    else:
        return render(request, 'emp/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'emp/register.html', context)

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'emp/change_password.html', context)

def emp_home(request):
    emps = Emp.objects.all()
    return render(request, "emp/home1.html", {'emps': emps})

def add_emp(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
        return redirect("/emp/home/")
    return render(request, "emp/add_emp.html", {})

def delete_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/emp/home/")

def update_emp(request, emp_id):
    emp = Emp.objects.get(pk=emp_id)
    print("Yes Bhai")
    return render(request, "emp/update_emp.html", {'emp': emp})

def do_update_emp(request, emp_id):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Emp.objects.get(pk=emp_id)

        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True
        e.save()
    return redirect("/emp/home/")

@csrf_protect
def get_crop_data(request):
    if request.method == 'POST':
        crop_name = request.POST.get('crop_name')

        lambda_url = 'https://1vk8d5k11e.execute-api.eu-west-1.amazonaws.com/default/x23109831_cropproj'
        headers = {'Content-Type': 'application/json', 'Access-Control-Allow-Origin' : '*', 'Access-Control-Allow-Methods' : '*'}
        payload = {'crop': crop_name}

        try:
            response = requests.post(lambda_url, json=payload, headers=headers)
            logger.info(f"Lambda request status code: {response.status_code}")
            if response.status_code == 200:
                crop_data = response.json()
                logger.info(f"Crop data: {crop_data}")
                return render(request, 'emp/crop_data.html', {'crop_data': crop_data})
            else:
                messages.error(request, 'Error: Crop data not found')
                logger.error("Error: Crop data not found")
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            logger.error(f"Error: {str(e)}")

    return redirect('home')


from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, authenticate, logout
from serviceapp.models import UserType,Registration,ServicerRegistration,Assign,Requests,Services
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

class index(TemplateView):
    template_name='index.html'
class user_signup(TemplateView):
    template_name='register.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        address = request.POST['address'] 
        district = request.POST['district']
        password = request.POST['password']

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Registration()# call the model
            reg.user = user
            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.address=address
            reg.district=district
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            # messages="Registered Successfully"
        return redirect('/',{'message':"Registered Successfully"})
            # return render(request, 'index.html', {'message': "successfully added"})

class loginview(TemplateView):
    template_name='login.html'
    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                elif UserType.objects.get(user_id=user.id).type == "servicer":
                    return redirect('/servicer')
                elif UserType.objects.get(user_id=user.id).type == "worker":
                    return redirect('/worker')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})
        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})
class servicer_signup(TemplateView):
    template_name='service_register.html'
    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        password = request.POST['password']
        image = request.FILES['image']
        regnum = request.POST['regnum']

        ob=FileSystemStorage()
        obj=ob.save(image.name, image)

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='0')
            user.save()

            reg = ServicerRegistration()# call the model
            reg.user = user
            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.image=obj
            reg.regnum=regnum
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "servicer"
            usertype.save()
            # messages="Registered Successfully"
        return redirect('/',{'message':"Registered Successfully"})

def logout_user(request):
    logout(request)
    return redirect(reverse('login'))




def Paymentcheckout(request,id):        
    user = Registration.objects.get(user_id=request.user.id)
    abc = Assign.objects.get(id=id)
         
    
        # amount = abc.amount 
    return render(request,"customer/checkoutpage.html",{'abc':abc})

def Chpayments(request,id):
    ch = Assign.objects.get(id=id)
    requ= ch.request_id 
  
    ff=Requests.objects.get(id=requ)
    se=ff.services_id
    abc=Services.objects.get(id=se)
    abc.status='Available'
    abc.save()
    ff.status='Payment Done'
    ff.save()
    ch.status ='paid'
    ch.paymentstatus = 'paid'
    ch.save()
    return redirect('/user')
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from serviceapp.models import Add_Services, Services, ServicerRegistration, Requests, UserType, Assign,Rating
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class index(LoginRequiredMixin,TemplateView):
    template_name='service provider/index.html'
class CreateServices(LoginRequiredMixin,TemplateView):
    template_name='service provider/create_services.html'
    def get_context_data(self, **kwargs):
        context = super(CreateServices, self).get_context_data(**kwargs)
        pro = Add_Services.objects.all()
        context['dept'] = pro
        return context
    def post(self, request, *args, **kwargs):
        xyz=ServicerRegistration.objects.get(user_id=self.request.user.id)
        name = request.POST['name']
        email = request.POST['email']
        department = request.POST['dept']
        description = request.POST['desc']
        price = request.POST['price'] 
        city = request.POST['city']
        image = request.FILES['image']
        password = request.POST['password']


        ob=FileSystemStorage()
        obj=ob.save(image.name, image)

        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'service provider/create_services.html', {'message': "already added the username or email"})

        else:

            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Services()# call the model
            reg.servicer_id=xyz.id
            reg.user=user
            reg.name=name
            reg.email=email
            reg.department_id=department
            reg.description = description
            reg.price=price
            reg.city=city
            reg.image = obj
            reg.password=password
            reg.status='Available'
            reg.save()
            type = UserType()
            type.user = user
            type.type = "worker"
            type.save()
            # messages="Registered Successfully"

            return redirect('/servicer')
class ViewServices(LoginRequiredMixin,TemplateView):
    template_name="service provider/view_services.html"
    def get_context_data(self, **kwargs):
        context = super(ViewServices, self).get_context_data(**kwargs) 
        abc=ServicerRegistration.objects.get(user_id=self.request.user.id)
        pro = Services.objects.filter(servicer_id=abc.id)
        context['services'] = pro  
        return context

class RemoveServices(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Services.objects.get(id=id).delete()
        return redirect('/servicer')
class UpdateServices(LoginRequiredMixin,TemplateView):
    template_name='service provider/upd_services.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateServices, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = Add_Services.objects.all()
        pro1 =  Services.objects.get(id=id3)
        context['dept'] = pro
        context['upd'] = pro1
       
    
        # id3 = self.request.GET['id']
        # pro =  Services.objects.get(id=id3)
        # context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        name = request.POST['name']
        department = request.POST['dept']
        description = request.POST['desc']
        price = request.POST['price'] 
        city = request.POST['city']
        image = request.FILES['image']

        ob=FileSystemStorage()
        obj=ob.save(image.name, image)

        reg = Services.objects.get(id=id3)# call the model
        reg.name=name
        reg.department_id=department
        reg.description = description
        reg.price=price
        reg.city=city
        reg.image = obj
        reg.save()
        # return redirect('/servicer')

        return render(request, 'service provider/index.html',{'message':"Successfully Profile Edited"})

class Profile(LoginRequiredMixin,TemplateView):
    template_name='service provider/profile.html'
    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = ServicerRegistration.objects.get(user_id=id1)
        context['profile'] = pro
        return context
class UpdateProfile(LoginRequiredMixin,TemplateView):
    template_name='service provider/updpro.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = ServicerRegistration.objects.get(id=id3)
        context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        phone = request.POST['number']
        regnum = request.POST['regnum']
        image = request.FILES['iamge']
        # district = request.POST['district']
        ob=FileSystemStorage()
        obj=ob.save(image.name, image)

        reg = ServicerRegistration.objects.get(id=id3)# call the model
        reg.phone = phone
        reg.image=obj
        reg.regnum=regnum
        reg.save()
        return render(request, 'service provider/index.html',{'message':"Successfully Updated"})
class ViewRequests(LoginRequiredMixin,TemplateView):
    template_name='service provider/service_request.html'
    def get_context_data(self, **kwargs):
        context = super(ViewRequests, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = ServicerRegistration.objects.get(user_id=id1)

        pro = Requests.objects.filter(provider_id=pro.id,status='Selected')
        context['rqst'] = pro
        return context
class Reject(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        rqs = Requests.objects.get(pk=id)
        rqs.status = 'Rejected'
        rqs.save()
        return redirect('/servicer')
class Approve(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        rqs = Requests.objects.get(pk=id)
        rqs.status = 'Approved'
        rqs.save()
        return redirect('/servicer')


class assign(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        id2 = request.GET['id2']
 
        pro = ServicerRegistration.objects.get(user_id=self.request.user.id)
       

        rq = Assign()
        gg=Requests.objects.get(id=id2)
        se=gg.services_id
        abc=Services.objects.get(id=se)
        abc.status='Booked'
        abc.save()
        # se=gg.services_id
        gg.status='assigned'
        
        gg.save()
        rq.services_id=id
        rq.request_id = id2
        rq.provider_id = pro.id
        rq.paymentstatus='Null'
        rq.status = 'assigned'
        rq.save()
        return redirect('/servicer')
class ViewFb(LoginRequiredMixin,TemplateView):
    template_name='service provider/viewfb.html'
    def get_context_data(self, **kwargs):
        context = super(ViewFb, self).get_context_data(**kwargs)
        abc=ServicerRegistration.objects.get(user_id=self.request.user.id)

        pro = Rating.objects.filter(provider_id=abc.id)
        context['fb'] = pro
        return context

class ViewPaymentLists(LoginRequiredMixin,TemplateView):
    template_name='service provider/viewpayment.html'
    def get_context_data(self, **kwargs):
        context = super(ViewPaymentLists, self).get_context_data(**kwargs)
        abc=ServicerRegistration.objects.get(user_id=self.request.user.id)

        pro = Assign.objects.filter(provider_id=abc.id)
        context['pay'] = pro
        return context

     

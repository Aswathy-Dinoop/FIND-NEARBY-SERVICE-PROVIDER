from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from serviceapp.models import Services,Add_Services,Registration,Requests,ServicerRegistration,Rating,Assign
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class index(LoginRequiredMixin,TemplateView):
    template_name='customer/index.html'
class viewallservices(LoginRequiredMixin,TemplateView):
    template_name='customer/view_all_services.html'
    def get_context_data(self, **kwargs):
        context = super(viewallservices, self).get_context_data(**kwargs)
        pro = Add_Services.objects.all()
        abc = Services.objects.filter(status='Available')
        context = {
            'services':abc,'dept':pro
        }
        return context

    def post(self, request, *args, **kwargs):
        pro = Add_Services.objects.all()
        search = self.request.POST['search']
        obj1=Add_Services.objects.get(id=search)
        services = Services.objects.filter(department_id=search)
        
        return render(request,'customer/view_all_services.html',{'services':services,'dept':pro})

class SendRequestsForm(TemplateView):
    template_name='customer/send_requests.html'
    def get_context_data(self, **kwargs):
        context = super(SendRequestsForm, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = Services.objects.get(id=id3)
        context['upd'] = pro
        return context
    def post(self, request, *args, **kwargs):
        id=request.GET['id']
        id2=self.request.GET['id2']
        user=Registration.objects.get(user_id=self.request.user.id)
        date= self.request.POST['bdate']
        time= self.request.POST['time']

        reg = Requests()
        reg.user_id = user.id
        reg.services_id = id
        reg.provider_id = id2
        reg.bookingdate=date
        reg.bookingtime=time
        reg.status='Selected'
        reg.save()
        return redirect('/user')

class SendRequests(View):
    def dispatch(self, request, *args, **kwargs):
        id=self.request.GET['id']
        id2=self.request.GET['id2']
        user=Registration.objects.get(user_id=self.request.user.id)
        
        ser=Services.objects.get(id=id)
        ser.status='Booked'
        ser.save()
    
        rq=Requests()
        rq.user_id=user.id
        rq.services_id=id
        rq.provider_id=id2
        rq.status="Requested"
        rq.save()
        return redirect('/user')
    
class Profile(LoginRequiredMixin,TemplateView):
    template_name='customer/profile.html'
    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = Registration.objects.get(user_id=id1)
        context['profile'] = pro
        return context
class UpdateProfile(LoginRequiredMixin,TemplateView):
    template_name='customer/updpro.html'
    def get_context_data(self, **kwargs):
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        id3 = self.request.GET['id']
        pro = Registration.objects.get(id=id3)
        context['upd'] = pro
        return context

    def post(self, request, *args, **kwargs):
        id3 = self.request.GET['id']

        number = request.POST['number']
        address = request.POST['address']
        name = request.POST['name']
        district = request.POST['district']

        reg = Registration.objects.get(id=id3)# call the model
        reg.number=number
        reg.address=address
        reg.name=name
        reg.district=district
        reg.save()
        return render(request, 'customer/index.html',{'message':"Successfully Updated"})

class myrequests(LoginRequiredMixin,TemplateView):
    template_name='customer/myrequests.html'
    def get_context_data(self, **kwargs):
        context = super(myrequests, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = Registration.objects.get(user_id=id1)

        pro = Requests.objects.filter(user_id=pro.id)
        context['rqst'] = pro
        return context
class Performance(LoginRequiredMixin,TemplateView):
    template_name='customer/feedback.html'
    def get_context_data(self, **kwargs):
        context = super(Performance, self).get_context_data(**kwargs)
        pro = Services.objects.all()
        context['empl'] = pro
        return context
    

    def post(self, request, *args, **kwargs):
        abc=Registration.objects.get(user_id=self.request.user.id)

        star = request.POST['star']
        print('asdf',star)
        comment = request.POST['comment']
        employee=request.POST['empl']
        gg=Services.objects.get(id=employee)
        provider=gg.servicer_id
        reg = Rating()
        reg.star = star
        reg.comment=comment
        reg.provider_id=provider
        reg.user_id=abc.id
        reg.workers_id=employee
        reg.status='FeedBack Added'
        reg.save()
        return redirect('/user')

class PaymentView(TemplateView):
    template_name='customer/paymentview.html'
    def get_context_data(self, **kwargs):
        context = super(PaymentView, self).get_context_data(**kwargs)
        id1 = self.request.user.id
        pro = Registration.objects.get(user_id=id1)

        pro = Assign.objects.filter(user_id=pro.id,paymentstatus='Pay Amount')
        context['rqst'] = pro
        return context





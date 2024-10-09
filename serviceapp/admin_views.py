from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from serviceapp.models import Add_Services,Registration,ServicerRegistration
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


class index(LoginRequiredMixin,TemplateView):
    template_name='Admin/index.html'
class AddService(LoginRequiredMixin,TemplateView):
    template_name='admin/add_services.html'
    def post(self, request, *args, **kwargs):
        service_name = request.POST['name']
        if Add_Services.objects.filter(service_name=service_name).exists():
            messages.warning(request, "The service %s is already added." %service_name)
            return render(request, 'admin/message.html')     
        else:

            reg = Add_Services()
            reg.service_name = service_name
            reg.save()
            return redirect('admin:index')

class ViewServices(LoginRequiredMixin,TemplateView):
    template_name='admin/view_services.html'
    def get_context_data(self, **kwargs):
        view_services = Add_Services.objects.all()
        context = {
            'view_services':view_services
        }
        return context

class RemoveServices(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Add_Services.objects.get(id=id).delete()
        return redirect('/admin')
        

class ViewUsers(LoginRequiredMixin,TemplateView):
    template_name='admin/view_users.html'
    def get_context_data(self, **kwargs):
        view_users = Registration.objects.all()
        context = {
            'view_users':view_users
        }
        return context
    
class RemoveUsers(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Registration.objects.get(id=id).delete()
        return redirect('/admin')
class Viewservicers(LoginRequiredMixin,TemplateView):
    template_name='admin/view_servicers.html'
    def get_context_data(self, **kwargs):
        view_servicers = ServicerRegistration.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context = {
            'view_servicers':view_servicers
        }
        return context
class RemoveServiceProviders(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        User.objects.get(id=id).delete()
        return redirect('/admin')
class ApproveServiceProviders(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name = '1'
        user.save()
        return redirect('/admin',{'message':"Account Approved"})
class ViewapprovedServiceProviders(LoginRequiredMixin,TemplateView):
    template_name='admin/approvedmembers.html'
    def get_context_data(self, **kwargs):
        view_approve_servicers = ServicerRegistration.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context = {
            'view_approve_servicers':view_approve_servicers
        }
        return context
class RemoveSP(View):
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        User.objects.get(id=id).delete()
        return redirect('/admin')  

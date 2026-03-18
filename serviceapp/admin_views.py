from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from serviceapp.models import Add_Services,Registration,ServicerRegistration,Services,Assign
from django.db.models import Sum, Q
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse


class index(LoginRequiredMixin, TemplateView):
    template_name = 'Admin/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Calculate Statistics
        context['user_count'] = Registration.objects.count()
        context['provider_count'] = ServicerRegistration.objects.count()
        context['worker_count'] = Services.objects.count()
        
        # Calculate Total Revenue
        total_revenue = 0
        paid_assignments = Assign.objects.filter(paymentstatus='paid')
        for assignment in paid_assignments:
            try:
                total_revenue += float(assignment.amount)
            except (ValueError, TypeError):
                pass
        context['total_revenue'] = total_revenue
        
        return context

class AddService(LoginRequiredMixin, TemplateView):
    template_name = 'admin/add_services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetching all existing services to show them alongside the add form
        context['services'] = Add_Services.objects.all().order_by('-id')
        return context

    def post(self, request, *args, **kwargs):
        service_name = request.POST.get('name')
        if not service_name:
            return redirect('admin:add_service')
            
        if Add_Services.objects.filter(service_name=service_name).exists():
            messages.warning(request, "The service %s is already added." % service_name)
            return render(request, 'admin/message.html')     
        else:
            reg = Add_Services()
            reg.service_name = service_name
            reg.save()
            messages.success(request, "Service added successfully!")
            return redirect('admin:add_service')

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
        id = request.GET.get('id')
        if id:
            try:
                Add_Services.objects.get(id=id).delete()
            except Add_Services.DoesNotExist:
                pass
        return redirect('admin:add_service')
        

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
        id = request.GET.get('id')
        if id:
            try:
                # Get the registration record first to find the linked User
                reg = Registration.objects.get(id=id)
                if reg.user:
                    # Deleting the User object automatically removes the Registration 
                    # record due to the CASCADE on_delete rule
                    reg.user.delete()
                else:
                    reg.delete()
            except Registration.DoesNotExist:
                pass
        return redirect('admin:view_users')

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
        id = request.GET.get('id')
        if id:
           try:
                User.objects.get(id=id).delete()
           except User.DoesNotExist:
               pass
        return redirect('admin:view_servicers')

class ApproveServiceProviders(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET.get('id')
        if id:
            try:
                user = User.objects.get(pk=id)
                user.last_name = '1'
                user.save()
            except User.DoesNotExist:
                pass
        return redirect('admin:view_servicers')

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
        id = request.GET.get('id')
        if id:
            try:
                User.objects.get(id=id).delete()
            except User.DoesNotExist:
                pass
        return redirect('admin:ViewapprovedServiceProviders')

class RevenueReport(LoginRequiredMixin, TemplateView):
    template_name = 'admin/revenue_report.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        providers = ServicerRegistration.objects.all()
        report_data = []
        
        for p in providers:
            payments = Assign.objects.filter(provider_id=p.id, paymentstatus='paid')
            total = 0
            for pay in payments:
                try:
                    total += float(pay.amount)
                except (ValueError, TypeError):
                    pass
            
            report_data.append({
                'provider': p,
                'total_revenue': total,
                'job_count': payments.count()
            })
            
        context['report'] = report_data
        return context

class ViewProviderWorkers(LoginRequiredMixin, TemplateView):
    template_name = 'admin/provider_workers.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pid = self.request.GET.get('id')
        provider = ServicerRegistration.objects.get(id=pid)
        workers = Services.objects.filter(servicer_id=pid)
        context['provider'] = provider
        context['workers'] = workers
        return context

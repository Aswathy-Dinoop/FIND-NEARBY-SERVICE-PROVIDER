from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from serviceapp.models import Add_Services, Services, ServicerRegistration, Requests, Assign,Rating
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class index(LoginRequiredMixin,TemplateView):
    template_name='worker/index.html'
class view_works(LoginRequiredMixin,TemplateView):
    template_name = 'worker/view_works.html'
    def get_context_data(self, **kwargs):
        abc=Services.objects.get(user_id=self.request.user.id)
        xyz=Assign.objects.filter(services_id=abc.id,status='assigned')
        context={
            'xyz':xyz
        }
        return context
    def post(self, request, *args, **kwargs):
        id1 = request.POST['id'] 
        workstatus = request.POST['workstatus']
        reg = Assign.objects.get(id=id1)
        se=reg.request_id
        abc=Requests.objects.get(id=se)
        abc.status='Work Completed'
        abc.save()
        reg.workstatus = workstatus
        reg.status = "status updated"
        reg.save()
        return redirect('worker:view_works')
class completedworks(LoginRequiredMixin,TemplateView):
    template_name='worker/completed.html'
    def get_context_data(self, **kwargs):
        abc=Services.objects.get(user_id=self.request.user.id)
        xyz=Assign.objects.filter(services_id=abc.id,workstatus='Completed',paymentstatus='Null')
        context={
            'xyz':xyz
        }
        return context
    def post(self, request, *args, **kwargs):
        id=request.POST['id']
        id2=request.POST['id2']
        var=Assign.objects.get(id=id2)
        
        amount=request.POST['amount']
        # abc=Problems.objects.get(id=id2)
        var.paymentstatus='Pay Amount'
        var.amount=amount
        var.user_id=id
        var.save()
        return render(request, 'worker/index.html',{'message':"Amount Assigned"})


class pendingworks(LoginRequiredMixin,TemplateView):
    template_name='worker/pending.html'
    def get_context_data(self, **kwargs):
        abc=Services.objects.get(user_id=self.request.user.id)
        xyz=Assign.objects.filter(services_id=abc.id,workstatus='pending')
        context={
            'xyz':xyz
        }
        return context

class ViewFb(LoginRequiredMixin,TemplateView):
    template_name='worker/viewfb.html'
    def get_context_data(self, **kwargs):
        context = super(ViewFb, self).get_context_data(**kwargs)
        abc=Services.objects.get(user_id=self.request.user.id)

        pro = Rating.objects.filter(workers_id=abc.id)
        context['fb'] = pro
        return context
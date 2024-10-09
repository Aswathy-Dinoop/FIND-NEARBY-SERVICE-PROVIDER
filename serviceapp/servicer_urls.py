from django.urls import path
from serviceapp.servicer_views import index, CreateServices, ViewServices, RemoveServices, UpdateServices, ViewRequests, \
    Profile, Reject, Approve, assign,ViewFb,UpdateProfile,ViewPaymentLists

urlpatterns = [
    path('', index.as_view()),
    path('services',CreateServices.as_view()),
    path('view_services',ViewServices.as_view()),
    path('RemoveServices',RemoveServices.as_view()),
    path('update_services',UpdateServices.as_view()),
    path('myrequests',ViewRequests.as_view()),
    path('myprofile',Profile.as_view()),
    path('Reject',Reject.as_view()),
    path('Approve',Approve.as_view()),
    path('assign',assign.as_view()),
    path('viewfeedbacks',ViewFb.as_view()),
    path('updateprofile',UpdateProfile.as_view()),
    path('ViewPaymentLists',ViewPaymentLists.as_view()),

]
def urls():
    return urlpatterns, 'servicer','servicer'
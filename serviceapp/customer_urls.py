from django.urls import path
from serviceapp.customer_views import index,UpdateProfile,viewallservices,SendRequests,Profile,myrequests, \
Performance,SendRequestsForm,PaymentView
urlpatterns = [
    path('', index.as_view()),
    path('viewallservices',viewallservices.as_view()),
    path('requests',SendRequests.as_view()),
    path('myprofile',Profile.as_view()),
    path('myrequests',myrequests.as_view()),
    path('ratingpage',Performance.as_view()),
    path('updateprofile',UpdateProfile.as_view()),
    path('requestform',SendRequestsForm.as_view()),
    path('payment',PaymentView.as_view()),


]
def urls():
    return urlpatterns, 'customer','customer'
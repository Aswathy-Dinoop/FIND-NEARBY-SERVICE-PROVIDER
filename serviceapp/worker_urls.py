from django.urls import path
from serviceapp.worker_views import index, view_works,completedworks,pendingworks,ViewFb

urlpatterns = [
    path('', index.as_view()),
    path('view_works',view_works.as_view(),name='view_works'),
    path('completed',completedworks.as_view(),name="completed"),  
    path('pending',pendingworks.as_view(),name="pending"), 
    path('viewfb',ViewFb.as_view(),name="viewfb"),  
 

]
def urls():
    return urlpatterns, 'worker','worker'
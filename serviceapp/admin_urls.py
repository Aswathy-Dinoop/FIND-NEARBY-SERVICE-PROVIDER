from django.urls import path
from serviceapp.admin_views import index, AddService, ViewServices, ViewUsers, RemoveServices, RemoveUsers, \
    Viewservicers, RemoveServiceProviders,ApproveServiceProviders,ViewapprovedServiceProviders,RemoveSP

urlpatterns = [
    path('', index.as_view(),name="index"),
    path('add_service',AddService.as_view(),name="add_service"),
    path('view_service',ViewServices.as_view(),name="add_service"),
    path('view_users',ViewUsers.as_view(),name="view_users"),
    path('remove_service',RemoveServices.as_view(),name="remove_service"),
    path('remove_users',RemoveUsers.as_view(),name="remove_users"),
    path('view_servicers',Viewservicers.as_view(),name="view_servicers"),
    path('view_users',ViewUsers.as_view(),name="view_users"),
    path('removeservicers',RemoveServiceProviders.as_view()),
    path('ApproveServiceProviders',ApproveServiceProviders.as_view()),
    path('ViewapprovedServiceProviders',ViewapprovedServiceProviders.as_view()),
    path('RemoveSP',RemoveSP.as_view())
]
def urls():
    return urlpatterns, 'admin','admin'
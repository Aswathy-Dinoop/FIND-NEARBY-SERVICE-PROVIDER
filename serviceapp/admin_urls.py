from django.urls import path
from serviceapp.admin_views import index, AddService, ViewServices, ViewUsers, RemoveServices, RemoveUsers, \
    Viewservicers, RemoveServiceProviders,ApproveServiceProviders,ViewapprovedServiceProviders,RemoveSP, \
    RevenueReport, ViewProviderWorkers

urlpatterns = [
    path('', index.as_view(),name="index"),
    path('add_service',AddService.as_view(),name="add_service"),
    path('view_service',ViewServices.as_view(),name="view_service"),
    path('view_users',ViewUsers.as_view(),name="view_users"),
    path('remove_service',RemoveServices.as_view(),name="remove_service"),
    path('remove_users',RemoveUsers.as_view(),name="remove_users"),
    path('view_servicers',Viewservicers.as_view(),name="view_servicers"),
    path('view_users',ViewUsers.as_view(),name="view_users"),
    path('removeservicers',RemoveServiceProviders.as_view(),name="removeservicers"),
    path('ApproveServiceProviders',ApproveServiceProviders.as_view(),name="ApproveServiceProviders"),
    path('ViewapprovedServiceProviders',ViewapprovedServiceProviders.as_view(),name="ViewapprovedServiceProviders"),
    path('RemoveSP',RemoveSP.as_view(),name="RemoveSP"),
    path('RevenueReport', RevenueReport.as_view(), name="RevenueReport"),
    path('ViewProviderWorkers', ViewProviderWorkers.as_view(), name="ViewProviderWorkers"),
]
def urls():
    return urlpatterns, 'admin','admin'
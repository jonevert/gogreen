from django.urls import path
from . import views

urlpatterns = [
    # path('', views.most_instances, name="activity-index"),
    # path('<slug:plate_nr>', views.most_instances, name="activity-specific-index")
    path('', views.index, name="activity-index"),
    path('<int:instance_pk>', views.instance_info, name="activity-specific-index")
]
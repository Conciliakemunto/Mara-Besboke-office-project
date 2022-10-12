from mara.views import index
from django.urls import path
from mara.views import about
from django.urls import path


urlpatterns=[ 
    path('', index)
]
urlpatterns=[
    path('', about)
]
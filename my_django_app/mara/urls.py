from django.contrib import admin
from mara.views import index, about, contact,signup,signin,signout
from django.urls import path



urlpatterns=[ 
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact,name='contact'),
    path('signup', signup, name='signup'),
    path('signin', signin, name='signin'),
    path('signout', signout, name='signout'),
]
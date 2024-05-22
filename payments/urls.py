from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.home, name='home'),
    path('pay', views.payment_gateway, name='pay'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel')
]

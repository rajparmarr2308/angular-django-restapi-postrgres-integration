from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register('data',views.FormViewSet)
urlpatterns = [
    url('',include(router.urls)),
    # path('data/',form_list),
]

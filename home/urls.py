from django.urls import path

from .views import RunNGSpiceCodeView

urlpatterns = [
    path('run_ngspice', RunNGSpiceCodeView.as_view(), name='runngspice'),

]

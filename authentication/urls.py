from django.urls import path

from .views import FacultyRegisterView, StudentRegisterView

urlpatterns = [
    # path('auth/student/login', ObtainAuthToken.as_view(), name='login'),
    path('auth/student/register', StudentRegisterView.as_view(),
         name='StudentRegisterView'),
    path('auth/faculty/register', FacultyRegisterView.as_view(),
         name='FacultyRegisterView'),
    # path('config', Config.as_view(), name='Config'),

]

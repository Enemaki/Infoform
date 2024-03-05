from django.urls import path

from .views import InformationFormView, HomePageView, SuccessView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('new/', InformationFormView.as_view(), name='info'),
    path('success/', SuccessView.as_view(), name='success')
]

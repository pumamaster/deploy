from django.urls import path
from .views import Index, Index2, ContactView

urlpatterns = [
    path('', Index.as_view(), name='index'),  
    path('index/', Index2.as_view(), name='index2'),  
    path('contact/', ContactView.as_view(), name='contact'),  
]
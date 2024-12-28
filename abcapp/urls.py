
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('category/<int:category_id>/',views.home,name='filter_by_category'),
    path('sample',views.sample,name='sample'),
    path('user-product/',views.user_product,name='user_product'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
]
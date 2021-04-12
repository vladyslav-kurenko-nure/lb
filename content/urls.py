from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', LinkListView.as_view(), name='home'),
    path('addpage/', LinkCreateView.as_view(), name='add_page'),
    path('deletepage/<slug:post_slug>/', LinkDeleteView.as_view(), name='delete_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', LinkDetailView.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CategoryListView.as_view(), name='category'),
    path('open/', countofclick, name='open')
]

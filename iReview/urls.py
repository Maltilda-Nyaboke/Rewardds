from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('new_project/', views.new_project, name='new_project'),
    path('search/', views.search_results, name='search'),
    path('logout/', views.logout, name='logout'),
    path('api/profile/', views.ProfileList.as_view(), name=''),
    path('api/project/', views.ProjectList.as_view(), name=''),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

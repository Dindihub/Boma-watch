from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',views.index,name = 'index'),
    path('register',views.register,name='register'),
    path('login',views.login_in,name='login'),
    path('logout',views.log_out,name='logout'),
    path('home',views.home,name='home'),
    path('profile',views.profile,name='profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('create-hood', views.create_hood, name='create_hood'),
    path ('join_hood/<str:id>/',views.join_hood,name='join_hood'),
    # path('hoods', views.hoods, name='hood'),
    # path('upload_project', views.upload_project, name='upload_project'),
    # path('search', views.project_search, name='search'),

    

]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
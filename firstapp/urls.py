from django.urls import path
from . import views


app_name='first_app'
urlpatterns=[
    path('',views.home_view,name='home'),
    #path('startupregistration/',views.startupRegistration,name='startupRegistration'),
    #path('capitalistregistration/', views.capitalistRegistration,name='capitalistRegistration'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('<int:choice>/<int:id>/afterlogin/', views.after_login, name='after_login'),
]

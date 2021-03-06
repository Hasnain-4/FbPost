from django.urls import path, include
from fb1 import views

urlpatterns = [
    path('', views.home , name = 'home'),
    path('sign_up', views.signup , name = 'signup'),
    path('signin', views.signin , name = 'signin'),
    path('forgetpassword', views.forget , name = 'forget'),
    path('about', views.about , name = 'about'),
    path('contact', views.contact , name = 'contact'),
    path('logout', views.logout,name='logout'),
    path('fbuser', views.fbuser,name='fbuser'),
    path('imagepost', views.imagepost,name='imagepost'),
    path('videopost', views.videopost,name='videopost'),
    path('posts', views.posts,name='posts'),
    path('editimagepost', views.imagepost,name='imagepost'),
    path('editvideopost', views.videopost,name='videopost'),
    path('editprofile', views.editprofile,name='editprofile'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('dlt/<id>',views.delete_postv,name='dlt'),
    
    
]
from django.urls import path     
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('register', views.register),
    path('log', views.log),
    path('login', views.login),
    path('create_wedding', views.create_wedding),
    path('add_wedding', views.add_wedding),
    path('create_registry', views.create_registry),
    path('add_registry/<int:user_id>', views.add_registry),
    path('wedding/<int:user_id>', views.wedding),
    path('contribute/<int:registry_id>', views.contribute),
    path('my_account/<int:user_id>', views.my_account),
    path('edit_account/<int:user_id>', views.edit_account),
    path('make_contribution/<int:registry_id>', views.make_contribution),
    path('success', views.success),
    path('registry/<int:user_id>', views.registry),
    path('details/<int:user_id>', views.details),
    path('posts/<int:user_id>', views.posts),
    path('make_post/<int:user_id>', views.make_post),
    path('posts/like_post/<int:post_id>/<int:user_id>', views.like_post),
    path('posts/unlike_post/<int:post_id>/<int:user_id>', views.unlike_post),
    path('search', views.search),
    path('my_wedding/<int:wedding_id>', views.my_wedding),
    path('edit_wedding/<int:wedding_id>/<int:user_id>', views.edit_wedding),
    path('delete_wedding/<int:wedding_id>', views.delete_wedding),
    path('delete_wedding/<int:wedding_id>', views.delete_wedding),
    path('logout', views.logout)
]
urlpatterns += staticfiles_urlpatterns()
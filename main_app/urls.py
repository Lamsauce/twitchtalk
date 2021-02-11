from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('games/', views.games, name='games'),
    path('accounts/profile/', views.profile, name='profile'),
    path('<int:thread_id>/', views.thread, name='thread'),
    path('addthread/', views.addthread, name='addthread'),
    path('<int:thread_id>/edit', views.editthread, name='editthread'),
    path('<int:thread_id>/delete', views.deletethread, name='deletethread'),
    path('games/<int:game_id>/', views.showgame, name='showgame')
]


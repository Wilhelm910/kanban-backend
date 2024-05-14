"""
URL configuration for kanbanboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from board.views import BoardDetailView, BoardView, CreateUserView, CurrentUserView, LoginView, TaskView, UpdateTaskView, UserListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    # path('board/', TaskView.as_view()),
    # path('createTask/', CreateTaskView.as_view()),
    
    # path('createBoard/', CreateBoardView.as_view()),
    path('createUser/', CreateUserView.as_view()),
    path('userlist/', UserListView.as_view()),
    path('updateTask/<int:pk>/', UpdateTaskView.as_view()),
    path('getCurrentUser/', CurrentUserView.as_view()),
  
    # path('allboard/', AllBoardsView.as_view()),
    
    path('tasks/', TaskView.as_view()),
    path('boards/', BoardView.as_view()),
    path('board/<int:pk>/', BoardDetailView.as_view()),
    
    
    #  path('users/', UserView.as_view(), name='user-list-create'),
    # path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
    # path('users/current/', UserView.as_view(), {'pk': 'current'}, name='current-user'),
]

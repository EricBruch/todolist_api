from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from todo.views import TodoViewSet, login_view, register_view
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('login/', login_view),
    path('register/', register_view),
    path('admin/', admin.site.urls),
]

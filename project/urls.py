from django.contrib import admin
from django.urls import path

from apps.user import views as userViews
from apps.note import views as noteViews

from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('',noteViews.HomeView.as_view(),name='home'),
    path('add/',noteViews.AddNoteView.as_view(),name='add'),
    path('register/',userViews.RegisterView.as_view(), name='register'),
    path('delete/<int:pk>/',noteViews.DeleteView.as_view(),name='delete'),
    path('update/<int:pk>/',noteViews.UpdateView.as_view(),name='update'),
]

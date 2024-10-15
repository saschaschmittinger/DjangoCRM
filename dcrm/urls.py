from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from leads.views import SignUpView
 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace='leads')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signUp')
 
]
 
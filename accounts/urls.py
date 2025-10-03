from django.urls import path
from django.urls import reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("registro/", views.registro, name="registro"),
    path("perfil/", views.perfil, name="perfil"),
    path("perfil/editar/", views.editar_perfil, name="editar_perfil"),
    path("password_change/",auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html",success_url=reverse_lazy("accounts:password_change_done")), name="password_change"),
    path("password_change/done/",auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"),name="password_change_done"),   
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
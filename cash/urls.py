from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from money import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', views.list, name='list'),
    path('detail/<int:business_id>/', views.detail,name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:business_id>/', views.update, name='update'),
    path('delete/<int:business_id>/', views.delete, name='delete'),
    path('login/', views.userlogin, name='login'),
    path('logout/', views.userlogout, name='logout'),
    path('signup/', views.signup, name='signup'),

    ]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


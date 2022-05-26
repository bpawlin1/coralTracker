from django.urls import path
from coral import views
from .views import  CreateCoralView # new
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 
    path("", views.index, name="index"),
    path("<int:pk>/", views.coral_detail, name="coral_detail"),
    path("newCoral/", CreateCoralView.as_view(), name="newCoral"),
    path("<int:pk>/coralUpdate", views.UpdateCoralView.as_view(),name="coralUpdate"),
    path("<int:pk>/coralDelete",views.DeleteCoralView.as_view(),name="coralDelete"),
] 

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)







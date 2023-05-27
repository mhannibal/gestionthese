from django.urls import path
from .views import CustomUserCreate, UserInformationsViewSet

app_name = 'users'

# urlpatterns = [
#     path('create/<int:id>', CustomUserCreate.as_view(), name="create_user"),
# ]
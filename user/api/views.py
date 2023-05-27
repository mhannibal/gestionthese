from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserInfoSerializer#, UserActivationSerializer,  CustomUserSerializer,
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from user.models import User
from rest_framework import viewsets, status


class UserInformationsViewSet(viewsets.ModelViewSet):
    serializer_class = UserInfoSerializer
    def get_queryset(self):
        return  User.objects.all()



# class UserViewSet(viewsets.ModelViewSet):
#     serializer_class = CustomUserSerializer
#     def get_queryset(self):
#         return  User.objects.all()

# class CustomUserCreate(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request, format='json'):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, format='json'):
#         serializer = UserActivationSerializer(data=request.data)
#         if serializer.is_valid():
#             user = User.objects.get(pk=serializer.data["id"])
#             user.is_active = serializer.data["is_active"]
#             user.is_staff = serializer.data["is_staff"]
#             user.save()
#             if user:
#                 json = UserActivationSerializer(user).data
#                 return Response(json, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id=None):
        
#         print(id)
#         user = User.objects.get(pk=id)
#         if user:
#             json = {"id": user.pk }
#             user.delete()
#             return Response(json, status=status.HTTP_204_NO_CONTENT)
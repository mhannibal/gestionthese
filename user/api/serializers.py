from rest_framework import serializers
from user.models import User


# class CustomUserSerializer(serializers.ModelSerializer):
#     """
#     Currently unused in preference of the below.
#     """
#     email = serializers.EmailField(required=True)
#     user_name = serializers.CharField(required=True)
#     first_name = serializers.CharField(required=True)
#     last_name = serializers.CharField(required=True)
#     password = serializers.CharField(min_length=8, write_only=True)

#     class Meta:
#         model = User
#         fields = ('email', 'user_name', 'password', 'first_name', 'last_name')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         password = validated_data.pop('password', None)
#         # as long as the fields are the same, we can just use this
#         instance = self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance



class UserInfoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


# class UserActivationSerializer(serializers.ModelSerializer):    
#     id = serializers.IntegerField()

#     class Meta:
#         model = User
#         fields = 'id', 'is_active', 'is_staff'
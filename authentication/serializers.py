from django.contrib.auth.models import User
from rest_framework import serializers


class CreateStudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    username = serializers.CharField(min_length=6, required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


class CreateFacultySerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    username = serializers.CharField(min_length=6, required=True)
    password = serializers.CharField(
        min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.is_staff = True
        user.save()
        return user

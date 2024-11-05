from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import HttpResponse, redirect, render
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CreateStudentSerializer


class StudentCreateView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):

        serializer = CreateStudentSerializer(data={
            'full_name': request.data.get('full_name').title() if request.data.get('full_name') else None,
            'email': request.data.get('email'),
            'password': request.data.get('password'),
        })

        if serializer.is_valid():
            try:
                created_user = serializer.save()
                created_user.groups.add(Group.objects.get(name='Student'))
                refresh = RefreshToken.for_user(created_user)
                return Response(data={"success": "true", "message": "Student Created.", "refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={"success": "false", "message": str(e).title()})
        else:
            return Response(data={"success": "false", "message": str(serializer.errors)})


class ObtainAuthToken(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        user_instance = authenticate(email=request.data.get(
            'email'), password=request.data.get('password'))
        if user_instance is not None:
            refresh = RefreshToken.for_user(user_instance)
            return Response(data={"success": "true", "refresh": str(refresh), "access": str(refresh.access_token)}, status=status.HTTP_200_OK)
        else:
            return Response(data={"success": "false", "message": "User Not Found."})

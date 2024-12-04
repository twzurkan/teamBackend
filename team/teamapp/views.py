from django.shortcuts import render

# Create your views here.
from teamapp.models import Member
from teamapp.serializer import MemberSerializer

from rest_framework import generics


class MemberList(generics.ListCreateAPIView):
    # Simply use generics here for my list view that includes GET and POST
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    # Simply use generics here for my detail view that includes GET,PUT,DELETE
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

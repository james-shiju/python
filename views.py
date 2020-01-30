from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Contact, IContact
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets

from rest_framework import serializers

class Contact(object):
    def __init__(self, email, content, created=None):
        self.name = name
        self.age = age
        self.phone = phone
        # self.email = email

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    phone = serializers.IntegerField()
    class Meta:
        model = Contact



# # Create your views here.
# def index(request):
#     c = Contact.objects.all()
#     # res = Contact(name=c.name, age=c.age, phone=c.phone)
#     res = Contact(c, many=True)
#     return HttpResponse(JSONRenderer().render(serializer.data))

class ContactViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

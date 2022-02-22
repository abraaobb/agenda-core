from rest_framework import viewsets
from core import models, serializers

class ContactViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()
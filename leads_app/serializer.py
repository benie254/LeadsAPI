from rest_framework import serializers 
from leads_app.models import Subscriber, Contact


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber 
        fields = ('id','__all__')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact 
        fields = ('id','__all__')
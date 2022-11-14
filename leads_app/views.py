from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework.views import APIView 
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status 

import sendgrid
from sendgrid.helpers.mail import * 
from decouple import config 

from leads_app.models import Subscriber, Contact
from leads_app.serializer import SubscriberSerializer, ContactSerializer

# Create your views here.
class AllSubscribers(APIView):
    permission_classes = (IsAdminUser,IsAuthenticated)
    def get(self,request,format=None):
        subscribers = Subscriber.objects.all().order_by('date_subscribed')
        serializers = SubscriberSerializer(subscribers,many=True)
        return Response(serializers.data)

    permission_classes = (AllowAny)
    def post(self,request,format=None):
        serializers = SubscriberSerializer(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data['name']
            email = serializers.validated_data['email']
            serializers.save()
            sg = sendgrid.SendGridAPIClient(api_key=config('SENDGRID_API_KEY'))
            msg = render_to_string('email/new-subscriber.html', {
                'name': name,
                'email': email,
            })
            message = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = 'heartsnart.ke@gmail.com',
                subject = "New Subscriber",
                html_content='<p>Hello, benie,' + msg
            )
            msg2 = render_to_string('email/welcome-subscriber.html', {
                'name': name,
                'email': email,
            })
            message = Mail(
                from_email = Email("davinci.monalissa@gmail.com"),
                to_emails = email,
                subject = "Welcome",
                html_content='<p>Hello,' + str(name) + ',' + msg2
            )
            try:
                sendgrid_client = sendgrid.SendGridAPIClient(config('SENDGRID_API_KEY'))
                response = sendgrid_client.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e)
            status_code = status.HTTP_201_CREATED
            response = {
                'success' : 'True',
                'status code' : status_code,
                'message': 'Email report sent  successfully',
                }
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
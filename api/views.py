from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers


class AnnouncementView(APIView):
    def get(self, request):
        announcements = models.Announcement.objects.all().order_by("-date_created")
        if not announcements.exists():
            return Response({"error": "No announcements found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FaqView(APIView):
    def get(self, request):
        faqs = models.Faqs.objects.all().order_by('-date_created')[:8]
        if not faqs.exists():
            return Response({"error": "No FAQs found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.FaqSerializer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ContactView(APIView):
    def post(self,request):
        name = request.data.get('name')
        email = request.data.get('email')
        phoneNumber = request.data.get('phonenumber')
        message = request.data.get('message')
        
        contact = models.Contact.objects.create(name=name,email=email,phone_number=phoneNumber,message = message)
        contact.save()
        
        return Response({"message":"message sent"}, status = status.HTTP_201_CREATED)



class BlogView(APIView):
    def get(self, request):
        blog = models.Blog.objects.all().order_by('-date_created')[:5]
        if not blog.exists():
            return Response({"error": "No blogd found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.BlogSerializer(blog, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TeamView(APIView):
    def get(self,request):
        team = models.Team.objects.all().order_by("-id")
        if not team.exists():
            return Response({"erro:":"no team found"},status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.TeamSerializer(team, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)
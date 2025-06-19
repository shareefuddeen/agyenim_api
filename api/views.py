from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from django.core.cache import cache
from django.http import JsonResponse



class AnnouncementView(APIView):
    def get(self, request):
        
        data = cache.get("announcement_list")
        if data:
            announcements = data
        else:
            queryset = models.Announcement.objects.all().order_by("-date_created")
            if not queryset.exists():
                return Response({"error": "No announcements found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.AnnouncementSerializer(queryset, many=True)
            announcements = serializer.data
            cache.set('announcement_list',announcements)
        return Response(announcements, status=status.HTTP_200_OK)


class FaqView(APIView):
    def get(self, request):
        data = cache.get('faqs_list')
        if data:
            faqs = data
        else:
            queryset = models.Faqs.objects.all().order_by('-date_created')[:8]
            if not queryset.exists():
                return Response({"error": "No FAQs found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.FaqSerializer(queryset, many=True)
            faqs = serializer.data
            cache.set('faqs_list')
        return Response(faqs, status=status.HTTP_200_OK)

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
        data = cache.get('blogs_view')
        if data:
            blogs = data
        else:
            queryset = models.Blog.objects.all().order_by('-date_created')[:5]
            if not queryset.exists():
                return Response({"error": "No blogd found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.BlogSerializer(queryset, many=True)
            blogs = serializer.data
        return Response(blogs, status=status.HTTP_200_OK)
    
class TeamView(APIView):
    def get(self,request):
        data = cache.get('team_list')
        if data:
            team =data
        else:
            queryset = models.Team.objects.all().order_by("-id")
            if not queryset.exists():
                return Response({"erro:":"no team found"},status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.TeamSerializer(queryset, many =True)
            team = serializer.data
        return Response(team, status=status.HTTP_200_OK)


# testing caching
def redis_test_view(request):
    cache.set('redis_test_key', 'Redis is working!', timeout=60)
    value = cache.get('redis_test_key')
    return JsonResponse({'message': value})
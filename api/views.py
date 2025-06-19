from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
from django.core.cache import cache
from django.http import JsonResponse
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

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
            cache.set('faqs_list',faqs)
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
        data = cache.get('blogs_list')
        if data:
            blogs = data
        else:
            queryset = models.Blog.objects.all().order_by('-date_created')[:5]
            if not queryset.exists():
                return Response({"error": "No blogd found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = serializers.BlogSerializer(queryset, many=True)
            blogs = serializer.data
            cache.set('blog_list',blogs)
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
            serializer = serializers.TeamSerializer(queryset, many =True,context={"request": request})
            team = serializer.data
            cache.set('team_list',team)
        return Response(team, status=status.HTTP_200_OK)



# testing caching
def redis_test_view(request):
    cache.set('redis_test_key', 'Redis is working!', timeout=60)
    value = cache.get('redis_test_key')
    return JsonResponse({'message': value})

#signals
@receiver(post_save, sender=models.Announcement)
@receiver(post_delete,sender=models.Announcement)
def clear_cache(sender,instance,**kwargs):
    cache.delete('announcement_list')
    

@receiver(post_save, sender=models.Faqs)
@receiver(post_delete,sender=models.Faqs)
def clear_cache(sender,instance,**kwargs):
    cache.delete('faqs_list')
    
@receiver(post_save, sender=models.Blog)
@receiver(post_delete,sender=models.Blog)
def clear_cache(sender,instance,**kwargs):
    cache.delete('blog_list')
    
@receiver(post_save, sender=models.Team)
@receiver(post_delete,sender=models.Team)
def clear_cache(sender,instance,**kwargs):
    cache.delete('team_list')
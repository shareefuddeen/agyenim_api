from rest_framework import serializers
from . import models

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Announcement
        fields = "__all__"


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faqs
        fields = "__all__"
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields ="__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields ="__all__"
        
        
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = "__all__"
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
    image = serializers.SerializerMethodField()
    class Meta:
        model = models.Team
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
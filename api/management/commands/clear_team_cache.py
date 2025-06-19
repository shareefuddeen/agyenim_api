from django.core.management.base import BaseCommand
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Clear the team_list cache'

    def handle(self, *args, **kwargs):
        cache.delete('team_list')
        self.stdout.write(self.style.SUCCESS('✅ team_list cache cleared!'))

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Creates an initial superuser if none exists."

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="adminpassword123"
            )
            self.stdout.write(self.style.SUCCESS('Superuser "admin" created.'))
        else:
            self.stdout.write('Superuser "admin" already exists.')

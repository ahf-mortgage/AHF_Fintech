from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Creates users from a text file'

    # def add_arguments(self, parser):
    #     # parser.add_argument('file_path', type=str, help='Path to the text file')

    def handle(self, *args, **options):
        all_users = User.objects.all()
        for user in all_users:
            print("user= ",user)
            user.set_password("123456")
            user.save()


      
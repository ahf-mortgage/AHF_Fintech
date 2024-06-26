from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Creates users from a text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the text file')

    def handle(self, *args, **options):
        file_path = options['file_path']

        with open(file_path, 'r') as file:
            for line in file:
                username, password = line.strip().split(' ')
                user = User.objects.filter(username=username).first()
                print("user=",user)
                if user == None:
                    User.objects.create_user(username=username,password=password)
                else:
                    User.objects.create_user(username=f"{username}_{random.randint(1,1000000)}",password=password)
                self.stdout.write(f'Created user: {username}')
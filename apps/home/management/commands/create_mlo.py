from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT
import random

class Command(BaseCommand):
    help = 'Creates mlo from a text file'
    def handle(self, *args, **options):
        users = User.objects.all()
        mlo_id = 30010


        for user in users:
            mlo = MLO_AGENT.objects.filter(user = user).first()
            if mlo == None:
                MLO_AGENT.objects.create(user=user,NMLS_ID = mlo_id)
            else:
                continue
            mlo_id += 1
            self.stdout.write(f'Created mlo: {mlo}')
                
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import Bps,CompPlan
import random

class Command(BaseCommand):
    help = 'update users from a text file'

    def handle(self, *args, **options):
        cps = CompPlan.objects.all()
        for c in cps:
            print("complan = ",c)
            c.Maximum_Compensation = 27500
            c.Flat_Fee = 0
            

            c.save()
            

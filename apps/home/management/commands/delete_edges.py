from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Edge,Node
import random

class Command(BaseCommand):
    help = 'Creates edges from a text file'
    def handle(self, *args, **options):
        all_edges = Edge.objects.all()

        for edge in all_edges:
            print("edge = ",edge)
            edge.delete()         

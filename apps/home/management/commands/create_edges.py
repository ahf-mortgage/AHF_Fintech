from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Edge,Node
import random

class Command(BaseCommand):
    help = 'Creates edges from a text file'
    def handle(self, *args, **options):
        nodes        = Node.objects.all()
        edges        = Edge.objects.all()
        counter      = 110015
        start_mlo    = MLO_AGENT.objects.all()[1]
        start_node   = Node.objects.filter(mlo_agent = start_mlo).first()

        for node in nodes[::2]:
            Edge.objects.create(source_node=start_node,target_node=node,edge_id=counter)
            counter += 1
        self.stdout.write(f'Created edge: {len(nodes)}')
     
                    
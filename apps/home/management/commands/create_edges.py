from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Edge,Node
import random

class Command(BaseCommand):
    help = 'Creates edges from a text file'
    def handle(self, *args, **options):
        nodes        = Node.objects.all()
        edges        = Edge.objects.all()
        counter      = 63
        start_mlo    = MLO_AGENT.objects.all()[1]
        start_node   = Node.objects.filter(mlo_agent__user__username="JohnDoe42_535801").first()

        for node in nodes[67:73]:
            print("mlo created = ",node)
            edge = Edge.objects.create(source_node=start_node,target_node=node,edge_id = counter)
            # edge.delete()
            counter += 1
        self.stdout.write(f'Created edge')
     
                    
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Edge,Node
import random

class Command(BaseCommand):
    help = 'Creates edges from a text file'
    def handle(self, *args, **options):
        nodes = Node.objects.all()[160:200]
        edges = Edge.objects.all()[101:150]
        counter = 110000
        ashaton_4 = MLO_AGENT.objects.filter(user__username = "ashaton_4").first()
        ashaton_3_node = Node.objects.filter(mlo_agent=ashaton_4).first()

        for edge,node in zip(edges,nodes):
            Edge.objects.create(source_node=ashaton_3_node,target_node=node,edge_id=counter)
            counter += 1
        
        self.stdout.write(f'Created edge: {len(nodes)}')
     
                    
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Node
import random

class Command(BaseCommand):
    help = 'Creates Node from a text file'
    def handle(self, *args, **options):
        mlo_agents = MLO_AGENT.objects.all()
        node_id = 3049


        for agent in mlo_agents:
            node = Node.objects.filter(mlo_agent=  agent).first()
            if node == None:
                Node.objects.create(mlo_agent=agent,node_id = node_id)
            else:
                continue
            node_id += 1
            self.stdout.write(f'Created Node: {node_id - 1}')
                
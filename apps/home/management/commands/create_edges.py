from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Edge,Node
import random

class Command(BaseCommand):
    help = 'Creates edges from a text file'
    def handle(self, *args, **options):
        all_nodes        = Node.objects.all()
        start_node   = Node.objects.filter(mlo_agent__user__username="AHF").first()

        parent_nodes = all_nodes[::6]
        result = []
        all_edges = Edge.objects.all()


        for edge in all_edges:
            print("edge = ",edge)
            edge.delete()         


        for i in range(0, len(all_nodes), 6):
            Edge.objects.create(source_node = all_nodes[i],target_node = all_nodes[i + 1])
            k = 2
            while k < 7:
                Edge.objects.create(source_node = all_nodes[i+1],target_node = all_nodes[i + k])


                Edge.objects.create(source_node = all_nodes[i+k],target_node = all_nodes[i + k+27])
                Edge.objects.create(source_node = all_nodes[i+k],target_node = all_nodes[i + k+28])
                Edge.objects.create(source_node = all_nodes[i+k],target_node = all_nodes[i + k+29])
                Edge.objects.create(source_node = all_nodes[i+k],target_node = all_nodes[i + k+30])
                Edge.objects.create(source_node = all_nodes[i+k],target_node = all_nodes[i + k+31])




                Edge.objects.create(source_node = all_nodes[i+k+2],target_node = all_nodes[i + k+6])
                Edge.objects.create(source_node = all_nodes[i+k+2],target_node = all_nodes[i + k+7])
                Edge.objects.create(source_node = all_nodes[i+k+2],target_node = all_nodes[i + k+8])
                Edge.objects.create(source_node = all_nodes[i+k+2],target_node = all_nodes[i + k+9])
                Edge.objects.create(source_node = all_nodes[i+k+2],target_node = all_nodes[i + k+10])



                Edge.objects.create(source_node = all_nodes[i+1],target_node = all_nodes[i + k+1])

                Edge.objects.create(source_node = all_nodes[i+k+1],target_node = all_nodes[i + k+11])
                Edge.objects.create(source_node = all_nodes[i+k+1],target_node = all_nodes[i + k+12])
                Edge.objects.create(source_node = all_nodes[i+k+1],target_node = all_nodes[i + k+13])
                Edge.objects.create(source_node = all_nodes[i+k+1],target_node = all_nodes[i + k+14])
                Edge.objects.create(source_node = all_nodes[i+k+1],target_node = all_nodes[i + k+15])





                Edge.objects.create(source_node = all_nodes[i+1],target_node = all_nodes[i + k+2])



                Edge.objects.create(source_node = all_nodes[i+1],target_node = all_nodes[i + k+4])
                Edge.objects.create(source_node = all_nodes[i+k+4],target_node = all_nodes[i + k+16])
                Edge.objects.create(source_node = all_nodes[i+k+4],target_node = all_nodes[i + k+17])
                Edge.objects.create(source_node = all_nodes[i+k+4],target_node = all_nodes[i + k+18])
                Edge.objects.create(source_node = all_nodes[i+k+4],target_node = all_nodes[i + k+19])
                Edge.objects.create(source_node = all_nodes[i+k+4],target_node = all_nodes[i + k+20])


                Edge.objects.create(source_node = all_nodes[i+1],target_node = all_nodes[i + k+5])

                Edge.objects.create(source_node = all_nodes[i+k+5],target_node = all_nodes[i + k+21])
                Edge.objects.create(source_node = all_nodes[i+k+5],target_node = all_nodes[i + k+22])
                Edge.objects.create(source_node = all_nodes[i+k+5],target_node = all_nodes[i + k+23])
                Edge.objects.create(source_node = all_nodes[i+k+5],target_node = all_nodes[i + k+24])
                Edge.objects.create(source_node = all_nodes[i+k+5],target_node = all_nodes[i + k+25])



                break
             
                k += 1

            break
        
    
         

       
    
       

 
                    
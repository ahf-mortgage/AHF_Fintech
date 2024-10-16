import random
import string
from django import forms
from django.forms import Select
from .models import MLO_AGENT,LoanAmount,Edge,Node


def generate_random_alphanumeric_strings(count=5, length=6):
    alphanumeric_chars = string.ascii_letters + string.digits
    return [''.join(random.choices(alphanumeric_chars, k=length)) for _ in range(count)][0]





class EdgeForm(forms.ModelForm):

  
    def available_nodes(self):
        # Get all node IDs that are used in edges
        used_node_ids = Edge.objects.values_list('source_node', flat=True).union(
            Edge.objects.values_list('target_node', flat=True)
        )
        available_nodes = Node.objects.exclude(node_id__in=used_node_ids)
        print("used in available_nodes id ",available_nodes)
        return available_nodes


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['source_node'].initial = self.available_nodes()
        


    class Meta:
    
        model = Edge
        fields = "__all__"
        widgets = {
            'edge_id':forms.NumberInput(attrs={'maxlength':100,"disabled":"disable"}),
            'source_node': forms.Select(attrs={'maxlength':100,"disabled":"disable"}),
            'target_node': forms.Select(attrs={'maxlength':100}),
        
        }
   


class MloFrom(forms.ModelForm):

    class Meta:
        CHOICES = [
        ('1', 'Choice 1'),
        ('2', 'Choice 2'),
        ('3', 'Choice 3'),
    ]
        model = MLO_AGENT
        fields = "__all__"
        # exclude = "user",
        widgets = {
            'NMLS_sponsor_id': forms.TextInput(attrs={'maxlength':100,'readonly':True,"value":generate_random_alphanumeric_strings()}),
            'NMLS_ID': forms.TextInput(attrs={'maxlength':100,'readonly':True,"value":generate_random_alphanumeric_strings()}),
          

        }

    



class LoanAmountFrom(forms.ModelForm):

    class Meta:
        model = LoanAmount
        fields = "__all__"

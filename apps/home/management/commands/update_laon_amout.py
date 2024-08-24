from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan,LoanAmount
import random
import datetime

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)
commands = [2450,2375,1125,1000000,500000,400000]
class Command(BaseCommand):
    help = 'Creates mlo from a text file'
    def handle(self, *args, **options):
        loans = LoanAmount.objects.all()
     
        index = 1
        
        for ln in loans:
            ln.File_reference = f"31{index} Sunny street, California 23772"
            ln.loan_amount =  random.choice(commands)
            index += 1
            print("ln=",ln.File_reference)
            ln.save()

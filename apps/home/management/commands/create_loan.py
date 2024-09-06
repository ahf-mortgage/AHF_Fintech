from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan
import random
import datetime

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)



class Command(BaseCommand):
   
    help = 'Creates mlo from a text file'
    def handle(self, *args, **options):
        mlo_agents = MLO_AGENT.objects.filter(user__username__startswith = "William")
        mlo_id = 30090
        index = 80


        for agent in mlo_agents:
           Loan.objects.create(mlo_agent = agent,bps=2.75,File_reference=f"12{index} Any street, California 97720")#,date_closed = one_year_ago)
           index += 1
           self.stdout.write(f'Created mlo: {mlo_agents}')
                
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan,LoanAmount
import random
import datetime

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)



class Command(BaseCommand):
    help = 'Creates mlo from a text file'
    def handle(self, *args, **options):
        mlo_agents = MLO_AGENT.objects.all()
        mlo_id = 30010


        for i in range(1,100):
           LoanAmount.objects.create(loan_amount = 100 + i,loan_date = today,repayment_date = today, status= "paid")#,date_closed = one_year_ago)
           self.stdout.write(f'Created mlo: {mlo_agents}')
                
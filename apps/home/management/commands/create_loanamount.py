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
        loan_amounts = LoanAmount.objects.all()
        random_loan_amount = [num for num in range(100000,2000000)]
        for amount in loan_amounts:
           
            amount.loan_amount = random.choice(random_loan_amount)
            amount.save()
                
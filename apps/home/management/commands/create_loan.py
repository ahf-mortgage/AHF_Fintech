from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.recruiter.models import MLO_AGENT,Loan,LoanAmount
import random
import datetime
from django.utils import timezone

# Get the current date
today = datetime.date.today()

# Calculate the date from one year ago
one_year_ago = today.replace(year=today.year - 1)



class Command(BaseCommand):
   
    help = 'Creates loan'
    def handle(self, *args, **options):

        number_loan = 3
        loans_amounts = [1000000,1000000,10000]

        mlo_agents = MLO_AGENT.objects.all()
        mlo_id = 30903425
        index = 520

        today = datetime.datetime.today()


        for num,agent in zip(loans_amounts,mlo_agents):
           amount = LoanAmount.objects.create(loan_amount = num,loan_date = today,repayment_date = today)
           loan = Loan.objects.create(mlo_agent = agent,bps=2.75,File_reference=f"12{index} Any street, California 97720")#,date_closed = one_year_ago)
           index += 1
           self.stdout.write(f'Created mlo: {mlo_agents}')
           
        for  amount in LoanAmount.objects.all():
            for loan in Loan.objects.all():
                loan.amount.add(amount)
                loan.save()
                
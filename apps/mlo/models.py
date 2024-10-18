from django.db import models
from apps.accounts.models import User
from apps.recruiter.models import Loan


class MLO(models.Model):
    loan = models.ForeignKey(Loan,related_name="agent_loans" ,blank= True,null=True,on_delete= models.CASCADE)
    CHOICES = [(str(num), num) for num in range(50,250,25)]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_agent",blank=False,null=False)
    NMLS_sponsor_id = models.CharField(max_length=100,blank = False,null = False)
    NMLS_ID = models.CharField(max_length=100,blank = False,null = False) # unique 7 digits number  3000000 auto increment min_value = 3000000,auto_increment = True
   
    MLO_commission  = models.FloatField(blank = True,null = True)
    date_joined = models.DateTimeField(auto_now = True)
    # flat_Fee = models.FloatField(blank = True,null = True)
    max = models.CharField(max_length= 4,blank = True,null = True,choices=CHOICES)
    
    def __str__(self) -> str:
        return self.user.username	
    

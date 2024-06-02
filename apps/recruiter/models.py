from django.db import models
from django.contrib.auth.models import User
from utils.base import BaseModelMixin
from django.contrib.auth.models import User


class CompPlan(models.Model):
    Flat_Fee             = models.FloatField(default=0)
    Percentage           = models.FloatField()
    Minimum_Compensation = models.FloatField(default=2.75)
    Maximum_Compensation = models.FloatField(default=2750)
    MAX_GCI              = models.FloatField(default=27500)
    FF_MIN_LOAN          = models.IntegerField(default=27500)
    
    def __str__(self) -> str:
        return f"{self.Percentage}"
    
 
    
    
class Bps(models.Model):
    """
		Table that store bps information interval and maxmium value
    """
    bps       = models.FloatField(default=275)
    interval  = models.IntegerField(default=50)
    max_value = models.FloatField()
    
    def __str__(self):
        return f"{self.bps}"
    
    
class LoanBreakPoint(models.Model):
    loan_break_point = models.FloatField(default=1000000)
   

    def __str__(self):
        return f"{self.loan_break_point}"
    
    
class AHF(models.Model):
    commission = models.FloatField()
    loan_per_year = models.IntegerField(default=1)
    loan_per_month = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.commission}"
    
    
class Branch(models.Model):
    commission = models.DecimalField(max_digits=10,decimal_places=2,default=0.7)
    loan_per_year = models.IntegerField(blank=True,null=True)
    loan_per_month = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.commission}"
    
    
     
class Loan(models.Model):
	user = models.ForeignKey(User,blank= True,null=True,on_delete= models.CASCADE)
	amount = models.FloatField()

	def __str__(self):
 		return self.amount



class Company(models.Model):
    name = models.CharField(max_length = 1000,blank=True,null=True)
    cap = models.FloatField()
    company_commission = models.FloatField()
    number_of_loans = models.IntegerField(blank = True,null = True)
    total = models.FloatField()
    def __str__(self):
        return self.name

 
class Recruiter(models.Model):
    name  = models.CharField(max_length=100,null=True,blank=True)
    amount = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.amount}"
    

class MLO(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    level = models.IntegerField(max_length=1)
    def __str__(self):
        return f"{self.level}+"
    

class MLO_AGENT(models.Model):
    user            = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=True)
    NMLS_ID         = models.CharField(max_length = 7,primary_key=True)
    NMLS_ID_SPONSOR = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    first_name      = models.CharField(max_length = 10)
    last_name       = models.CharField(max_length = 10)
    joined_date     = models.DateTimeField(auto_now=True)

    
    def __str__(self) -> str:
        return f"{self.user.username}"
    
    
    
    
class MLO_AGENT_PRODUCTION(models.Model):
    NMLS_ID = models.ForeignKey(MLO_AGENT,on_delete=models.CASCADE,null=False,blank=False)
    loan_id = models.ForeignKey("LOANS",on_delete=models.CASCADE,blank=True,null=True)
    total  = models.FloatField(default=0)
    
    def __str__(self) -> str:
        return f"production - {self.NMLS_ID}"
    
    
    
class LOANS(models.Model):
    NMLS_ID = models.ForeignKey(MLO_AGENT,on_delete=models.CASCADE,blank=True,null=True)
    date_closed = models.DateTimeField()
    



class Edge(models.Model):
    from_node  = models.ForeignKey(MLO_AGENT, on_delete=models.CASCADE, unique=True, related_name='outgoing_edges')
    to_node    = models.ForeignKey(MLO_AGENT, on_delete=models.CASCADE, unique=True, related_name='incoming_edges')
    production = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.from_node.user.username} -> {self.to_node.user.username}"
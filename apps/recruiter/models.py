from django.db import models
from django.contrib.auth.models import User
from utils.base import BaseModelMixin
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 



class CompPlan(models.Model):
    user                 = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    Flat_Fee             = models.FloatField(default=0)
    Percentage           = models.FloatField(default=2.75)
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
    user      = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    bps       = models.FloatField(default=275)
    interval  = models.IntegerField(default=50)
    max_value = models.FloatField(default=275)
    
    def __str__(self):
        return f"{self.bps}"
    
    
class LoanBreakPoint(models.Model):
    user                 = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    loan_break_point     = models.FloatField(default=1000000)

    def __str__(self):
        return f"{self.loan_break_point}"
    
    
class AHF(models.Model):
    commission     = models.FloatField()
    loan_per_year  = models.IntegerField(default=1)
    loan_per_month = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.commission}"
    
    
class Branch(models.Model):
    user           = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,null=False)
    commission     = models.DecimalField(max_digits=10,decimal_places=2,default=0.7)
    loan_per_year  = models.IntegerField(blank=True,null=True)
    loan_per_month = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f"{self.commission}"
    
    





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

    CHOICES = [(num, num) for num in range(50,250,25)]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_mlo",blank=False,null=False)
    NMLS_sponsor_id = models.CharField(max_length=100,blank = False,null = False)
    NMLS_ID = models.CharField(max_length=100,blank = False,null = False) # unique 7 digits number  3000000 auto increment min_value = 3000000,auto_increment = True
   
    MLO_commission  = models.FloatField(blank = True,null = True)
    date_joined = models.DateTimeField(auto_now = True)
    flat_Fee = models.FloatField(blank = True,null = True)
    max = models.CharField(max_length= 4,blank = True,null = True,choices=CHOICES)
    
    def __str__(self) -> str:
        return self.user.username	
    
    
class  LoanAmount(models.Model):
    id = models.AutoField(primary_key=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    memo  = models.CharField(max_length=100,blank=True,null=True)
    order_of   = models.CharField(max_length=100,blank=True,null=True)
    loan_date = models.DateField()
    repayment_date = models.DateField()
    File_reference = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"loan amount {self.loan_amount}"


class LoanSetting(models.Model):
    user = models.ForeignKey(User,blank= False,null=False,on_delete=models.CASCADE)
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

    def __str__(self) -> str:
        return f"{self.month}"



class Loan(models.Model):
    mlo_agent = models.ForeignKey(MLO_AGENT,related_name="mlo_loans" ,blank= True,null=True,on_delete= models.CASCADE)
    amount    = models.ManyToManyField(LoanAmount,default=1,related_name="loans")
    bps       = models.FloatField()
    date_closed = models.DateTimeField(auto_created=False,auto_now_add=True)
    File_reference = models.CharField(max_length=100,blank=False,unique=True)

    
    def __str__(self):
        return f"loan of {self.mlo_agent}"

	
 
class Node(models.Model):
    node_id = models.IntegerField(primary_key=True)
    mlo_agent  = models.ForeignKey(MLO_AGENT,related_name="node_mlo",on_delete=models.CASCADE,blank=False,null=False)
    
    def __str__(self):
        return f"{self.mlo_agent}"

class Edge(models.Model):
    edge_id = models.IntegerField(primary_key=True)
    source_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outgoing_edges')#,unique=True)
    target_node = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='incoming_edges')#,unique=True)

    
    def __str__(self) -> str:
        return f"{self.source_node} --> {self.target_node}"


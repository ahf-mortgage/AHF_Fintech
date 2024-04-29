from django.db import models


class Category(models.Model):
	name = models.CharField(max_length = 100,blank = False,null = False)
	slug = models.SlugField(unique = True)

	def __str__(self):
		return f"{self.name}"


class Expense(models.Model):
	category    = models.ForeignKey(Category, related_name = "expense", on_delete = models.CASCADE)
	name        = models.CharField(max_length = 100)
	expense     = models.FloatField(blank = False,null = False)

	def save(self, *args, **kwargs):
		self.expense = self.expense
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.name}"


class EmployeeWithholding(models.Model):
	Social_Security =  models.FloatField()
	Medicare        =  models.FloatField()
	CA_disability   =  models.FloatField()
	total 			= models.FloatField(blank=True,null=True)
 
	class Meta:
		verbose_name = "Employee Withholding"
		verbose_name_plural = "Employee Withholding"
 
	def save(self, *args, **kwargs):
		self.total = self.Social_Security + self.Medicare + self.CA_disability 
		super().save(*args, **kwargs)
     
	
	def __str__(self) -> str:
		return f"EmployeeWithHoldings_{ self.Social_Security + self.Medicare + self.CA_disability }"


class BranchPayrollLiabilities(models.Model):
    Social_Security =  models.FloatField("Social Security")
    Medicare        =  models.FloatField()
    Fed_Unemploy   =  models.FloatField()
    CA_Unemployment =  models.FloatField("CA Unemployment")
    Employment_Training_Tax =   models.FloatField("Employment Training Tax (ETT)")
    total 			=  models.FloatField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        self.total = self.Social_Security + self.Medicare + self.Fed_Unemploy +  self.Employment_Training_Tax + self.CA_Unemployment 
        super().save(*args, **kwargs)
        
        
    def __str__(self) -> str:
        return f"Social_Security {self.Social_Security}  Medicare {self.Medicare} Fed_Unemploy {self.Fed_Unemploy}"
    
class BranchPayrollLiabilitieQ(models.Model):
    Social_Security =  models.FloatField("Social Security")
    Medicare        =  models.FloatField()
    Fed_Unemploy   =  models.FloatField()
    CA_Unemployment =  models.FloatField("CA Unemployment")
    Employment_Training_Tax =   models.FloatField("Employment Training Tax (ETT)")
    total 			=  models.FloatField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        self.total = float(self.Social_Security) + float(self.Medicare) + float(self.Fed_Unemploy) +  float(self.Employment_Training_Tax) + float(self.CA_Unemployment)
        super().save(*args, **kwargs)
        
        
    def __str__(self) -> str:
        return f"Social_Security"
    



class BranchPayrollLiabilitieR(models.Model):
    Social_Security =  models.FloatField("Social Security")
    Medicare        =  models.FloatField()
    Fed_Unemploy   =  models.FloatField()
    CA_Unemployment =  models.FloatField("CA Unemployment")
    Employment_Training_Tax =   models.FloatField("Employment Training Tax (ETT)")
    total 			=  models.FloatField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        self.total = float(self.Social_Security) + float(self.Medicare) + float(self.Fed_Unemploy) +  float(self.Employment_Training_Tax) + float(self.CA_Unemployment)
        super().save(*args, **kwargs)
        
        
    def __str__(self) -> str:
        return f"Social_Security"
    
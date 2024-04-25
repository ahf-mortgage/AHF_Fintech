from django.db import models


class Category(models.Model):
	name = models.CharField(max_length = 100,blank = False,null = False)
	slug = models.SlugField(unique = True)

	def __str__(self):
		return f"{self.name}"


class Expense(models.Model):
	category = models.ForeignKey(Category, related_name = "expense", on_delete = models.CASCADE)
	name = models.CharField(max_length = 100)
	expense  = models.FloatField(blank = False,null = False)

	def save(self, *args, **kwargs):
		self.expense = 12 * self.expense
		super().save(*args, **kwargs)

	def __str__(self):
		return f"{self.name}"


class EmployeeWithHoldings(models.Model):
	Social_Security =  models.FloatField()
	Medicare        =  models.FloatField()
	CA_disability   =  models.FloatField()
	total 			= models.FloatField()
 
	def save(self, *args, **kwargs):
		self.total = self.Social_Security + self.Medicare + self.CA_disability 
		super().save(*args, **kwargs)
     
	
	def __str__(self) -> str:
		return f"EmployeeWithHoldings_{ self.Social_Security + self.Medicare + self.CA_disability }"


class BranchPayrollLiabilities(models.Model):
    Social_Security =  models.FloatField()
    Medicare        =  models.FloatField()
    Fed_Unemploy   =  models.FloatField()
    Employment_Training_Tax =   models.FloatField()
    CA_Unemployment =  models.FloatField()
    total 			=  models.FloatField(blank=True,null=True)
    
    def save(self, *args, **kwargs):
        self.total = self.Social_Security + self.Medicare + self.Fed_Unemploy +  self.Employment_Training_Tax + self.CA_Unemployment 
        super().save(*args, **kwargs)
        
        
    def __str__(self) -> str:
        return f"{self.Social_Security}"
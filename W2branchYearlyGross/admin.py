from django.contrib import admin


from .models import Category
admin.site.register(Category)


from .models import Expense
@admin.register(Expense)
class YourModelAdmin(admin.ModelAdmin):
    list_filter = ('name', 'category', 'expense')
    list_display = ('name','expense','category')
    
    
from .models import EmployeeWithholding
@admin.register(EmployeeWithholding)
class EmployeeWithHoldingsModelAdin(admin.ModelAdmin):
    list_filter = ('Social_Security', 'Medicare', 'CA_disability')
    list_display = ('Social_Security','Medicare','CA_disability')



from .models import EmployeeWithholdingQ
@admin.register(EmployeeWithholdingQ)
class EmployeeWithHoldingsModelAdin(admin.ModelAdmin):
    list_filter = ('Social_Security', 'Medicare', 'CA_disability')
    list_display = ('Social_Security','Medicare','CA_disability')
    
    
    
from .models import EmployeeWithholdingR
@admin.register(EmployeeWithholdingR)
class EmployeeWithHoldingsModelAdin(admin.ModelAdmin):
    list_filter = ('Social_Security', 'Medicare', 'CA_disability')
    list_display = ('Social_Security','Medicare','CA_disability')


   
from .models import BranchPayrollLiabilities
@admin.register(BranchPayrollLiabilities)
class BranchPayrollLiabilities(admin.ModelAdmin):
    # list_filter = ('Social_Security', 'Medicare', 'CA_disability')
    list_filter = ('Social_Security', 'Medicare')
    
    
from .models import BranchPayrollLiabilitieR 
@admin.register(BranchPayrollLiabilitieR )
class BranchPayrollLiabilitieR (admin.ModelAdmin):
    list_filter = ('Social_Security', 'Medicare')
    
    
from .models import BranchPayrollLiabilitieQ
@admin.register(BranchPayrollLiabilitieQ)
class BranchPayrollLiabilitieQ(admin.ModelAdmin):
    list_filter = ('Social_Security', 'Medicare')
    
    
from .models import Q22
@admin.register(Q22)
class Q22Admin(admin.ModelAdmin):
    list_filter = ('value',)
   
   


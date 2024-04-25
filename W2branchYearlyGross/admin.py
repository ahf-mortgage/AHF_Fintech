from django.contrib import admin


from .models import Category
admin.site.register(Category)


from .models import Expense
@admin.register(Expense)
class YourModelAdmin(admin.ModelAdmin):
    list_filter = ('name', 'category', 'expense')
    list_display = ('name','expense','category')
    
    
from .models import EmployeeWithHoldings
@admin.register(EmployeeWithHoldings)
class EmployeeWithHoldingsModelAdin(admin.ModelAdmin):
    list_filter = ('Social_Security', 'Medicare', 'CA_disability')
    list_display = ('Social_Security','Medicare','CA_disability')




    
from .models import BranchPayrollLiabilities
@admin.register(BranchPayrollLiabilities)
class BranchPayrollLiabilities(admin.ModelAdmin):
    # list_filter = ('Social_Security', 'Medicare', 'CA_disability')
    list_filter = ('Social_Security', 'Medicare')

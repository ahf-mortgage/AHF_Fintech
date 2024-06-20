from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.recruiter.models import (CompPlan,Bps,LoanBreakPoint,Branch)
import numpy as np


data = {
    "bps_from_min_to_max": [
        50,
        100,
        100,
        125,
        150,
        175,
        200,
        225,
        250
    ],
    "gci_for_bps_from_min_to_max": [
        246913400,
        123456700,
        123456700,
        98765360,
        82304466.66666667,
        70546685.71428572,
        61728350,
        54869644.44444445,
        49382680
    ],
    "branch_for_bps_from_min_to_max": [
        49.5,
        99,
        99,
        123.75,
        148.5,
        173.25,
        198,
        222.75,
        247.5
    ],
    "ahf_for_bps_from_min_to_max ": [
        0.5,
        1,
        1,
        1.25,
        1.5,
        1.75,
        2,
        2.25,
        2.5
    ]
}

# Convert the data to a NumPy array
data_array = np.array([
    data["bps_from_min_to_max"],
    data["gci_for_bps_from_min_to_max"],
    data["branch_for_bps_from_min_to_max"],
    data["ahf_for_bps_from_min_to_max "]
]).T

# Convert the NumPy array to a list of dictionaries
rows = [
    dict(zip(data.keys(), row))
    for row in data_array
]

print(rows)




class RecruiterAPIView(APIView):
    """
    A simple API view that returns a JSON response.
    """
    def get_queryset(self,*args,**kwargs):
        return CompPlan.objects.all()
    
    
    def get(self, request):
        
        data = {}
        user = request.user
        
        return Response(data)
        
        try:
            bps = Bps.objects.filter(user = user).first()
        except Bps.DoesNotExist as e:
            raise e
        
        try:
            loan_break_point = LoanBreakPoint.objects.filter(user = user).first()
            
        except LoanBreakPoint.DoesNotExist as e:
            raise e
        
        try:
        
            branch = Branch.objects.filter(user = user).first()
        except Branch.DoesNotExist as e:
            raise e
    

        if not isinstance(request.user, AnonymousUser):
            try:
                comp_plan = CompPlan.objects.all().filter(user = user).first()
            except CompPlan.DoesNotExist as e:
                raise e
            
            gci = bps.bps * loan_break_point.loan_break_point / 10000 + comp_plan.Flat_Fee
            bps_from_min_to_max            = []  # bps from 50 to 250
            branch_for_bps_from_min_to_max = []
            gci_for_bps_from_min_to_max    = []
            ahf_for_bps_from_min_to_max    = []
    
     
            if comp_plan != None:
                if comp_plan.Percentage == 0.0:
                    bps_from_min_to_max              = [0,0] + [num*comp_plan.Percentage for num in range(100,250,25)]+[0]
                    gci_for_bps_from_min_to_max      = [gci/(num or 1) * 10000 for num in bps_from_min_to_max] 
                    ahf_for_bps_from_min_to_max      = [(1 - branch.commission) * num for num in bps_from_min_to_max] 
                    branch_for_bps_from_min_to_max   = [branch.commission * num for num in bps_from_min_to_max]
                else:
                    bps_from_min_to_max              = [50,100] + [num for num in range(100,250,25)]+[250]
                    gci_for_bps_from_min_to_max      = [gci/(num) * 10000 for num in bps_from_min_to_max] 
                    ahf_for_bps_from_min_to_max      = [(1 - branch.commission) * num for num in bps_from_min_to_max] 
                    branch_for_bps_from_min_to_max   = [branch.commission * num for num in bps_from_min_to_max]
        

                data = {
                bps_from_min_to_max,
                gci_for_bps_from_min_to_max,
                branch_for_bps_from_min_to_max,
                ahf_for_bps_from_min_to_max
                }
                print("data=",data)
                    
            else:
                return Response({
                    'msg':f'no comp plan found for user {request.user}'
                })
            
            return Response(data)
        else:
            return Response({
                    'msg':f'no comp plan found for user {request.user}'
                })
            

    def post(self, request):
        data = request.data
        # Perform some processing on the data
        processed_data = {
            'message': 'Data processed successfully',
            'result': data
        }
        return Response(processed_data, status=201)



class CompPlanAPIView(APIView):
    """
    A simple API view that returns a JSON response.
    """
    def get_queryset(self,*args,**kwargs):
    


        return CompPlan.objects.all()


    def get(self,request,*args,**kwargs):
        user = request.user
        loan_break_point     = LoanBreakPoint.objects.filter(user = user).first()
        comp_plan_obj        = CompPlan.objects.filter(user = user).first()
        branch               = Branch.objects.filter(user = user).first()
        data = {
            "flatFee":comp_plan_obj.Flat_Fee,
            "ff1000":comp_plan_obj.FF_MIN_LOAN,
            "percentage":comp_plan_obj.Percentage,
            "max":comp_plan_obj.MAX_GCI,
            "loanBreakPoint":loan_break_point.loan_break_point,
            "split":branch.commission
        }
        return Response(data)
    

    def comp_plan_change_view(self,request):
        """
            This function handle comp plane changes
            
            Flat_Fee=max_gci*loan_below_limits[len(loan_below_limits) -1]/10000

        """
        user   = request.user
        maximumMompensation = request.data.get('maximumMompensation',None)
        maxGci              = request.data.get('maxGci',None)
        compPlan            = request.data.get('compPlan',None)
        FFMINLOAN           = request.data.get('FFMINLOAN',None)
        loanBreak           = request.data.get('loanBreak',None)
        branchAmount        = request.data.get('branchAmount',None)


        loan_break_point     = LoanBreakPoint.objects.filter(user = user).first()
        comp_plan_obj        = CompPlan.objects.filter(user = user).first()
        branch               = Branch.objects.filter(user = user).first()

        Maximum_Compensation =  maximumMompensation
        max_gci              =  maxGci  
        FF_MIN_LOAN          =  compPlan  
        comp_plan            =  FFMINLOAN
        loan_break           =  loanBreak   
        branch_amount        =  branchAmount
        
        if branch_amount != None:
            branch_amount = float(branch_amount)
            if branch_amount > 99:
                branch_amount = 99
    
        MIN_LOAN               =  100000 
        bps                    =  Bps.objects.all().first()
        rows                   = [50] +  [num for num in range(100,275,25)]
        row_counter            = [i-7 for i in range(7,7+ len(rows))]
        
        
        loan_below_limits      = [num for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]  
        gci_result             = [(comp_plan_obj.Percentage * 100) * num / 10000 for num in range(int(loan_break_point.loan_break_point),MIN_LOAN - MIN_LOAN,-MIN_LOAN)]
        peak_loan_below_limits = loan_below_limits[len(loan_below_limits) - 1]
        peak_gci_results       = gci_result[len(gci_result)-1]     
        Flat_Fee               = comp_plan_obj.FF_MIN_LOAN - ((float(comp_plan) * peak_loan_below_limits)/100)
        
    

        if float(max_gci) > float(Maximum_Compensation):
            max_gci = Maximum_Compensation
                    
        if FF_MIN_LOAN != None:
            comp_plan_obj.FF_MIN_LOAN = float(FF_MIN_LOAN)
            comp_plan_obj.save()
            
        
        if branch_amount:
            comp_plan_obj.FF_MIN_LOAN           =  float(FF_MIN_LOAN)
            comp_plan_obj.MAX_GCI               =  max_gci
            comp_plan_obj.Maximum_Compensation  =  float(Maximum_Compensation)
            comp_plan_obj.Flat_Fee              =  Flat_Fee
            comp_plan_obj.Percentage            =  float(comp_plan)
            loan_break_point.loan_break_point   =  loan_break
            branch_amount                       =  int(branch_amount) / 100
            branch.commission                   =  branch_amount
            bps.bps                             =  float(comp_plan) * 100
            
            bps.save()
            loan_break_point.save()
            comp_plan_obj.save()
            branch.save()
            return Response({
                "saved":True
            })  
        return Response({
                "saved":False
            })  



    def post(self, request):
        response = self.comp_plan_change_view(request)
        print("response = ",response)
        data = request.data
        print("data = ",data)
        processed_data = {
            'message': 'Data processed successfully',
            'result': data
        }

        return response






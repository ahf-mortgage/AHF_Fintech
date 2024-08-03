from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from collections import deque
from django.contrib.auth.models import User
from collections import Counter
from apps.recruiter.models import (
    CompPlan,
    Bps,
    LoanBreakPoint,
    Branch,
    Edge,
    Node,
    MLO_AGENT,
    Loan)
from apps.RevenueShare.models import AnnualRevenueShare
from utils.pagination import EdgePagination
from utils.ahf_annual_cap_data import ahf_annual_cap_data as aacd
from .serialzers import NodeSerializer,EdgeSerializer
import numpy as np
import math
from django.utils import timezone




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





class NodeGraphView(ListAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
 

    def get(self, request, *args, **kwargs):
        # john_edges = Edge.objects.filter(source_node__mlo_agent__user__username = "tinsae")
        # ashaton3_edges = Edge.objects.filter(source_node__mlo_agent__user__username = "tinsae")

        edges =  Edge.objects.all() # john_edges.union(ashaton3_edges)

        node_list = Node.objects.all()
        level = 1
   
        data_ = []
        nodes = []
        _edges = []
        level_source_target = {}
        level = 1
        counter  = {

        }

        for node in node_list:
            nodes.append({
                "id":f"{node.pk}",
                "label":node.mlo_agent.user.username
            })

        for edge in edges:
            _edges.append({
                "id": edge.pk,
                "source": f"{edge.source_node.pk}",
                "target": f"{edge.target_node.pk}",
                "label": f'{edge.source_node.mlo_agent.user.username} sponsored {edge.target_node.mlo_agent.user.username}'
                })
        
   
        return Response({
            'nodes':nodes,
            "edges":_edges
        })




class EdgeGraphView(APIView):
    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer

    def get(self, request, *args, **kwargs):
        edges = Edge.objects.all()
        level = 1
        data_ = []
        for obj in edges:
            data = {
               "id":obj.edge_id,
                "source":obj.source_node.mlo_agent.user.username,
                "target": obj.target_node.mlo_agent.user.username
            }
            data_.append(data)
            print("level=",level)
            level += 1
        return Response(data_)


def calculate_commission_for_level_0(node,total_commission,split):
    mlo_agent   = node.mlo_agent
    date_joined = mlo_agent.date_joined
    now = timezone.now()
    # days_since_joined = (now - date_joined).days
    # anniversary_year_days = 365

    # if days_since_joined > anniversary_year_days:
    #     return ahf_amount
    # else:
    #     return 0.8 * ahf_amount

    return split* total_commission


class GetNodeInfo(APIView):
    queryset = Node.objects.all()
    def get(self, request, *args, **kwargs):
        query = request.GET
        found = False
        id = query.get('id',None)
        parent_id = query.get('parent_id',None)
        children = []
        first_node = Node.objects.all()[0]
        first_edge = Edge.objects.filter(source_node=first_node)
        try:
            node = Node.objects.filter(pk = id).first()
            parent_node = Node.objects.filter(pk = parent_id).first()
        except Node.DoesNotExist as e:
            raise e
        try:
            edges = Edge.objects.filter(source_node= node)
            for child in edges:
                children.append(child.target_node.mlo_agent.user.username)     
        except Edge.DoesNotExist as e:
            raise e
        return Response({
            'parent':parent_node.mlo_agent.user.username,
            'mlo':node.mlo_agent.user.username,
            'number_childern':len(edges),
            'children':children
        })




class GetLevelInfo(APIView):
    queryset = Node.objects.all()
    def get(self, request, *args, **kwargs):
        node_id = request.GET.get('node_id',None)
      
        if node_id == None:
            starting_node = Node.objects.all().first()
        starting_node = Node.objects.filter(node_id =node_id).first()
      
        queue         = deque([(starting_node, 0)])
        node_levels   = {starting_node.mlo_agent.user.username: 0}
        data          = []
        level_to_commission = {}
        levels = [i for i in range(1,8)]

        all_revenue_shares = AnnualRevenueShare.objects.all()
        try:
            loan_break_point = LoanBreakPoint.objects.all().first()
        except LoanBreakPoint.DoesNotExist as e:
            raise e
        

            
        try:
            comp_plan        = CompPlan.objects.all().first()
        except CompPlan.DoesNotExist as e:
            raise e

        try:
            bps        = Bps.objects.all().first()
        except Bps.DoesNotExist as e:
            raise e
        

        annual_revenue_shares = []
        test_branch_gross_income  =  aacd.get("test_branch_gross_income",None)
        ahf_amount                =  aacd.get("ahf_amount",1)
        AD9                       =  math.ceil(float(test_branch_gross_income)/float(ahf_amount) * 100)
        split                     = Branch.objects.filter().first().commission
        gci                       =   (comp_plan.Percentage * 100) * loan_break_point.loan_break_point/10000  + comp_plan.Flat_Fee

        for share in all_revenue_shares:
            annual_revenue_shares.append(share.percentage/100)

        for level,AD12 in zip(levels,annual_revenue_shares):
            level_to_commission[0] =  calculate_commission_for_level_0(starting_node,AD9,split)
            AE12 = AD9*AD12
            AG12 = AE12/2
        
            level_to_commission[level] = AG12

        while queue:
            node, level = queue.popleft()
            for edge in node.outgoing_edges.all():
                target_node = edge.target_node
                if target_node not in node_levels:
                    node_levels[target_node.mlo_agent.user.username] = level + 1
                    queue.append((target_node, level + 1))
        for mlo in node_levels:
            mlo_agent = MLO_AGENT.objects.filter(user__username = mlo)
            user      = User.objects.filter(username = mlo).first()
            mlo_agent = MLO_AGENT.objects.filter(user=user).first()
            loan      = Loan.objects.filter(mlo_agent= mlo_agent).first()
        
            print("commission = ",level_to_commission.get(node_levels.get(mlo,None),0))
            _data = {
                'mlo':mlo,
                'level':node_levels.get(mlo,None),
                'commission': level_to_commission.get(node_levels.get(mlo,None),0),
                'loan': len(loan.amount.all()) if loan  != None  else 0,
                'total_amount':sum([amount.loan_amount if loan != None else 0 for amount in loan.amount.all() ]),
                "split":f"{split * 100}%",
                'file_reference':loan.File_reference,
                'loan_amount':loan.amount.all().first().loan_amount,
                'date_funded':loan.amount.all().first().loan_date,
                'gci':f"${gci}",
                'bps':loan.bps,
                'ahf_commission':float(1 - split) * float(gci),
                'branch_commission':float(split) * float(gci)
            }
            data.append(_data)
        return Response(data)


class GetMloLevelInfo(APIView):
    queryset = Node.objects.all()
    def get(self, request, *args, **kwargs):
        mlo_id = request.GET.get('mlo_id',None)
        mlo = MLO_AGENT.objects.filter(id =mlo_id).first()

        user          = request.user
        request_mlo   = MLO_AGENT.objects.filter(user = user).first()
        request_agent = Node.objects.filter(mlo_agent= request_mlo).first()
        starting_node = request_agent
        queue         = deque([(starting_node, 0)])
        node_levels   = {starting_node.mlo_agent.user.username: 0}

        while queue:
            node, level = queue.popleft()
            for edge in node.outgoing_edges.all():
                target_node = edge.target_node
                if target_node not in node_levels:
                    node_levels[target_node.mlo_agent.user.username] = level + 1
                    queue.append((target_node, level + 1))
    
        return Response({
            'level':node_levels.get(mlo.user.username)
        })

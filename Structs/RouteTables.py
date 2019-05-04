class RouteTables():
    id=0
    StepTable=[]
    DjTree=[]
    RouteTable={}
    def __init__(self,id=0,DjTree=[],StepTable=[],RouteTable={}):
        self.id=id
        self.StepTable=StepTable
        self.DjTree=DjTree
        self.RouteTable=RouteTable

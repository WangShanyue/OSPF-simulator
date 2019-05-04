
class TableViewStruct():# 输出到每一个表中的路由器交互信息
    id=0
    Str=""
    def __init__(self,id,str):
        self.id=id
        self.Str=str

if __name__ == '__main__':
    test=''
    if(True):
        test=str('TableViewStruct(1,\'0\')')
        print(test)
    obj=eval(test)
    print(obj.Str)

from enum import Enum
class InfoType(Enum):
    NONE=0
    DJMAP=1


class AccessInfoStruct():#Socket传递消息的消息结构
    type=InfoType.NONE
    Str=""
    def __init__(self,type,Str):
        self.type=type
        self.Str=Str

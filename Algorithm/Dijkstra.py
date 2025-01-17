import copy
INF= 214748364
def dijkstra(graph,pos):
    node_num=len(graph)
    list = [[0,0,False] for col in range(node_num)]  #(adjvex,distance,finish)
    ListNoteTable=[]#把每一步的list都记录下来
    RouteTable={}#路由表
  #  print(list)
    for i in range(node_num):#初始化
        list[i]=[pos,graph[pos][i],False]
    list[pos] = [pos, 0, False]
    ListNoteTable.append(copy.deepcopy(list))
    list[pos]=[pos,0,True]
    ListNoteTable.append(copy.deepcopy(list))
    for i in range(node_num):
        if(i==pos):
            continue
        RouteTable[i]=i
    for k in range(node_num-1):
        min_num = INF
        min_pos = 0
        for j in range(node_num):  # 获得最小值并赋值为True
            if(list[j][2]==True):continue
            if (min_num > list[j][1]):
                min_num = list[j][1]
                min_pos = j

        if (list[min_pos][1] < INF):#如果值太大就退出
            list[min_pos][2] = True
        else:
            break

        for i in range(node_num):
            if (list[i][2] == True or list[min_pos][1]>=INF): continue
            if(list[min_pos][1]+graph[min_pos][i]<list[i][1]):#原点到最小点的距离+最小点到目标点的距离小于原点到目标点的距离
                list[i][1] = list[min_pos][1] + graph[min_pos][i]
                list[i][0]=min_pos
                RouteTable[i]=RouteTable[min_pos]
        temp=copy.deepcopy(list)
        ListNoteTable.append(temp)
    tree =[[] for col in range(node_num)] #建立空表

    for i in range(node_num):
        if(list[i][2]==False):
            del(RouteTable[i])


    for i in range(node_num):
        if (i==pos or list[i][2]==False) :continue
        tree[list[i][0]].append(i)
    return tree,ListNoteTable,RouteTable
        #for i in range

if __name__ == '__main__':
   graph=  [[214748364, 2147483647, 214748364, 214748364, 214748364], [214748364, 214748364, 100, 214748364, 214748364], [214748364, 100, 214748364, 100, 100], [214748364, 214748364, 100, 214748364, 214748364], [214748364, 214748364, 100, 214748364, 214748364]]

   dijkstra(graph,4)
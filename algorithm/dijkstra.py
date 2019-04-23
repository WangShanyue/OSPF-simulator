INF= 214748364
def dijkstra(graph,pos):
    node_num=len(graph)
    list = [[0,0,False] for col in range(node_num)]  #(adjvex,distance,finish)
  #  print(list)
    for i in range(node_num):#初始化
        list[i]=[pos,graph[pos][i],False]
        if(i==pos):
            list[i]=[pos,0,True]
    for k in range(node_num-1):
        min_num = INF
        min_pos = 0
        for j in range(node_num):  # 获得最小值并赋值为True
            if(list[j][2]==True):continue
            if (min_num > list[j][1]):
                min_num = list[j][1]
                min_pos = j
        list[min_pos][2] = True
        for i in range(node_num):
            if (list[i][2] == True): continue
            if(list[min_pos][1]+graph[min_pos][i]<list[i][1]):#原点到最小点的距离+最小点到目标点的距离小于原点到目标点的距离
                list[i][1] = list[min_pos][1] + graph[min_pos][i]
                list[i][0]=min_pos
    tree =[[] for col in range(node_num)] #建立空表
    min_pos=0
    for i in range(node_num):
        if (i==pos) :continue
        tree[list[i][0]].append(i)
    return tree
        #for i in range

if __name__ == '__main__':
   graph=  [[214748364, 100, 214748364, 214748364, 214748364], [100, 214748364, 100, 214748364, 214748364], [214748364, 100, 214748364, 100, 100], [214748364, 214748364, 100, 214748364, 214748364], [214748364, 214748364, 100, 214748364, 214748364]]

   dijkstra(graph,4)
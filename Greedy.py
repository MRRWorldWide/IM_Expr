import numpy as np
import copy
import ICmodel


# 读取图的关系矩阵
graph_data = np.loadtxt('graph.txt')

# 初始节点集
init_set = []

# 激活节点个数
spread_num = 0

print("**********贪心+IC@IM结果**********")

# （贪心算法）往S中加入新节点，使得每次加入后激活的节点数最多
# 当所有节点都被激活时停止循环
# f = open('result.txt', 'a')
while spread_num != len(graph_data):
    max_spread_num = 0
    for index in range(len(graph_data)):
        if index not in init_set:
            test_S = copy.deepcopy(init_set)
            test_S.append(index)
            result_spread_num = ICmodel.ICModel(graph_data, test_S)
            if result_spread_num >= max_spread_num:
                max_spread_num = result_spread_num
                max_spread_node = index
    spread_num = max_spread_num
    init_set.append(max_spread_node)
    print("init_num: ", len(init_set), " spread_num: ", max_spread_num, " S:", init_set)
    # f.write("init_num: " + str(len(init_set)) + " spread_num: " + str(max_spread_num) + " S:" + str(init_set) + "\n")

# f.close()

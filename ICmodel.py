import numpy as np
import copy
import random


# IC模型
# 输入：图的邻接矩阵、初始节点集S
# 输出：感染点的个数
def ICModel(data, init_set) -> int:
    # 激活集A，存储本轮被激活的所有点
    # 初始值为S
    active_set = init_set

    # 所有节点的激活状态
    # 0为未激活，1为激活
    active_status_set = np.zeros(len(data), dtype=int)

    # 激活所有起始点
    for index2 in range(len(init_set)):
        active_status_set[init_set[index2]] = 1

    # 开始循环
    while active_status_set.sum() < len(data):

        # 激活集A的非激活邻居集N
        # 存储本轮可能被传染的点
        neighbor_set = []

        # 取出未激活可达点，及点的所有有效边的概率
        p_dictionary = {}
        for d_index in range(len(data)):
            for s_index in range(len(active_set)):
                # 可达且未被激活
                if data[active_set[s_index], d_index] != 0.0 and active_status_set[d_index] != 1:
                    if d_index not in neighbor_set:
                        neighbor_set.append(d_index)
                        p_dictionary[d_index] = []
                    p_dictionary[d_index].append(data[active_set[s_index], d_index])

        # 出口：不存在未激活可达点
        if len(neighbor_set) == 0:
            break

        # 计算未激活可达点的激活概率
        # neighbor_p_set = []
        # for index2 in range(len(neighbor_set)):
        #     p_one = p_dictionary[neighbor_set[index2]]
        #     p = 1.0
        #     for i in range(len(p_one)):
        #         p = p * (1 - p_one[i])
        #     p = 1 - p
        #     neighbor_p_set.append(p)

        # 清空A集
        active_set = []

        # 激活
        for index3 in range(len(neighbor_set)):
            p_this = p_dictionary[neighbor_set[index3]]
            for p in p_this:
                seed = random.random()
                if seed < p:
                    active_status_set[neighbor_set[index3]] = 1
                    active_set.append(neighbor_set[index3])

        # 如果没有新的节点被激活，传播停止
        if len(active_set) == 0:
            break

    # print(init_set, active_status_set)
    # 传播结束返回传播的节点数
    return active_status_set.sum()


# 验证random均匀分布
def test_rnd():
    r01 = 0
    r12 = 0
    r23 = 0
    r34 = 0
    r45 = 0
    r56 = 0
    r67 = 0
    r78 = 0
    r89 = 0
    r910 = 0

    for i in range(10000000):
        x = random.random() * 10
        if 0 <= x < 1:
            r01 += 1
        if 1 <= x < 2:
            r12 += 1
        if 2 <= x < 3:
            r23 += 1
        if 3 <= x < 4:
            r34 += 1
        if 4 <= x < 5:
            r45 += 1
        if 5 <= x < 6:
            r56 += 1
        if 6 <= x < 7:
            r67 += 1
        if 7 <= x < 8:
            r78 += 1
        if 8 <= x < 9:
            r89 += 1
        if 9 <= x < 10:
            r910 += 1

    print("******random()均匀分布验证结果******")
    print("0~1：", r01)
    print("2~3：", r12)
    print("3~4：", r23)
    print("4~5：", r34)
    print("5~6：", r45)
    print("6~7：", r56)
    print("7~8：", r67)
    print("8~9：", r78)
    print("9~10：", r910)

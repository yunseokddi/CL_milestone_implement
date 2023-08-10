import numpy as np

sample_list = [[97.80000305175781], [93.9000015258789, 95.20000457763672], [91.9000015258789, 93.20000457763672, 93.9000015258789], [90.9000015258789, 87.70000457763672, 93.10000610351562, 92.70000457763672], [90.20000457763672, 84.50000762939453, 90.10000610351562, 91.80000305175781, 90.20000457763672], [87.70000457763672, 83.50000762939453, 88.60000610351562, 89.30000305175781, 88.4000015258789, 84.60000610351562], [88.00000762939453, 81.80000305175781, 87.4000015258789, 89.20000457763672, 88.30000305175781, 84.20000457763672, 88.50000762939453], [87.50000762939453, 81.30000305175781, 86.60000610351562, 88.4000015258789, 88.20000457763672, 83.4000015258789, 86.30000305175781, 86.70000457763672], [87.60000610351562, 80.20000457763672, 87.10000610351562, 88.10000610351562, 87.60000610351562, 83.00000762939453, 86.10000610351562, 86.00000762939453, 92.10000610351562], [85.70000457763672, 78.80000305175781, 87.10000610351562, 85.60000610351562, 85.4000015258789, 82.4000015258789, 84.60000610351562, 84.50000762939453, 89.80000305175781, 87.50000762939453]]

num = 0

forgetting_list = []

for i in range(9):
    max_num = -1.0
    min_num = 300.0
    for j in range(num,10):
        if sample_list[j][i] > max_num:
            max_num = sample_list[j][i]

        if sample_list[j][i] < min_num:
            min_num = sample_list[j][i]

    forgetting_list.append(max_num-min_num)

    num += 1

print("forgetting : {:.3f}".format(sum(forgetting_list)/len(forgetting_list)))
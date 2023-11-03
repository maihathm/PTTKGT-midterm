import numpy as np
probability = [[1,2,3],[4,5,6]]
city_list = [[1,2,3],[4,5,6]]

for i in range(0, len(probability)):
        temp=sum([probability[i][0] for i in range(0,len(probability))])
        if (i+1 not in city_list and temp != 0):
            temp=sum([probability[i][0] for i in range(0,len(probability))])
            probability[i][1] = int(probability[i][0]/temp)
print(probability)

probability_ = np.array([[1,2,3],[4,5,6]])
for i in range(0, probability_.shape[0]):
        if (i+1 not in city_list and probability_[:,0].sum() != 0):
            probability_[i, 1] = probability_[i, 0]/probability_[:,0].sum()
print(probability_)

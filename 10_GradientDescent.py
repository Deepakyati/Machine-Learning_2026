import numpy as np


# m - slope
# b - intercept
# mb - m derivatives
# bd - b derivatives


def gradient_descent(x,y):
    m_curr=b_curr=0
    iterations=100
    n=len(x)
    learning_rate=0.08
    for i in range(iterations):
        y_predicted=m_curr*x+b_curr
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m {}, b {}, cost {},iterations {}".format(m_curr, b_curr,cost,i))

x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_descent(x,y)


"""python 10_GradientDescent.py
m 0.062, b 0.018000000000000002, cost 89.0,iterations 0
m 0.122528, b 0.035592000000000006, cost 84.881304,iterations 1
m 0.181618832, b 0.052785648000000004, cost 80.955185108544,iterations 2
m 0.239306503808, b 0.069590363712, cost 77.21263768455901,iterations 3
m 0.29562421854195203, b 0.086015343961728, cost 73.64507722605434,iterations 4
m 0.35060439367025875, b 0.10206956796255283, cost 70.2443206760065,iterations 5
m 0.40427867960173774, b 0.11776180246460617, cost 67.00256764921804,iterations 6
m 0.4566779778357119, b 0.13310060678206653, cost 63.912382537082294,iterations 7
m 0.5078324586826338, b 0.14809433770148814, cost 60.966677449199324,iterations 8
m 0.5577715785654069, b 0.16275115427398937, cost 58.15869595270883,iterations 9"""
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

# Simulating Social Networks
# Neeraj Joshi

#1a:  for i in 1,…,n respondents simulate a position in a 2-dimensional
#     space using a draw from a 2d normal distribution

mu, sigma = 0, 0.5 # mean and standard deviation
point_list = []
x = []
y = []
n = 5

for item in range(n):
    xVal = np.random.normal(mu, sigma)
    yVal = np.random.normal(mu, sigma)  
    x.append(xVal)
    y.append(yVal)
    point_list.append((xVal, yVal))
#print x
#print y
#print point_list
    
def euc_distance(x1, y1, x2, y2):
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

def draw_edge(x1, y1, x2, y2, dist, a):
    test = np.random.binomial(1, (exp(a * dist))/(1 + exp(a * dist)), 1)
    if(test == 1):
        plt.plot([x1, x2], [y1, y2], color = 'k', linestyle = '-')
        
def euc_distance_matrix(points):
    matrix = []
    for i in range(n):
        new_row = []
        first_point = points[i]
        for item in points:
            dist = euc_distance(first_point[0], first_point[1], item[0], item[1])
            new_row.append(str(dist))
            draw_edge(first_point[0], first_point[1], item[0], item[1], dist, 0.1) 
        matrix.append(new_row)    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print "                     ".join(row)                                             


matrix_test = euc_distance_matrix(point_list)
#print_matrix(matrix_test)
   


print euc_distance(0, 10, 0, 5)

for item in point_list:
    plt.plot(item[0], item[1], '.b')



plt.axis([-2.5, 2.5, -2.5, 2.5])
plt.show()

#n, p = 1, .5 # number of trials, probability of each trial
#s = np.random.binomial(n, p, 10)
#print s

#Covarities

for individual in point_list:
    beta0 = 0.1
    beta1 = 0.1
    beta2 = 0.2
    age = int(np.random.uniform(1, 91))
    gender = np.random.binomial(1, 0.5, 1)
    """
    if(gender == 1):
        gender = 'male'
    else:
        gender = 'female'
    """
    outcome = np.random.normal(beta0 + beta1 * gender + beta2 * age, 10)
    individual = (individual[0], individual[1], age, gender[0], outcome)
    print individual



























"""
mu, sigma = 0, 0.1
matrix = []
n = 100

for item in range(n):
    print item

for x in range(0, n):
    matrix.append(["O"] * n)

def print_matrix(matrix):
    for row in matrix:
        print " ".join(row)




numpy.zeros((5,5))
print numpy.zeros((5,5))

mu, sigma = 0, 0.1 # mean and standard deviation
s = numpy.random.normal(mu, sigma, 1000)
print s


import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 30, normed=True)
plt.plot(bins, 1/(sigma * numpy.sqrt(2 * numpy.pi)) *
numpy.exp( - (bins - mu)**2 / (2 * sigma**2) ),
linewidth=2, color='r')
plt.show()
"""

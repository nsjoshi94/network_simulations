import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

# Simulating Social Networks
# Neeraj Joshi


mu, sigma = 0, 0.5 # mean and standard deviation
point_list = []
x = [] #x coordinates 
y = [] #y coordinates
n = 12 #individuals in the network

for item in range(n):
    xVal = np.random.normal(mu, sigma)
    yVal = np.random.normal(mu, sigma)  
    x.append(xVal)
    y.append(yVal)
    point_list.append((xVal, yVal))
#print x
#print y
#print point_list

#plots points from a list of points
for item in point_list:
    plt.plot(item[0], item[1], '.b')

#takes in two points and returns the distance between them 
def euc_distance(x1, y1, x2, y2):
    distance = sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

#draws an edge according to a binomial distribution with probability
# p = e^(dist * a)/ (1 + e^(dist * a))
def draw_edge(x1, y1, x2, y2, dist, a):
    test = np.random.binomial(1, (exp(a * dist))/(1 + exp(a * dist)), 1)
    if(test == 1):
        plt.plot([x1, x2], [y1, y2], color = 'k', linestyle = '-')

#given a list of points represented as tuples, calculates the euclidean distance
#between any two points and stores them in a matrix. This matrix is then returned
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

#prints a matrix in a form which is visually appealing
def print_matrix(matrix):
    for row in matrix:
        print "                     ".join(row)                                             



#print matrix_test
#print_matrix(matrix_test)
matrix_test = euc_distance_matrix(point_list)
plt.axis([-1.5, 1.5, -1.5, 1.5])
plt.show()

#n, p = 1, .5 # number of trials, probability of each trial
#s = np.random.binomial(n, p, 10)
#print s

#Covarities

#adding some data for each individual, determining an age from a uniform distribution
#and determining a gender from a probability distribution with p = 0.5. Finially assigning
#an outcome by taking a normal distribution with p = beta0 + beta1 * gender + beta2 * age
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

#Testing with modules in Python, Numpy and SciPy
#Also experimenting with matrices and graphing using matplotlib
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
